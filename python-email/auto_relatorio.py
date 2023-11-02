###########################################################
#   Automatizar o tratamento e envio do relatorio         #
###########################################################
# Autor: Matheus Marins                                   #
# Data: 01/11/2023                                        #
# Versao: 1.0                                             #
########################################################### 


# Importando as bibliotecas
from email.mime.application import MIMEApplication
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import pandas as pd
#from email.mime.base import MIMEBase

# Carregando variáveis de ambiente
# Devido ao git não subir o .env é necessário criar um arquivo .env na pasta Env e colocar as variáveis de ambiente conforme exemplo
from dotenv import load_dotenv
load_dotenv('./Env/.env')

# Função para tratamento dos dados
# OBS: Este tratameneto é totalmente dependente da exportação vinda do banco de dados
def tratamento_dados():
    # Mensagem de tratamento
    print('Tratando os dados...')
    # Tratamento dos dados, caso erro ele informa ao usuário qual o erro
    try:
        df = pd.read_excel('./dados/dados.xlsx')
        #print(df.head()) #Caso necessário para verificar as tabelas
        #Separando as colunas pela virgula
        df[['1', '2','3','4','5']] = df['OPA'].str.split(',', n=4, expand=True) #n=1 é o número de vezes que a coluna será separada, n é sempre n-1 em relação a tabela
        #Removendo a coluna OPA, já foi tratada e não é mais necessária
        df.drop(columns=['OPA'], inplace=True)
        # Definindo o novo arquivo
        df.to_excel('./dados/dados_tratados.xlsx')
        print('Dados tratados com sucesso!')
    except FileNotFoundError:
        print('ERRO: Arquivo não encontrado!')
    except Exception as e:
        print('Erro durante o tratamento dos dados: ', e)

# Definindo as variáveis
# Toda documentação do MIME -> https://docs.python.org/3/library/email.mime.html
email = os.getenv('email') # E-mail que será usado para envio
senha = os.getenv('senha') #Caso use o Gmail, é necessário gerar uma senha de aplicativo, caso use o Outlook, é a senha normal
destinatarios = os.getenv('destinatario') #Caso seja mais de um destinatário, usar o formato 'email1, email2'
copia = os.getenv('copia') #Caso seja necessário colocar alguém em cópia, respeitando o formato 'email1, email2'
conteudo = f'Bom dia! \n\n Segue em anexo o relatório das linhas de controle. \n\n Atenciosamente, \n Matheus Marins Bernardello \n\n Este e-mail foi enviado automaticamente. Em caso de dúvidas favor me acionar via teams.' #Corpo do e-mail
# Função para envio do e-mail
def envio_email():
    #Mensagem de envio
    print('Enviando e-mail...')
    # Tenta o envio do e-mail caso retorne erro, informa ao usuario qual o erro
    try:
        # Preparando o e-mail
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = ', '.join(destinatarios.split(','))
        msg['Cc'] = ', '.join(copia.split(',')) if copia else ''
        msg['Subject'] = 'Relatório das Linhas Controle'
        # Adicionando corpo ao e-mail
        msg.attach(MIMEText(conteudo, 'plain'))
        #Adicionar a planilha tratado ao e-mail
        Path_dados= './dados/dados_tratados.xlsx'
        #with garante que o arquivo será fechado ao final da execução
        with open(Path_dados, 'rb') as arquivo:
            part = MIMEApplication(arquivo.read(), Name=os.path.basename(Path_dados))
        # Cabeçalho do anexo
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(Path_dados)}"'
        msg.attach(part)
        # Configurando o servidor SMTP do Gmail
        smtp = smtplib.SMTP(host='smtp.office365.com', port=587) #Caso use o GMAIL o host é 'smtp.gmail.com' e Porta 587
        smtp.starttls()
        # Iniciando o login
        smtp.login(email, senha)
        # Enviando o e-mail
        smtp.sendmail(email, destinatarios.split(',') + copia.split(','), msg.as_string())
        # Fechando a conexão
        smtp.quit()
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('Erro durante o envio do e-mail: ',e)

# Função para conexão com o banco de dados
# def banco():
#     conn = sqlite3.connect('banco.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         Seu código SQL
#     ''')
#     conn.close()

if __name__ == '__main__':
    #banco()
    tratamento_dados()
    #envio_email()