from conexao import conectar
def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes(
                id  serial PRIMARY  KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INTEGER NOT NULL,
                avaliacao REAL)
            """)
            conexao.commit()
        except Exception as erro:
            print(f'erro ao criar a tabela {erro}')
        finally:
            cursor.close()
            conexao.close()
criar_tabela()

def inserir_fime(titulo,genero,ano,avaliacao):
    conexao,cursor =conectar()
    if conexao:
        try:
            cursor.execute(
            "INSERT INTO filmes (titulo genero, ano, avaliacao)VALUES(%s,%s,%s,%s)",
            (titulo,genero,ano,avaliacao)
            )

            conexao.commit()
        except Exception as  erro:
            print(f'erro ao inserir filmes')
        finally:
            cursor.close()
            conexao.close()
            inserir_fime("avatar","acao",2009,10,0)
            


        
            