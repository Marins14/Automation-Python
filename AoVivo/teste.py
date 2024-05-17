# import calendar 
# year=2023
# month=10
# x=calendar.month(year,month)
# print(x)
import time
from datetime import datetime

agora= datetime.now()
formato="%d/%m/%Y %H:%M:%S"
data_formatada=agora.strftime(formato)

def soma(a,b):
    resultado = a+b
    return resultado
def divisao(a,b):
    resultado = a/b
    return resultado

class calculadora:
    print("Bem vindo a calculadora! ")
    print(f'Você está realizando esta operação: {data_formatada} ')
    time.sleep(1)
    c=int(input("Escolha sua operação: 1 - Soma 2 - Divisao: "))
    match c:
        case 1:
            x=int(input("Digite os valores: 1: "))
            y=int(input("Digite os valores: 2: "))
            print(f'O Resultado da soma é: {soma(x,y)}')
        case 2: 
            x=int(input("Digite os valores: 1: "))
            y=int(input("Digite os valores: 2: "))
            print(f'O Resultado da divisão é: {divisao(x,y):.2f}')
