import sqlite3

def criando_tabela():  
    try:
        conexao = sqlite3 .connect("biblioteca.db")

        cursor = conexao.cursor()
#criação da tabela 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            disponivel TEXT          
            )
""")
    except Exception as erro:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar criar tabela {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()  

criando_tabela()

#Criando Cadastro

# def cadastro_livro(titulo, autor, ano):
#     try:
#         conexao = sqlite3 .connect("biblioteca.db")
#         cursor = conexao.cursor()
#         cursor.execute("""
#             INSERT INTO livros (titulo, autor, ano, disponivel)
#             VALUES (?,?,?,?)                             
#             """,
#             (titulo, autor, ano, "sim")
#         )
#         conexao.commit()

#     except Exception as error:
#         #Caso ocorra algum erro no banco
#         print(f"erro ao tentar cadastrar livro {error}")
#     finally:
#         #Sempre fechar a conexão
#         if conexao:
#             conexao.close()  
           

# titulo = input("Digite o titulo do livro desejado: ").lower()
# autor = input("Digite o autor do livro: ").lower()
# ano = int(input("Digite o ano do livro: "))

# cadastro_livro(titulo, autor, ano )

#Listagem de livros 

def listar_livros():
    try:
        conexao = sqlite3 .connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM livros")
        for linha in cursor.fetchall():
            print(f"ID: {linha [0]} | TITULO: {linha [1]} | AUTOR: {linha[2]} | ANO: {linha[3]} DISPONIVEL{linha[4]}")
            print("-"*60)

    except Exception as error:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar listar dados da biblioteca {error}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()  
listar_livros()


#Atualização
# def atualizaçao_tabela(disponivel, id_livro):
#     try:
#         conexao = sqlite3 .connect("biblioteca.db")
#         cursor = conexao.cursor()
#         cursor.execute("""
#         UPDATE livros
#         SET  disponivel = ?
#         WHERE id = ?                             
#         """, (disponivel, id_livro)
#         )
#         conexao.commit()
#     except Exception as error:
#         #Caso ocorra algum erro no banco
#         print(f"erro ao tentar atualizar a lista {error}")
#     finally:
#         #Sempre fechar a conexão
#         if conexao:
#             conexao.close()


# disponivel = input("Tem o livro que deseja ? (sim ou não): ")
# id_livro = input("Digite o livro que deseja alterar: ")

# atualizaçao_tabela(disponivel, id_livro)
# listar_livros()

#Apagar os livros

def deletar_livros():
    try:
        conexao = sqlite3 .connect("biblioteca.db")
        cursor = conexao.cursor()
        id = int(input("Digite o id do livros que deseja deletar: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
        conexao.commit()
        print("Livro removido com sucesso!")
    except Exception as error:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar remover livros {error}")
deletar_livros()
    
