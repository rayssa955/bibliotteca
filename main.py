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

def cadastro_livro(titulo, autor, ano):
    try:
        conexao = sqlite3 .connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO livros (titulo, autor, ano, disponivel)
            VALUES (?,?,?,?)                             
            """,
            (titulo, autor, ano, "sim")
        )
        conexao.commit()

    except Exception as error:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar cadastrar livro {error}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()  
           

titulo = input("Digite o titulo do livro desejado: ").lower()
autor = input("Digite o autor do livro: ").lower()
ano = int(input("Digite o ano do livro: "))

cadastro_livro(titulo, autor, ano )


