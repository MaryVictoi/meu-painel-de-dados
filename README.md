<!-- BANNER DO PROJETO -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,10,24,30&height=220&section=header&text=Meu%20Painel%20de%20Dados&fontSize=48&fontAlignY=36&desc=An%C3%A1lise%20L%C3%B3gica%20e%20Processamento%20de%20Vetores%20em%20Python&descAlignY=60&descSize=16" width="100%" alt="Banner do Projeto" />
</p>

<!-- BADGES / DISTINTIVOS -->
<p align="center">
  <a href="#-tecnologias-e-conceitos">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  </a>
  <a href="#-sobre-o-projeto">
    <img src="https://img.shields.io/badge/Instituição-ETEC_Rubens_de_Faria_e_Souza-red?style=for-the-badge" alt="ETEC Badge" />
  </a>
  <a href="#-licença">
    <img src="https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge" alt="MIT License Badge" />
  </a>
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status Badge" />
</p>

---

## 📑 Sumário
- [Sobre o Projeto](#-sobre-o-projeto)
- [Tecnologias e Conceitos](#-tecnologias-e-conceitos)
- [Arquitetura do Algoritmo](#-arquitetura-do-algoritmo)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Como Executar](#-como-executar)
- [Exemplo de Saída](#-exemplo-de-saída)
- [Autora e Créditos](#-autora-e-créditos)
- [Licença](#-licença)

---

## 📌 Sobre o Projeto

O **Meu Painel de Dados** é uma aplicação em Python desenvolvida para demonstrar o gerenciamento eficiente de rotinas pessoais através de vetores dinâmicos (listas).

O projeto foi elaborado como requisito de avaliação prática na disciplina de **Desenvolvimento de Sistemas I** do curso Técnico em Desenvolvimento de Sistemas na **ETEC Rubens de Faria e Souza** (Sorocaba - SP).

> [!NOTE]
> **Objetivo Acadêmico:** Validar o uso de estruturas de repetição, vetores dinâmicos via `.append()`, manipulação de tipos de dados (`str`, `int`) e tomada de decisão fundamentada no comprimento da lista (`len()`).

---

## 🛠️ Tecnologias e Conceitos

* **Linguagem:** [Python 3.x](https://www.python.org/)
* **Estrutura de Dados:** Listas / Vetores Dinâmicos
* **Controlo de Fluxo:** Laços `for` e Estruturas Condicionais `if / elif / else`
* **Entrada e Saída:** Funções `input()`, `print()` e formatação de strings (`f-strings`)

---

## ⚙️ Arquitetura do Algoritmo

O programa segue um fluxo sequencial de 4 fases bem definidas:

| Fase | Ação | Função / Método | Descrição Lógica |
| :--- | :--- | :--- | :--- |
| **1. Coleta** | Entrada de Dados | `input()`, `int()` | Coleta o nome, cidade e converte a quantidade de tarefas para número inteiro. |
| **2. Cadastro** | Povoamento | `.append()` + `for` | Adiciona dinamicamente cada tarefa especificada pelo utilizador ao final da lista. |
| **3. Leitura** | Varredura da Lista | `for t in tarefas` | Iteração elemento a elemento para exibição formatada dos itens cadastrados. |
| **4. Decisão** | Avaliação do Volume | `len(tarefas)` | Aplica regras de negócio para gerar um diagnóstico personalizado da rotina. |

### Regras de Negócio (Diagnóstico de Rotina)
- **`len(tarefas) == 0`**: Exibe *"Nenhuma tarefa cadastrada."*
- **`len(tarefas) <= 3`**: Exibe *"[Nome] de [Cidade]: rotina leve hoje!"*
- **`else` (`> 3`)**: Exibe *"[Nome] de [Cidade]: rotina cheia! Organize prioridades."*

---

## 🎨 Apresentação do Projeto

<p align="center">
  <a href="[https://canva.link/vj5erxl6t566k49](https://canva.link/vj5erxl6t566k49)" target="_blank">
    <img src="[https://img.shields.io/badge/Apresentação_no_Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white](https://img.shields.io/badge/Apresentação_no_Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white)" alt="Link da Apresentação no Canva" />
  </a>
</p>

---

## 📂 Estrutura do Repositório

```text
meu-painel-de-dados/
├── main.py          # Código-fonte principal em Python
├── README.md        # Documentação completa do projeto
└── .gitignore       # Arquivos a serem ignorados pelo Git
