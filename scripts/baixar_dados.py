"""
Módulo de Coleta de Dados Públicos
Objetivo: Baixar dados de moléculas do PubChem para o pipeline de triagem.
"""

import os
import urllib.request
import json

def baixar_moleculas_pubchem(termo_busca="aspirin", saida_csv="data/moleculas_pubchem.csv"):
    """Busca compostos no PubChem por nome e salva um arquivo CSV com os SMILES."""
    os.makedirs("data", exist_ok=True)
    
    print(f"[INFO] Consultando o PubChem para o termo: '{termo_busca}'...")
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{termo_busca}/property/CanonicalSMILES,MolecularWeight/json"
    
    try:
        with urllib.request.urlopen(url) as resposta:
            dados = json.loads(resposta.read().decode())
            
        propriedades = dados['PropertyTable']['Properties']
        
        # Montando o conteúdo CSV de forma limpa
        linhas = ["ID,smiles,Molecular_Weight_PubChem\n"]
        for item in propriedades:
            cid = item.get('CID')
            smiles = item.get('CanonicalSMILES')
            mw = item.get('MolecularWeight')
            if smiles:
                linhas.append(f"PubChem_{cid},{smiles},{mw}\n")
                
        with open(saida_csv, 'w', encoding='utf-8') as f:
            f.writelines(linhas)
            
        print(f"[SUCESSO] Dados salvos com sucesso em {saida_csv}!")
        
    except Exception as e:
        print(f"[ERRO] Falha ao conectar com a API do PubChem: {e}")

if __name__ == "__main__":
    baixar_moleculas_pubchem(termo_busca="aspirin")
