import os
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, Reference

# Garantir que a pasta outputs existe
os.makedirs("outputs", exist_ok=True)

# Ler os dados dos candidatos filtrados do seu pipeline
try:
    df = pd.read_csv("outputs/candidatos_filtrados.csv")
except Exception:
    print("Aviso: Arquivo de candidatos filtrados não encontrado. Usando dados de exemplo.")
    data = {
        'ID': ['PubChem_2244', 'PubChem_3672', 'PubChem_1983'],
        'smiles': ['CC(=O)OC1=CC=CC=C1C(=O)O', 'CC(C)CC1=CC=C(C=C1)C(C)C(=O)O', 'CC(=O)NC1=CC=C(C=C1)O'],
        'Molecular_Weight': [180.16, 206.28, 151.16],
        'LogP': [1.31, 3.07, 1.35],
        'H_Donors': [1, 1, 2],
        'H_Acceptors': [3, 2, 1]
    }
    df = pd.DataFrame(data)

# Criar o arquivo do Excel
wb = openpyxl.Workbook()

# Aba 1: Dashboard Executivo
ws_dash = wb.active
ws_dash.title = "Dashboard"
ws_dash.views.sheetView[0].showGridLines = True

# Aba 2: Dados Brutos do Pipeline
ws_data = wb.create_sheet(title="Dados Moleculares")
ws_data.views.sheetView[0].showGridLines = True

# Cores e Estilos Profissionais (Tema Verde Biologia/Quimioinformática)
primary_fill = PatternFill(start_color="1B4332", end_color="1B4332", fill_type="solid")
header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")

accent_fill = PatternFill(start_color="D8F3DC", end_color="D8F3DC", fill_type="solid")
card_title_font = Font(name="Segoe UI", size=10, bold=True, color="2D6A4F")
card_value_font = Font(name="Segoe UI", size=16, bold=True, color="1B4332")

thin_border = Border(
    left=Side(style='thin', color='CCCCCC'),
    right=Side(style='thin', color='CCCCCC'),
    top=Side(style='thin', color='CCCCCC'),
    bottom=Side(style='thin', color='CCCCCC')
)

# Preencher Aba de Dados Brutos
headers = ['ID da Molécula', 'Estrutura SMILES', 'Peso Molecular (g/mol)', 'LogP (Lipofilicidade)', 'Doadores H', 'Aceitadores H', 'Status Lipinski']
ws_data.append(headers)

for col_num, header in enumerate(headers, 1):
    cell = ws_data.cell(row=1, column=col_num)
    cell.fill = primary_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal='center', vertical='center')

for idx, row in df.iterrows():
    ws_data.append([
        row['ID'], 
        row['smiles'], 
        float(row['Molecular_Weight']), 
        float(row['LogP']), 
        int(row['H_Donors']), 
        int(row['H_Acceptors']), 
        'Aprovado'
    ])

# Formatar as células da aba de dados
for row in range(2, len(df) + 2):
    for col in range(1, 8):
        cell = ws_data.cell(row=row, column=col)
        cell.font = Font(name="Segoe UI", size=10)
        cell.border = thin_border
        if col in [3, 4]:
            cell.number_format = '#,##0.00'
            cell.alignment = Alignment(horizontal='right')
        elif col in [5, 6]:
            cell.number_format = '#,##0'
            cell.alignment = Alignment(horizontal='center')
        else:
            cell.alignment = Alignment(horizontal='center' if col == 1 or col == 7 else 'left')

# Construção do Dashboard Interativo na Aba 1
ws_dash['B2'] = "PAINEL EXECUTIVO: TRIAGEM VIRTUAL DE FÁRMACOS"
ws_dash['B2'].font = Font(name="Segoe UI", size=16, bold=True, color="1B4332")

ws_dash['B3'] = "Monitoramento de Propriedades Físico-Químicas baseadas na Regra de Lipinski"
ws_dash['B3'].font = Font(name="Segoe UI", size=10, italic=True, color="555555")

