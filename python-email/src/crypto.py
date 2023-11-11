#Função para colocar senha no excel 

path_data = '../dados/dados_tratados.xlsx'
#Gerando uma senha
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
def crypto_excel(path_data):
    print('Criptografando o arquivo...')    
    # Abrindo o arquivo com a chave
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    # Criando o objeto fernet
    fernet = Fernet(key)
    # Abrindo o arquivo para criptografar
    with open(path_data, 'rb') as file:
        original = file.read()
    # Criptografando os dados
    encrypted = fernet.encrypt(original)
    # Abrindo o arquivo para escrever os dados criptografados
    change_file = path_data.replace('.xlsx', '_encrypted.xlsx')
    with open(change_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print('Arquivo criptografado com sucesso!')