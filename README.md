# Pipeline Automatizado de Triagem Virtual em Quimioinformática

## Sobre o Projeto
Este projeto consiste em um **pipeline computacional** desenvolvido em Python para realizar a triagem virtual de moléculas utilizando a **Regra de Lipinski** (Regra dos Cinco) para avaliação de *drug-likeness*. 

O sistema processa compostos, calcula propriedades físico-químicas essenciais (peso molecular, lipofilicidade, doadores e aceitadores de hidrogênio) e gera relatórios automáticos em PDF juntamente com um dashboard interativo em Excel (`.xlsx`).

## Arquitetura e Tecnologias
O pipeline foi estruturado seguindo boas práticas de engenharia de dados:
- **Linguagem:** Python 3 (utilizando `Pandas` para manipulação de dados e `RDKit` para química computacional).
- **Relatórios:** Automação de planilhas formatadas com `OpenPyXL` e relatórios executivos.
- **Controle de Versão:** Git e GitHub.

## Organização do Repositório
- `data/` : Dados brutos de entrada (arquivos SMILES e identificadores)
- `outputs/` : Resultados processados, relatórios PDF e dashboard em Excel
- `scripts/` : Scripts de automação (triagem, relatórios e geração da planilha)
- `.ignorarnogit` : Configuração de arquivos ignorados pelo Git
- `requisitos.txt` : Dependências e bibliotecas do projeto
- `README.md` : Documentação detalhada do projeto

## A Lógica por Trás do Filtro: A Regra de Lipinski
Para aprovar os compostos, o script avalia quatro critérios de absorção oral:
- **Peso Molecular (Molecular Weight $\le$ 500 g/mol):** Garante facilidade de permeação pelas membranas celulares.
- **Lipofilicidade (LogP $\le$ 5):** Mede o coeficiente de partição óleo/água.
- **Doadores de Hidrogênio (H_Donors $\le$ 5):** Contagem de grupos hidroxila e amina.
- **Aceitadores de Hidrogênio (H_Acceptors $\le$ 10):** Contagem de átomos de oxigênio e nitrogênio.

---

## Como Instalar e Configurar

1. Clone o repositório e acesse a pasta:
   bash
   git clone [https://github.com/ingridlohana359-rgb/Analises-quimioinformatica.git](https://github.com/ingridlohana359-rgb/Analises-quimioinformatica.git)
   cd Analises-quimioinformatica

