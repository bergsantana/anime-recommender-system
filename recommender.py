import pandas as pd
import streamlit as st
 
 
def readReviews():
    return pd.read_csv('updated-list.csv')


def recommend_app():
    st.title("Sistema de Recomendação Colaborativo de Animes")

    searched = [] 
    title = st.text_input("Digite o titulo do anime:")

    rating = st.slider(f"Avalie ", 0, 10)

    if st.button('adicionar'):

        if title: 
            searched.append({title: title, rating: rating})


    st.write("### Avaliados")
    if len(searched): 
        for anime in searched:
            st.write(anime)



    # if st.button("Recomendar Músicas"):
    #     if username in users:
    #         recommendations = recommend(username, ratings)
    #         st.write(f"Recomendações para {username}")
    #         for recommendation in recommendations:
    #             st.write(f"{recommendation[0]} - Pontuação: {recommendation[1]}")

    #     else: 
    #         st.write("Nome de usuário não encontrado. Por favor, insira um nome de usuário válido.")


# Função principal do aplicativo Streamlit
def main():
    recommend_app()

if __name__ == "__main__":
    main()