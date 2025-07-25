import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmZGRlNGQ0MzhiZmFkNTY0MWZjZmQzNTY3OTRlNWIwMSIsIm5iZiI6MTc0MDc2NzI3NC4wMDg5OTk4LCJzdWIiOiI2N2MyMDAyYWM1ZGU4NDJiNGJhMjdiYzUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.bL8ZH4jy3_cpNESqNI5N-__7uoetncuvmd2t4XWuBHI"
}

    response = requests.get(url.format(movie_id), headers=headers)


    
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[0:6]
    recommend_movies = []
    recommend_movies_posters=[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb' ))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    

