from conexao import conectar
def criar_tabela():
    conexao, cursor = conectar
    if conexao:
        try:
            cursor.execute("""
             CREATE TABLE IF NOT EXISTS filmes(
              id  serisl primary key    
               titulo TEXT NOT NULL
               genero TEXT NOT NULL
              ano INTEGER NOT NULL
              avaliacao REAL)
            """)
            conexao.commit()
        except Exception as erro:
            print(f'erro ao criar a tabela {erro}')
        finally:
            cursor.close()
            conexao.close()
            criar_tabela()
            