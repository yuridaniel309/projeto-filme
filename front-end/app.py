import streamlit as st 
import requests

#url  da api fastAPI
API_URL ="http://127.0.0.1.8000"

st.set_page_config(page_title="gerenciador de filmes", page_icon="🎬")
st.title("🎥 gerenciador de filmes")

#menu lateral
menu =st.sidebar.radio("navegação", ["catalogo","adicionar filmes"])

if menu == "catalogo":
    st.subheader("todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes",[]
        if filmes:
        for filmes in filmes
        st.write(f"**")
        print()
    else:
        st.error("erro ao acessar a API")