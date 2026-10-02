"""
Módulo de Coleta de Dados com Fallback de Segurança
Objetivo: Buscar dados do PubChem via API ou usar dados locais se o servidor estiver ocupado.
"""

import os
import urllib.request
import json

def baixar_ou_gerar_dados(saida_csv="data/moleculas_pubchem.csv"):
    os.makedirs("data", exist_ok=True)
    cids = [2244, 3672, 1983]
    cids_str = ",".join(map(str, cids))
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cids_str}/property/CanonicalSMILES,MolecularWeight/json"
    
    try:
        print(f"[INFO] Consultando o PubChem para os CIDs: {cids_str}...")
        with urllib.request.urlopen(url) as resposta:
            dados = json.loads(resposta.read().decode())
            
        propriedades = dados['PropertyTable']['Properties']
        linhas = ["ID,smiles,Molecular_Weight_PubChem\n"]
        for item in propriedades:
            cid = item.get('CID')
            smiles = item.get('CanonicalSMILES')
            mw = item.get('MolecularWeight')
            if smiles:
                linhas.append(f"PubChem_{cid},{smiles},{mw}\n")
                
        with open(saida_csv, 'w', encoding='utf-8') as f:
            f.writelines(linhas)
        print(f"[SUCESSO] Dados obtidos via API e salvos em {saida_csv}!")
        
    except Exception as e:
        print(f"[AVISO] Servidor do PubChem ocupado ({e}). Usando dados locais de segurança...")
        # Dados de fallback garantidos (Aspirina, Ibuprofeno, Paracetamol)
        dados_fallback = (
            "ID,smiles,Molecular_Weight_PubChem\n"
            "PubChem_2244,CC(=O)OC1=CC=CC=C1C(=O)O,180.16\n"
            "PubChem_3672,CC(C)CC1=CC=C(C=C1)C(C)C(=O)O,206.28\n"
            "PubChem_1983,CC(=O)NC1=CC=C(O)C=C1,151.16\n"
        )
        with open(saida_csv, 'w', encoding='utf-8') as f:
            f.write(dados_fallback)
        print(f"[SUCESSO] Dados de fallback carregados com sucesso em {saida_csv}!")

if __name__ == "__main__":
    baixar_ou_gerar_dados()
