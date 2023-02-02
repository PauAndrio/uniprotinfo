from flask import Flask, render_template, url_for, request, redirect
from config import config, PREFIX
from model import db, User, Userdata, Seqanalysis
from forms import SignUpForm, LoginForm, UniprotForm
from uniprot_api import get_unipro_info_tuple
from flask_bcrypt import bcrypt
from flask_login import login_user, login_required, logout_user, LoginManager, current_user

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.config.from_object(config['producction'])
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, (int(user_id)))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginerror = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.checkpw(form.password.data.encode('utf8'), user.password):
                login_user(user)
                return redirect(url_for('userspace'))
        loginerror = "Invalid email or password."
    return render_template('auth/login.html', form=form, loginerror=loginerror )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf8'), bcrypt.gensalt())
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.flush()
        db.session.refresh(new_user)
        new_user_data = Userdata(name=form.name.data, surname=form.surname.data,
                                 institution=form.institution.data, user_id=new_user.id)
        db.session.add(new_user_data)
        db.session.commit()
        return redirect(url_for('userspace'))

    return render_template('auth/signup.html', form=form)

@app.route('/userspace', methods=['GET', 'POST'])
@login_required
def userspace():
    user = db.session.get(User, (int(current_user.id)))
    form = UniprotForm()
    if form.validate_on_submit():
        seqanalysis = Seqanalysis.query.filter_by(uniprot=form.uniprot.data).first()
        if not seqanalysis:
            try: 
                uniprot_info_tuple = get_unipro_info_tuple(form.uniprot.data)
                seqanalysis =  Seqanalysis(uniprot=uniprot_info_tuple[0], sequence=uniprot_info_tuple[1], mol_weight=uniprot_info_tuple[2])
            except Exception as e:
                print(e)
        if seqanalysis:
            user.sequences.append(seqanalysis)
            db.session.add(user)
            db.session.commit()

    return render_template('userspace.html', form=form, user_sequences=user.sequences)

@app.route('/seqanalysis/<seqanalysis_id>')
@login_required
def seqanalysis(seqanalysis_id):
    seqanalysis = db.session.get(Seqanalysis, (int(seqanalysis_id)))
    if seqanalysis in current_user.sequences:
        return render_template('seqanalysis.html', seqanalysis=seqanalysis)
    else:
        return redirect(url_for('userspace'))


hostedApp = Flask(__name__)
hostedApp.config.from_object(config['development'])
hostedApp.wsgi_app = DispatcherMiddleware(NotFound(), {f"{PREFIX}":app})


if __name__ == "__main__":
    hostedApp.run()