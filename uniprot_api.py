from Bio.SeqUtils.ProtParam import ProteinAnalysis
import requests


def get_unipro_info_tuple(uniprot_accession_code):
    sequence = get_sequence(uniprot_accession_code)
    mol_weight = ProteinAnalysis(sequence).molecular_weight()
    return uniprot_accession_code, sequence, mol_weight


# def get_sequence(uniprot_accession_code):
#    url = f'https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=json&query=accession={uniprot_accession_code}&fields=sequence'
#    return next(iter(requests.get(url).json().get('results') or []), None).get('sequence').get('value')


def get_sequence(uniprot_accession_code):
    url = f'https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=json&query=accession={uniprot_accession_code}&fields=sequence'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data.get('results')
        if results:
            first_result = results[0]
            sequence = first_result.get('sequence')
            if sequence:
                return sequence.get('value')

    return None
