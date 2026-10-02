"""
Módulo de Relatório Rascunho
Objetivo: Exibir os resultados da triagem virtual de forma clara no terminal.
"""

import os
import pandas as pd

def gerar_relatorio():
    caminho_saida = "outputs/candidatos_filtrados.csv"
    
    if not os.path.exists(caminho_saida):
        print(f"[AVISO] Arquivo de resultados não encontrado em {caminho_saida}. Execute a triagem primeiro.")
        return
        
    df = pd.read_csv(caminho_saida)
    
    print("\n" + "="*50)
    print(" RELATÓRIO RASCUNHO - CANDIDATOS APROVADOS (LIPINSKI)")
    print("="*50)
    print(f"Total de compostos aprovados: {len(df)}\n")
    
    if len(df) > 0:
        # Exibe as colunas principais das primeiras moléculas
        colunas_interesse = ['ID', 'smiles', 'Molecular_Weight', 'LogP']
        print(df[colunas_interesse].to_string(index=False))
    else:
        print("Nenhum composto passou nos critérios de filtragem.")
        
    print("="*50 + "\n")

if __name__ == "__main__":
    gerar_relatorio()
