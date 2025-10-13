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

def inserir_fimes(titulo,genero,ano,avaliacao):
    conexao,cursor =conectar()
    if conexao:
        try:
            cursor.execute(
            "INSERT INTO filmes (titulo, genero, ano, avaliacao)VALUES(%s,%s,%s,%s)",
            (titulo,genero,ano,avaliacao)
            )

            conexao.commit()
        except Exception as  erro:
            print(f'erro ao inserir filmes{erro}')
        finally:
            cursor.close()
            conexao.close()
inserir_fimes("avatar","açao", 2009 ,10)

def listar_filmes():
    conexao,cursor =conectar()
    if conexao:
        try:
            cursor.execute(
             "SELECT * FROM filmes ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as  erro:
            print(f'erro ao tentar listar filmes{erro}')
        finally:
            cursor.close()
            conexao.close()
 
def atualiza_filme(id_filme,nova_avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filmes SET avaliacao = %s WHERE id = %s",
                (nova_avaliacao, id_filme)
            )
            conexao.commit()
        except Exception as  erro:
            print(f'erro ao tentar atualizar o filmes{erro}')
        finally:
            cursor.close()
            conexao.close()
            
def deletar_filme(id_film):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETAR FROM filmes  WHERE id = %s",(id_filme,)
            )
            conexao.commit()
        except Exception as  erro:
            print(f'erro ao tentar deletar o filmes{erro}')
        finally:
            cursor.close()
            conexao.close()
deletar_filme(9)