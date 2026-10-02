"""
Módulo de Triagem Virtual Inicial
Objetivo: Carregar dados do PubChem, calcular propriedades (RDKit) e filtrar compostos.
"""

import os
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

def carregar_dados(caminho_arquivo):
    """Lê um arquivo CSV contendo IDs de compostos e sequências SMILES."""
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
    return pd.read_csv(caminho_arquivo)

def calcular_propriedades(df):
    """Calcula Peso Molecular, LogP, Doadores e Aceitadores de H."""
    pesos, logs, hbd, hba = [], [], [], []
    
    for smiles in df['smiles']:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            pesos.append(Descriptors.MolWt(mol))
            logs.append(Descriptors.MolLogP(mol))
            hbd.append(Descriptors.CalcNumHBD(mol))
            hba.append(Descriptors.CalcNumHBA(mol))
        else:
            pesos.append(None)
            logs.append(None)
            hbd.append(None)
            hba.append(None)
            
    df['Molecular_Weight'] = pesos
    df['LogP'] = logs
    df['H_Donors'] = hbd
    df['H_Acceptors'] = hba
    return df

def filtrar_candidatos(df):
    """Aplica filtro baseado na Regra de Lipinski."""
    return df[
        (df['Molecular_Weight'] <= 500) & 
        (df['LogP'] <= 5) & 
        (df['H_Donors'] <= 5) & 
        (df['H_Acceptors'] <= 10)
    ]

if __name__ == "__main__":
    # Caminho corrigido apontando para os dados baixados do PubChem
    input_path = "data/moleculas_pubchem.csv"
    output_path = "outputs/candidatos_filtrados.csv"
    
    os.makedirs("outputs", exist_ok=True)
    
    print("[INFO] Iniciando triagem virtual com dados do PubChem...")
    df_mol = carregar_dados(input_path)
    df_calc = calcular_propriedades(df_mol)
    df_filtrado = filtrar_candidatos(df_calc)
    
    df_filtrado.to_csv(output_path, index=False)
    print(f"[SUCESSO] Triagem concluída! {len(df_filtrado)} compostos aprovados salvos em {output_path}")
