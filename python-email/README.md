# Automatização de relatórios

## Pré-requisitos
- Certifique-se que possue os módulos abaixo instalados, caso não instale com os comandos abaixo:
```python
pip install pandas
pip install openpyxl
pip install python-dotenv
```

## Como usar
- Crie um arquivo .env com as variáveis de ambiente
- Execute o arquivo auto_relatorio.py com ```python auto_relatorio.py```
- O arquivo .xlsx será gerado na pasta dados

## OBS: Lembrando que é necessário configurar o banco de dados de acordo com o seu ambiente
- Exemplo de .env está na pasta Env
- Exemplo de .xlsx está na pasta dados
- Ajustar a função trata_dados() de acordo com o arquivo exportado pelo banco de dados

## Autor
- [Matheus Marins Bernardello](mailto:matheus.bernardello@live.com)