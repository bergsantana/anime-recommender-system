import pandas as pd
import streamlit as st
import time
 
def readReviews():
    return pd.read_csv('user-ratings.csv')

def search_anime(name: str):
    df = pd.read_csv('anime.csv') 
    results = df[df['Name'].str.contains(name, case=False)]

    matrix  = []
    for row in results.iterrows():
        animeId = row[1].values[0]
        animeName = row[1].values[1]
        matrix.append([animeId, animeName])

    return matrix

def recommend_app():
    
    ratings = [] 
    optionsWithId = []
    options = []
    selected_option = ''

    if 'ratings' not in st.session_state:
        st.session_state['ratings'] = ratings

    if 'ratings' in st.session_state:
        ratings = st.session_state['ratings']

    st.title("Sistema de Recomendação Colaborativo de Animes")

    title = st.text_input("Digite o titulo do anime:")
 
    rating = st.slider(f"Avalie ", 0, 10)

    if title:
        optionsWithId = search_anime(title)
        print(optionsWithId)
        options = [anime[1] for anime in optionsWithId ]

        # options.append(search_anime(title))
        print(options)

 
    if len(options):
       # print('options?')
       #  print(options)
        selected_option = st.selectbox("Pesquise uma opcao", options)

 




    st.write("### Avaliados")
    if len(ratings): 
        for anime in ratings:
            st.write(f"{anime[1]} - {anime[0]}")

         
    if st.button('adicionar'):
        if selected_option: 
            ratings.append([rating, selected_option])
            title = ''
            rating=0
        with st.spinner('Wait for it...'):
            time.sleep(2)
        st.success("Done!")

# Função principal do aplicativo Streamlit
def main():
    recommend_app()

if __name__ == "__main__":
    main()