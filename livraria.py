import mysql.connector
from prettytable import PrettyTable
import datetime



from prettytable import from_csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Fernandinho123",
    database="livraria",
)

mycursor = mydb.cursor()


def cadastrar_livro(nome_livro, autor_livro, editora_livro, preco, livro_estoque):
    sql = "INSERT INTO livro(nome_livro, autor_livro,editora_livro,preco,livro_estoque)VALUES(%s,%s,%s,%s,%s)"
    valores = (nome_livro, autor_livro, editora_livro, preco, livro_estoque)
    mycursor.execute(sql, valores)

    mydb.commit()


def cria_tabela():
    # Cria a tabela
    x = PrettyTable(["Id", "Livro", "Autor", "Editora", "Preço", "Estoque"])

    # Alinha as colunas
    x.align["Id"] = "l"
    x.align["Livro"] = "l"
    x.align["Autor"] = "l"
    x.align["Editora"] = "r"
    x.align["Preço"] = "r"
    x.align["Estoque"] = "r"

    # Deixa um espaço entre a borda das colunas e o conteúdo (default)
    x.padding_width = 1

    return x

def cria_tabelaUser():
    # Cria a tabela
    x = PrettyTable(["Id", "Nome", "Senha", "Staff"])

    # Alinha as colunas
    x.align["Id"] = "l"
    x.align["Nome"] = "l"
    x.align["Senha"] = "l"
    x.align["Staff"] = "r"


    # Deixa um espaço entre a borda das colunas e o conteúdo (default)
    x.padding_width = 1

    return x

def mostrar_tudo():
    sql = ("SELECT * FROM livro ORDER BY nome_livro")
    mycursor.execute(sql)
    resultado = mycursor.fetchall()
    x = cria_tabela()

    for y in resultado:
        x.add_row([f"{y[0]}", f"{y[1].title()}", f"{y[2].title()}", f"{y[3].title()}", f"{y[4]}", f"{y[5]}"])

    print(x)


def consultar_livro(palavra):
    sql = (f"SELECT * FROM livro  WHERE nome_livro LIKE '%{palavra}%' ORDER BY nome_livro ")
    mycursor.execute(sql)

    resultado = mycursor.fetchall()
    x = cria_tabela()

    for y in resultado:
        x.add_row([f"{y[0]}", f"{y[1].title()}", f"{y[2].title()}", f"{y[3].title()}", f"{y[4]}", f"{y[5]}"])

    print(x)


def consultar_user(palavra):
    sql = (f"SELECT * FROM usuario  WHERE nome LIKE '%{palavra}%' ORDER BY nome ")
    mycursor.execute(sql)

    resultado = mycursor.fetchall()
    x = cria_tabelaUser()

    for y in resultado:
        x.add_row([f"{y[0]}", f"{y[1].title()}", f"{y[2]}", f"{y[3]}"])

    print(x)
def tudos_user():
    sql = ("SELECT * FROM usuario ORDER BY nome")

    mycursor.execute(sql)

    resultado = mycursor.fetchall()
    x = cria_tabelaUser()

    for y in resultado:
        x.add_row([f"{y[0]}", f"{y[1].title()}", f"{y[2]}", f"{y[3]}"])

    print(x)
def consultar_autor(palavra):
    sql = (f"SELECT * FROM livro  WHERE autor_livro LIKE '%{palavra}%' ")
    mycursor.execute(sql)

    resultado = mycursor.fetchall()
    x = cria_tabela()

    for y in resultado:
        x.add_row([f"{y[0]}", f"{y[1].title()}", f"{y[2].title()}", f"{y[3].title()}", f"{y[4]}", f"{y[5]}"])

    print(x)


def consultar_editora(palavra):
    sql = (f"SELECT * FROM livro  WHERE editora_livro LIKE '%{palavra}%' ")
    mycursor.execute(sql)

    resultado = mycursor.fetchall()
    x = cria_tabela()

    for y in resultado:
        x.add_row([f"{y[0]}", f"{y[1].title()}", f"{y[2].title()}", f"{y[3].title()}", f"{y[4]}", f"{y[5]}"])

    print(x)


