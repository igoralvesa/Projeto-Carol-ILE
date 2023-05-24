import os
from funcao import menu
from funcao import tabela_categoria
from funcao import tabela_categoria_ler

dic = {1: "CASA", 2: "COMIDA", 3: "TRANSPORTE", 4: "USOPESSOAL"}
while True:
    try:
        valores = [1, 2]
        decisao = int(input("você deseja entrar no menu? [1 - SIM, 2 - NÃO] "))
        if decisao in valores:
            break
        else:
            print("VALOR INVÁLIDO! as opções são 1 ou 2")
    except ValueError:
        print("LETRAS NÃO SÃO ACEITAS! informe um valor válido")
 


def adicionar():
    arquivo = open("dados.csv", "a")
    nome = input("Com o que você gastou? ::: ").capitalize()
    while True:
        try:
         valor = float(input("Quanto custou? "))
         break
        except KeyError:
            print("informe um valor válido.")
        except ValueError:
            print("informe um valor válido")
    tabela_categoria()
    
    while True:
        try:
         valores = [1, 2, 3, 4]
         escolha_categoria = int(input("O gasto se encaixa em qual categoria? "))
         if escolha_categoria in valores:
             break
         else:
             print("VALOR INVÁLIDO! as opções são de 1 a 4")
         
        except ValueError:
            print("LETRAS NÃO SÃO ACEITAS! informe um valor válido")
    arquivo.write(f"{nome}\t{valor}R$ ----- {dic[escolha_categoria]}\n")
    arquivo.close()


def ler():

    tabela_categoria_ler()
    while True:
        try:
         valores = [1,2,3,4,5]
         escolha_ler = int(input("Digite a categoria que você deseja ver os gastos: "))
         if escolha_ler in valores:
             break
         else:
             print("VALOR INVÁLIDO! as opções são de 1 a 5")
        except ValueError:
            print("LETRAS NÃO SÃO ACEITAS! informe um valor válido")
    if escolha_ler == 5:
        print("Gastos totais:\n")
        for i in range(1, 5):
            arquivo = open("dados.csv", "r")
            for linha in arquivo:
                if dic[i] in linha:
                    print(linha.replace("-----", ""), end="")
            arquivo.close()
    else:
        arquivo = open("dados.csv", "r")
        print(f"\nGastos com {dic[escolha_ler]}:\n")
        for linha in arquivo:
            if dic[escolha_ler] in linha:
                print(linha[:linha.find('-----')])
        arquivo.close()
    print()


def atualizar():
    return 0


def deletar():
    while True:
        with open("dados.csv", 'r') as f:
            linhas = f.readlines()
        f.close()

        arquivo = open("dados.csv", "r")
        transacoes = []
        print()
        for i in arquivo:
            exc = i.find(next(filter(str.isdigit, i)), 0)
            print(f"{i[:exc]}")
            transacoes.append(i[:exc].replace("\t", ""))
        arquivo.close()

        excluir = input(f"\nQual transação você deseja deletar?? ").capitalize()

        if excluir in transacoes:
            arquivo = open("dados.csv", "w")
            for linha in linhas:
                if excluir not in linha:
                    arquivo.write(linha)
            print("DELETADO!")
            arquivo.close()
            break

        else:
            print("Digite uma transação válida! ", "\n")


while decisao == 1:
    menu()
    while True:
        try:
            valores = [1,2,3,4,5]
            pergunta = int(input("O que você deseja realizar? "))
            os.system('cls')
            if pergunta in valores:
                break
            else:
                print("VALOR INVÁLIDO! as opções são de 1 a 5")
                menu()
        except KeyError:
            print("informe um valor válido.")
        except ValueError:
            print("Informe um valor válido.")
    if pergunta == 1:
        adicionar()

    elif pergunta == 2:
        ler()

    elif pergunta == 3:
        atualizar()

    elif pergunta == 4:
        deletar()

    
    else:
        break

    print("retornando ao menu.....")
