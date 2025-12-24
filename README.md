#  Sistema de Triagem de Pacientes (Fila Prioritária em Python)

##  Descrição do Projeto

Este projeto é uma aplicação de console desenvolvida em **Python** com o objetivo de simular um sistema de triagem hospitalar com classificação de risco. O foco principal é a aplicação prática de estruturas de dados avançadas, especificamente a **Fila Prioritária (Priority Queue)**, para garantir que pacientes em estado mais grave (maior prioridade) sejam atendidos antes.

O sistema coleta dados detalhados do paciente e do caso clínico, atribui uma classificação de risco (de 1 a 5, onde 1 é o mais grave) e gerencia a fila de atendimento de forma eficiente, utilizando o algoritmo de **Heap Mínimo** (`heapq` do Python).

##  Funcionalidades

O programa oferece um menu interativo com as seguintes opções:

| Opção | Funcionalidade | Descrição |
| :--- | :--- | :--- |
| **1** | **Adicionar novo paciente** | Coleta dados do paciente e do caso, atribui a classificação de risco e insere na fila prioritária. |
| **2** | **Atender próximo paciente** | Remove o paciente com a maior prioridade (menor número de risco) da fila para atendimento. |
| **3** | **Visualizar fila** | Exibe a lista de pacientes na fila, ordenada por prioridade. |
| **4** | **Sair** | Encerramento do sistema. |

##  Tecnologias e Conceitos Aplicados

O projeto é uma excelente demonstração de conceitos de **Análise e Projeto de Algoritmos** e **Estruturas de Dados**:

| Categoria | Tecnologia/Conceito | Descrição |
| :--- | :--- | :--- |
| **Linguagem** | **Python** | Linguagem principal de desenvolvimento, escolhida pela legibilidade e facilidade de prototipagem. |
| **Estrutura de Dados** | **Fila Prioritária (Heapq)** | Implementação eficiente da fila prioritária utilizando o módulo `heapq` (heap binário). |
| **Classes** | **`Paciente` e `Caso`** | Modularização do código para encapsular dados de identificação e detalhes clínicos. |
| **Complexidade** | **Análise Big O** | O projeto inclui uma análise da complexidade de tempo das operações de inserção e remoção, ambas com complexidade **O(log n)**. |

##  Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina (versão 3.6 ou superior).

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Execução da Aplicação

O projeto é executado diretamente pelo arquivo principal.

```bash
python main.py
```

### 3. Interação

Após a execução, o sistema apresentará um menu de opções no console para que você possa interagir, adicionando pacientes e simulando o atendimento.

##  Estrutura do Projeto

O projeto é modularizado em três arquivos principais, refletindo a separação de responsabilidades:

```
seu-repositorio/
├── main.py                   # Lógica principal, menu de interação e orquestração das classes.
├── paciente.py               # Classe Paciente (nome, cpf, telefone, endereco, classificacao_risco).
├── caso.py                   # Classe Caso (sintomas, febre, cortes, ulceras).
├── fila_prioritaria.py       # Classe FilaPrioritaria (implementação do heap).
└── README.md                 # Este arquivo.
```

##  Contribuição

Este projeto é um exercício acadêmico e não está aberto a contribuições externas. No entanto, sinta-se à vontade para fazer um *fork* e adaptá-lo para seus próprios estudos.

##  Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

**Desenvolvido por:** João Pedro `@Jao2k25`
