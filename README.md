# Projeto Interpretador Lox Simples

## Integrantes
- Amanda Abreu - Matrícula: 211030925 - Turma: T03
- Arthur Rodrigues -  Matrícula: 211030291 - Turma: T03

## Introdução
Este projeto consiste no desenvolvimento de um interpretador para uma linguagem de programação simples inspirada na linguagem Lox, utilizada na disciplina de compiladores. O interpretador implementa análise léxica, análise sintática, interpretação e análise semântica básicas. O sistema implementa a validação de tokens especificos, como: 
  - CPF
  - CNPJ
  - E-mail
  - Celular
  - Data

O interpretador é escrito em Python e utiliza técnicas clássicas de compiladores, como análise top-down recursiva para parsing e uma árvore de sintaxe abstrata (AST) para representar o código.


## Regras de Validação

A linguagem permite que o usuário escreva comandos com dados, e o interpretador verifica **se esses dados são válidos** de acordo com regras semânticas específicas. Exemplos:

- Verifica se um **CPF** ou **CNPJ** está corretamente formatado e possui dígitos válidos.
- Valida se um **e-mail** é bem formado.
- Confirma se um número de **celular** segue o padrão brasileiro.
- Checa se uma **data** é válida no calendário.

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/fcte-compiladores/trabalho-final-trabalho-final-compialdores.git
   cd trabalho-final-trabalho-final-compialdores

2. Certifique-se de ter o python3 instalado
3. Instale as dependências:
   ```bash
   pip install lark
4. Execute o modo interativo:
   ```bash
   python3 main.py
5. Execute o modo com Parser: 
   ```bash
   python3 interpretador.py

## Referências
### **Documentação oficial do Python (3.8+)**
  Utilizada como referência principal para estruturação do código, manipulação de strings, uso de expressões regulares com o módulo re, e criação da interface de linha de comando (CLI). Ajudou também na compreensão e uso de funções, condicionais e manipulação de listas.

### **Documentação oficial do Lark (https://github.com/lark-parser/lark)**
  Utilizada como base principal para criação da gramática .lark, construção do parser e uso da classe Transformer para interpretar os dados estruturados. Ajudou na definição das regras léxicas e sintáticas da linguagem de validação.

### **Validação de CPF e CNPJ**
  A lógica de validação foi baseada nas regras oficiais de formação dos dígitos verificadores, com apoio de artigos técnicos e exemplos disponíveis em fóruns como Stack Overflow. A implementação final do algoritmo foi feita manualmente, com ajustes próprios para integrá-los ao interpretador e ao sistema de mensagens.

### **Material de aula da disciplina de Compiladores**
  Utilizados como base conceitual para definição das etapas de análise léxica, sintática e semântica. A estrutura do projeto seguiu a proposta didática apresentada durante o curso.
