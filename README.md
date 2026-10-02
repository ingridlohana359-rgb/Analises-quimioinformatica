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

## A Lógica por Trás do Filtro: A Regra de Lipinski
Para decidir quais compostos são aprovados, o script utiliza a famosa Regra de Lipinski (também conhecida como a Regra dos Cinco). Na indústria farmacêutica, essa regra avalia o perfil de *drug-likeness* (viabilidade como fármaco).
O filtro avalia quatro critérios principais:
- **Peso Molecular (Molecular_Weight $\le$ 500 g/mol):** Moléculas muito grandes têm dificuldade de atravessar as membranas celulares. O limite garante que o composto mantenha propriedades farmacocinéticas adequadas.
- **Lipofilicidade (LogP $\le$ 5):** Mede o quanto a molécula gosta de gordura em relação à água. Um valor equilibrado garante que ela consiga atravessar as paredes celulares lipídicas.
- **Doadores de Hidrogênio (H_Donors $\le$ 5):** Conta grupos como hidroxilas ou aminas. Limitar esse número evita que a molécula tenha dificuldades para passar pelas barreiras biológicas.
- **Aceitadores de Hidrogênio (H_Acceptors $\le$ 10):** Conta átomos como oxigênio e nitrogênio que fazem ligações de hidrogênio. Controlar essa quantidade garante uma boa solubilidade e interação com os alvos biológicos.
-
