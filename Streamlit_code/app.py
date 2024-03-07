import streamlit as st
import pickle
import pandas as pd
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

def recommend(game):
    game_index = games[games["title"] == game].index[0]
    distances = similarity[game_index]
    games_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_games=[]
    for i in games_list:
        recommended_games.append(games.iloc[i[0]].title)
    return recommended_games

def recommend_url(game):
    game_index = games[games["title"] == game].index[0]
    distances = similarity[game_index]
    games_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_url=[]
    for i in games_list:
        recommended_url.append(games.iloc[i[0]].url)
    return recommended_url

game_dict = pickle.load(open("game_dict.pkl", "rb"))
games = pd.DataFrame(game_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Λ.ᄃ.Ƨ GΛMΣ DΣᄃK")
selected_game_option = st.selectbox("Enter the game name", games["title"].values)

if st.button("Recommend"):
    recommendations = recommend(selected_game_option)
    recommendation_urls = recommend_url(selected_game_option)

    st.write("Recommended Games:")
    for game, url in zip(recommendations, recommendation_urls):
        st.image(url)
        st.write(game)
