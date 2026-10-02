import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def gerar_relatorio_pdf():
    pdf_path = "outputs/relatorio_candidatos_lipinski.pdf"
    csv_path = "outputs/candidatos_filtrados.csv"
    
    # Ler os dados gerados pela triagem
    df = pd.read_csv(csv_path)
    
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []
    
    # Estilos profissionais
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#1b4332'),
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#555555'),
        spaceAfter=15
    )
    text_style = ParagraphStyle(
        'TextStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#333333'),
        spaceAfter=10,
        leading=12
    )
    
    # Cabeçalho
    story.append(Paragraph("Relatório de Triagem Virtual: Regra de Lipinski", title_style))
    story.append(Paragraph("Análise de propriedades físico-químicas para descoberta de fármacos (Foco Educacional e Portfólio)", subtitle_style))
    
    # Texto descritivo didático
    intro_texto = (
        "<b>O que é este relatório?</b> Este documento apresenta os resultados de uma triagem computacional "
        "baseada na Regra de Lipinski. O objetivo é selecionar moléculas que possuem perfil adequado para "
        "absorção oral no corpo humano.<br/><br/>"
        "<b>Glossário Rápido para Entender os Dados:</b><br/>"
        "• <b>ID / Molécula:</b> Identificação do composto testado.<br/>"
        "• <b>Estrutura SMILES:</b> É a representação em texto da estrutura química da molécula (como o computador 'vê' os átomos e ligações).<br/>"
        "• <b>Peso Molecular (g/mol):</b> Deve ser menor que 500 para garantir que a molécula seja pequena o suficiente para circular bem.<br/>"
        "• <b>LogP (Lipofilicidade):</b> Mede o quanto a molécula gosta de gordura vs. água. Valores abaixo de 5 indicam que ela atravessa bem as membranas celulares.<br/>"
        "• <b>Doadores / Aceitadores de H:</b> Contagem de átomos polares que fazem ligações de hidrogênio (essenciais para interagir com o alvo sem bloquear a absorção)."
    )
    story.append(Paragraph(intro_texto, text_style))
    story.append(Spacer(1, 10))
    
    # Limpar e renomear as colunas do DataFrame para ficar limpo em Português
    # Vamos manter apenas as colunas essenciais e bonitas
    colunas_desejadas = ['ID', 'smiles', 'Molecular_Weight', 'LogP', 'H_Donors', 'H_Acceptors']
    df_limpo = df[[c for c in colunas_desejadas if c in df.columns]].copy()
    
    # Renomear colunas para termos amigáveis
    df_limpo.columns = ['ID', 'Estrutura SMILES', 'Peso Molecular', 'LogP', 'Doadores H', 'Aceitadores H']
    
    # Arredondar valores numéricos para 2 casas decimais para não poluir a tabela
    for col in ['Peso Molecular', 'LogP']:
        if col in df_limpo.columns:
            df_limpo[col] = pd.to_numeric(df_limpo[col]).round(2)

    # Montar a tabela para o PDF
    data = [list(df_limpo.columns)]
    for _, row in df_limpo.iterrows():
        data.append([str(val) for val in row.values])
        
    tabela = Table(data, colWidths=[70, 160, 75, 55, 65, 65])
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2d6a4f')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f8f9fa')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dee2e6')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8),
    ]))
    
    story.append(tabela)
    
    doc.build(story)
    print("[SUCESSO] Relatório PDF didático gerado com sucesso!")

if __name__ == '__main__':
    gerar_relatorio_pdf()
