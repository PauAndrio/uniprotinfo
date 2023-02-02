from Bio.SeqUtils.ProtParam import ProteinAnalysis
import requests

def get_unipro_info_tuple(uniprot_accession_code):
    sequence = get_sequence(uniprot_accession_code)
    mol_weight = ProteinAnalysis(sequence).molecular_weight()
    return uniprot_accession_code, sequence, mol_weight 

def get_sequence(uniprot_accession_code):
    url = f'https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=json&query=accession={uniprot_accession_code}&fields=sequence'
    return next(iter(requests.get(url).json().get('results') or []), None).get('sequence').get('value')    