# Função para criar os Cards de Indicadores (KPIs) com fórmulas do Excel
def create_card(ws, start_col, start_row, title, formula, number_format=None):
    ws.merge_cells(start_row=start_row, start_column=start_col, end_row=start_row, end_column=start_col+1)
    ws.merge_cells(start_row=start_row+1, start_column=start_col, end_row=start_row+2, end_column=start_col+1)
    
    t_cell = ws.cell(row=start_row, column=start_col, value=title)
    t_cell.font = card_title_font
    t_cell.alignment = Alignment(horizontal='center', vertical='center')
    
    v_cell = ws.cell(row=start_row+1, column=start_col, value=formula)
    v_cell.font = card_value_font
    v_cell.alignment = Alignment(horizontal='center', vertical='center')
    if number_format:
        v_cell.number_format = number_format
        
    for r in range(start_row, start_row+3):
        for c in range(start_col, start_col+2):
            cell = ws.cell(row=r, column=c)
            cell.fill = accent_fill
            cell.border = thin_border

# Adicionar os KPIs puxando dados da outra aba
max_row_data = len(df) + 1
create_card(ws_dash, start_col=2, start_row=5, title="Total de Compostos", formula=f"=COUNTA('Dados Moleculares'!A2:A{max_row_data})")
create_card(ws_dash, start_col=5, start_row=5, title="Peso Molecular Médio", formula=f"=AVERAGE('Dados Moleculares'!C2:C{max_row_data})", number_format='#,##0.00')
create_card(ws_dash, start_col=8, start_row=5, title="LogP Médio", formula=f"=AVERAGE('Dados Moleculares'!D2:D{max_row_data})", number_format='#,##0.00')

# Tabela Resumo no Dashboard
ws_dash['B10'] = "Resumo dos Candidatos Aprovados"
ws_dash['B10'].font = Font(name="Segoe UI", size=12, bold=True, color="1B4332")

dash_headers = ["ID", "Peso Molecular", "LogP", "Status"]
for i, h in enumerate(dash_headers, 2):
    cell = ws_dash.cell(row=11, column=i, value=h)
    cell.fill = primary_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal='center')

for idx in range(len(df)):
    row_src = idx + 2
    row_dest = 12 + idx
    ws_dash.cell(row=row_dest, column=2, value=f"='Dados Moleculares'!A{row_src}").alignment = Alignment(horizontal='center')
    ws_dash.cell(row=row_dest, column=3, value=f"='Dados Moleculares'!C{row_src}").number_format = '#,##0.00'
    ws_dash.cell(row=row_dest, column=4, value=f"='Dados Moleculares'!D{row_src}").number_format = '#,##0.00'
    ws_dash.cell(row=row_dest, column=5, value=f"='Dados Moleculares'!G{row_src}").alignment = Alignment(horizontal='center')
    
    for c in range(2, 6):
        ws_dash.cell(row=row_dest, column=c).font = Font(name="Segoe UI", size=10)
        ws_dash.cell(row=row_dest, column=c).border = thin_border

# Adicionar Gráfico de Colunas no Dashboard
chart = BarChart()
chart.type = "col"
chart.style = 10
chart.title = "Comparativo de Peso Molecular por Candidato"
chart.y_axis.title = "Peso Molecular (g/mol)"
chart.x_axis.title = "ID do Composto"
chart.legend = None

data_ref = Reference(ws_dash, min_col=3, min_row=11, max_row=11 + len(df))
cats_ref = Reference(ws_dash, min_col=2, min_row=12, max_row=11 + len(df))

chart.add_data(data_ref, titles_from_data=True)
chart.set_categories(cats_ref)
chart.width = 14
chart.height = 7.5

ws_dash.add_chart(chart, "G10")

# Ajustar automaticamente a largura das colunas
for ws in [ws_dash, ws_data]:
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = openpyxl.utils.get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

# Salvar o arquivo na pasta outputs do projeto
excel_path = "outputs/dashboard_quimioinformatica.xlsx"
wb.save(excel_path)
print(f"[SUCESSO] Script executado! Dashboard criado em: {excel_path}")
