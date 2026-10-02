# Pipeline Automatizado de Triagem Virtual em Quimioinformática

## Sobre o Projeto
Este projeto consiste num **pipeline computacional** desenvolvido em Python e executado em ambiente Linux (Ubuntu) para realizar a **triagem virtual** de compostos químicos. O principal objetivo é automatizar a busca por moléculas com potencial farmacológico, avaliando rapidamente se elas possuem características adequadas para se tornarem potenciais fármacos.

Em termos simples: o script pega um lote de moléculas, calcula suas propriedades físicas e químicas e aplica um "peneiramento inteligente" para separar apenas aquelas que têm boas chances de serem absorvidas pelo organismo humano.

---

## Arquitetura e Tecnologias
O pipeline foi estruturado seguindo boas práticas de engenharia de software e ciência de dados:
* **Linguagem:** Python 3 (com bibliotecas especializadas como `Pandas` para manipulação de tabelas e `RDKit` para química computacional).
* **Fonte de Dados:** API pública do PubChem (com um mecanismo de segurança/fallback para garantir estabilidade offline).
* **Controle de Versão:** Git.

A organização das pastas do repositório segue este padrão limpo:

quimioinformatica-pipeline/
│
├── data/                  # Dados brutos de entrada (SMILES e IDs)
├── outputs/               # Resultados processados e filtrados
├── scripts/               # Scripts de automação (download, triagem e relatório)
├── .ignorarnogit          # Arquivos ignorados pelo Git
└── README.md              # Documentação do projeto
A Lógica por Trás do Filtro: A Regra de Lipinski
​Para decidir quais compostos são aprovados, o script utiliza a famosa Regra de Lipinski (também conhecida como a Regra dos Cinco). Na indústria farmacêutica, essa regra serve para avaliar a "drug-likeness" (o perfil de semelhança com um fármaco) de uma molécula, prevendo se ela pode ser administrada por via oral de forma eficiente.
​O filtro avalia quatro critérios principais:
​Peso Molecular (Molecular_Weight \le 500 g/mol): Moléculas muito grandes têm dificuldade de atravessar as membranas celulares. O limite garante que o composto seja pequeno o suficiente para circular bem pelo corpo.
​Lipofilicidade (LogP \le 5): Mede o quanto a molécula gosta de gordura em relação à água. Um valor equilibrado garante que ela consiga atravessar as paredes celulares de gordura sem ficar "presa" nelas.
​Doadores de Hidrogênio (H_Donors \le 5): Conta grupos como hidroxilas ou aminas. Limitar esse número evita que a molécula tenha dificuldades para passar pelas barreiras biológicas.
​Aceitadores de Hidrogênio (H_Acceptors \le 10): Conta átomos como oxigênio e nitrogênio que fazem ligações de hidrogênio. Controlar essa quantidade garante uma boa solubilidade e interação com os alvos biológicos.
