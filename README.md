Este projeto mostra como criar, listar, atualizar e excluir produtos em um banco MS SQL usando Python.  

O objetivo é demonstrar que sei **organizar um CRUD completo**, mesmo com algumas limitações do banco de teste.

## Scripts

- **listar_produtos.py**: Lista produtos filtrando pelo nome.
- **criar_produto.py**: Cria novos produtos.
- **atualizar_produto.py**: Atualiza produtos existentes. Depende da SP `SpUpdateProduto`, que não existe no banco de teste.
- **excluir_produto.py**: Exclui produtos pelo código.

## Requisitos

- Python 3.x
- Bibliotecas: `pyodbc`, `prettytable`
- Acesso ao banco de dados fornecido (usuário, senha, host, porta)

## Como usar

1. Instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
Rode o script que quiser no terminal:

bash
Copiar código
python listar_produtos.py
python criar_produto.py
python atualizar_produto.py
python excluir_produto.py
Observação: os scripts foram escritos para serem claros e diretos, mostrando que o CRUD funciona. A atualização depende da SP que não existe no banco de teste.