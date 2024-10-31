import pandas as pd
import streamlit as st
import time
from math import isnan, sqrt

def readReviews():
    df = pd.read_csv('teste-final.csv')
    return df.iterrows()


def coseno(user, row_values): 
    xy = 0
    sum_x2 = 0
    sum_y2 = 0

    for review in user:
        sum_x2 += user[review] ** 2
        
        rating = row_values[int(review) + 1 ]
        if rating and not isnan(rating):
            xy += user[review] * rating


    for row in row_values[1:]:
        if not isnan(row):
            sum_y2 += row ** 2

    if xy == 0:
        return 0
    else:
        return (xy / (sqrt(sum_x2) * sqrt(sum_y2)))





def knn(userReviews , k):
    print("USer reviews")
    print(userReviews)
    dataset = readReviews()

    distances = [ ]

    for row in dataset:
 
        user_id = int (row[1].values[0])
        values = row[1].values

        distance =float( coseno(userReviews, values))
        distances.append([distance, user_id])
 

    distances.sort(reverse=True)

 

    neighbors = {}
    distances = distances[0:k]
    df = pd.read_csv('teste-final.csv')
    animeList = pd.read_csv('anime.csv')

    for neighbor in distances:
        neighbors[str(neighbor[0])] = {}
        
        row = df[df['user_id'] == neighbor[1]]
       
        for value in row.values:
            
            i = 0
            for rating in value:
                if not isnan(rating) and str(i - 1) not in userReviews and i != 0:
   
                    animeName = animeList[animeList['MAL_ID'] == (i  - 1)].values[0][3]
                    mal_rate = animeList[animeList['MAL_ID'] == (i  - 1)].values[0][4]
                    neighbors[str(neighbor[0])][animeName] = mal_rate
                    
 
                i += 1

            

    best_recommendations = next(iter(neighbors))
 
    best_recommendations =  sorted(neighbors[str(best_recommendations)].items(), key=lambda item: item[1], reverse=True)
    print('recomendacoes')
    print(best_recommendations)

    return best_recommendations




def search_anime(name: str):
    df = pd.read_csv('anime.csv') 
    results = df[df['Name'].str.contains(name, case=False)]

    matrix  = []
    for row in results.iterrows():
        animeId = row[1].values[2]
        animeName = row[1].values[3]
        matrix.append([animeId, animeName])

    return matrix

def recommend_app():
    ratings = {} 
    optionsWithId = []
    options = []
    selected_option = ''
    similar_users = {}
    neighbors = {}

    if 'ratings' not in st.session_state:
        st.session_state['ratings'] = ratings

    if 'ratings' in st.session_state:
        ratings = st.session_state['ratings']

    st.title("Sistema de Recomendação Colaborativo de Animes")

    title = st.text_input("Digite o titulo do anime:")
 
    rating = st.slider(f"Avalie ", 0, 10)

    if title:
        optionsWithId = search_anime(title)
        options = [anime[1] for anime in optionsWithId ]

 
    if len(options):
        selected_option = st.selectbox("Selecione uma opcao", options)

    st.write("### Avaliados")
    if len(ratings): 
        for anime in ratings:
            st.write(f"MAL_ID {anime} : Sua nota = {ratings[anime]} ")

    def append_then_reset(title, rating):
        if selected_option: 
            optionWithId = [ x for x in optionsWithId if x[1] == selected_option]
            ratingWithId = [rating, optionWithId[0][0]]
            

            ratings[str(ratingWithId[1])] = rating
            title = ""
            rating=0
        with st.spinner('Wait for it...'):
            time.sleep(1)
        st.success("Done!")
       
    
    
 

    if st.button('adicionar'):
        append_then_reset(title, rating)

    if st.button('Obter recomendações'):
        similar_users = knn(ratings, 5)
        print('similares')
        print(similar_users)
        if len(ratings) < 5:
            st.error('Avalie pelo menos 5 itens para obter recomendações')
        else:
            print('Obter recomendações')
            
            with st.spinner('Wait for it...'):
                time.sleep(1)
                similar_users = knn(ratings, 5)
            st.success("Done!")
            if similar_users:
                for suggestions in similar_users:
                    st.write(f"Titulo: {suggestions[0]} - Nota no MAL: {suggestions[1]}")
            # knn(ratings)
    

# Função principal do aplicativo Streamlit
def main():
    recommend_app()

if __name__ == "__main__":
    main()