def puxar_menor_preco():
    sql = (f"SELECT * FROM livro  ORDER BY preco")
    mycursor.execute(sql)

    resultado = mycursor.fetchall()
    x = cria_tabela()

    for y in resultado:
        x.add_row([f"{y[0]}", f"{y[1].title()}", f"{y[2].title()}", f"{y[3].title()}", f"{y[4]}", f"{y[5]}"])

    print(x)


def delete_book(id):
    sql = f"DELETE FROM livro where id_livro = {id}"
    mycursor.execute(sql)
    mydb.commit()


def delete_user(id):
    sql = f"DELETE FROM usuario where user_id = {id}"
    mycursor.execute(sql)
    mydb.commit()


def register_staff(nome, senha, staff):
    sql = f"SELECT COUNT(nome)FROM usuario WHERE nome ='{nome}'"
    mycursor.execute(sql)
    resultado = mycursor.fetchall()
    if resultado[0][0] != 0:

        return False
    else:

        sql = "INSERT INTO usuario(nome,senha,staff)VALUES(%s,%s,%s)"
        valores = (nome, senha, staff)
        mycursor.execute(sql, valores)

        mydb.commit()
        return True


def register(nome, senha):
    sql = f"SELECT COUNT(nome)FROM usuario WHERE nome ='{nome}'"
    mycursor.execute(sql)
    resultado = mycursor.fetchall()
    if resultado[0][0] != 0:
        return False
    else:
        staff = 0
        sql = "INSERT INTO usuario(nome,senha,staff)VALUES(%s,%s,%s)"
        valores = (nome, senha, staff)
        mycursor.execute(sql, valores)

        mydb.commit()
        return True


def login(nome, senha):
    sql = f"SELECT * FROM usuario WHERE senha ={senha} AND nome ='{nome}'"

    mycursor.execute(sql)

    resultado = mycursor.fetchall()

    dados = [resultado[0][1], resultado[0][3]]

    return dados


def verifica_string(palavra):
    try:
        pal = int(palavra)
        return False
    except:
        return True


def verifica_int(palavra):
    try:
        pal = int(palavra)
        return True
    except:
        return False


def boas_vindas():
    print("Bem vindo ao Sistema da Biblioteca!")
    print("Use os comandos abaixo para interagir no sistema:")

def op1():
    print("Bem vindo ao Sistema da Biblioteca!")
    print("Use os comandos abaixo para interagir no sistema:")
    print("1| Opções de staff gerenciar biblioteca")
    print("2| Opções comuns de consulta")
    print("3| Gerenciar users")
    print("4| Voltar ao login")

def opcao_staf():
    print("Use os comandos abaixo para interagir no sistema:")
    print("1| Cadastrar Livro")
    print("2| Deletar Livro")


def consulta():
    print("1| Mostrar tudo")
    print("2| Consultar por nome de  Livro")


def col():
    print("0| voltar")
    print("1| Mostrar tudo")
    print("2| Consultar por nome de  Livro")
    print("3| Consultar por autor")
    print("4| conultar por editora")
    print("5| Menor preço")

    op = input()

    if op == '0':
        pass
    elif op =='1':
        mostrar_tudo()
        acao = input("0| voltar")
        if acao == '0':
            pass
    elif op =='2':
        nome = input("digite o tirulo do livro:")
        consultar_livro(nome)
        op = input("0| para voltar ")
        if op == '0':
            pass
    elif op =='3':
        nome = input("digite o nome do autor:")
        consultar_autor(nome)
        op = input("0| para voltar ")
        if op == '0':
            pass
    elif op =='4':
        nome = input("digite o nome da editora:")
        consultar_editora(nome)
        op = input("0| para voltar ")
        if op == '0':
            pass
    elif op =='5':
        puxar_menor_preco()
        op = input("0| para voltar ")
        if op == '0':
            pass
"""
    inicio do programa
"""

