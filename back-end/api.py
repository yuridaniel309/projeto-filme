from fastapi import FastAPI
import funcao

#rodar o fastapi
#python -m uvicorn api:app -- reload
#testar api fastAPI
#/docs > documentação swgger
#/redoc >docomentação redoc


#iniciar o fastapi
app = FastAPI(title="gerenciador de filmes")

#get = pegar/ listar
#post = criar / enviar
#put = atualizar
#delete = deletar


@app.get("/")
def home():
    return{"mensagem": " quero café prrof"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str,ano: int, avaliacao: float):
    funcao.inserir_fimes(titulo,genero,ano,avaliacao)
    return{"mensagem": "filme adicional com sucesso!"}
    
