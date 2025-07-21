# Projeto Interpretador Lox Simples

## Integrantes
- Amanda Abreu - Matrícula: 211030925
- Arthur Rodrigues -  Matrícula:

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
