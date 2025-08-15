import streamlit as st
import pickle
import pandas as pd

# Load movie data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Choose a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    def recommend(movie):
        index = movies[movies['title'] == movie].index[0]
        distances = similarity[index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = []
        for i in movie_list:
            recommended_movies.append(movies.iloc[i[0]].title)
        return recommended_movies

    recommendations = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for m in recommendations:
        st.write(m)