libera_senha = False
libera_senh = False
libera_login = False
opcao = False
opcao_menu = False
opca = False
menu_staf = False
boas_vindas()
while True:
    print("Você Ja tem registro?")
    op = int(input("1| Sim   2| Não\n"))
    # a pessoa ja tem login
    if op == 1:

        # verifica se o login corresponde ao esperado
        while libera_login is not True:
            logins = (input("Digite seu login:"))
            libera_login = verifica_string(logins)
        # verifica se a senha corresponde ao esperado

        while libera_senha is not True:
            senha = (input("Digite seu senha:"))
            libera_senha = verifica_int(senha)
        # efetua login
        dados = login(logins, senha)
        with open('loginLOgs.txt','a') as log:
            x = datetime.datetime.now()
        
            log.write(f'o usuario {logins} logou as {x} \n')
        # verifica se o usuario e admnistrador
        if dados[1] == 1:
            # apresenta as alternativas
            while True:
                op1()


                op = int(input(":"))

                # 1| Opções de staff gerenciar biblioteca
                if op == 1:
                    opcao_staf()
                    op = int(input(":"))
                    # cadastrar livro
                    if op == 1:

                        print("Titulo do livro:")
                        nome = str(input())
                        print("Nome do autor:")
                        autor = str(input())

                        print("Nome da editora:")
                        editora = str(input())
                        print("preço:")
                        preco = float(input())
                        print("estoque")
                        estoque = str(input())

                        cadastrar_livro(nome,autor,editora,preco,estoque)
                        print(f"livro '{nome}' cadastrado com sucesso!")
                        print("##############")
                    # deletar livro
                    elif op == 2:
                        print("Para deletar um livro voce precisara do id do livro. ")
                        print(" use os comandos a baixo para consultar.\n")
                        for x in range(0,1000):
                            consulta()
                            print("5| digitar id direto")
                            print("0| voltar")

                            op = int(input())
                            # indetificção das entradas
                            # sai dessa tela
                            if op == 0:
                                break
                            # mostra todos os livros
                            elif op == 1:
                                mostrar_tudo()
                                print("Digite o id para deletar ou 0| para voltar    ")
                                id = int(input())
                                if id == 0:
                                    break
                                else:
                                    delete_book(id)
                            # pesquisa pelo titulo
                            elif op == 2:
                                print("0| Para voltar")
                                nome = input("Digite o titulo do livro:")
                                if nome == '0':
                                    break
                                else:
                                    consultar_livro(nome)
                                    print("Digite o id para deletar ou 0| para voltar    ")
                                    id = int(input())
                                    delete_book(id)
                                    print("livro deletado com sucesso!")
                            # deletar direto pelo id
                            elif op == 5:
                                id = (input("Digite o id do livro ou 0| para voltar"))
                                if id == '0':
                                    break
                                else:
                                    delete_book(id)
                                    print("livro deletado com sucesso!")
                elif op == 2:
                    col()
                elif op == 3:
                    print("1| consultar usario por nome:")
                    print("2| mostrar todos os usuarios")
                    print("3| para registrar um usuario")
                    print("4| Deletar um user")
                    op =input()
                    if op == '1':
                        nome = input("digite o nome:")
                        consultar_user(nome)
                    elif op == '2':
                        tudos_user()
                    elif op == '3':
                        nome = input("digite o nome")
                        senha = input("digite a senha ")
                        staff = (input("digite o cargo"))
                        if register_staff(nome,senha,staff):
                            print("\n")
                            print(f"Usuario '{nome}'adicionado com sucesso!\n")
                        else:
                            print("error! :(   o usuario ja existe.")
                    elif op =='4':
                        print("1| consultar usario por nome:")
                        print("2| mostrar todos os usuarios")
                        op =input()
                        if op == '1':
                            nome = input("digite o nome:")
                            consultar_user(nome)

                            id = input("digite o id para ser deletado | 0 para voltar")
                            if id == '0':
                                pass
                            else:
                                delete_user(id)
                        elif op == '2':
                            tudos_user()
                            id = input("digite o id para ser deletado | 0 para voltar")
                            if id == '0':
                                pass
                            else:
                                delete_user(id)
                elif op == 4:
                    pass



        else:
            col()
    elif op == 2:
        nome = input("digite seu nome:")
        senha = input("digite sua senha:")
        register(nome,senha)
        while True:
            col()