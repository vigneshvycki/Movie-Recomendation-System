import streamlit as st
import pickle
import pandas as pd
import requests


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movie_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
        
movie_dict=pickle.load(open('/Users/admin/Desktop/new_project/Movie recommend/movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('/Users/admin/Desktop/new_project/Movie recommend/similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movie_name=st.selectbox(
    'How would you like to be contact?',
    movies['title'].values
)
if st.button('Reccommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)