import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide")

#######################################


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=34a878418067f3134821ccc93668bdb9&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def fetch_homepage(movie_id):
    home = f"https://www.themoviedb.org/movie/{movie_id}"
    return home


st.header("Movie Recommender System")

#######################################

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list1 = sorted(list(enumerate(distances)),reverse=True , key = lambda x:x[1])[1:13]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_homepage = []
    for i in movies_list1:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_homepage.append(fetch_homepage(movie_id))
    return recommended_movies , recommended_movies_posters , recommended_movies_homepage

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

rating = pickle.load(open('rating.pkl','rb'))
popular = pd.DataFrame(rating)


selected_movie_name = st.selectbox(
    'list of movies',
    movies['title'].values
)

if st.button('Recommend'):
    names , posters , homepages = recommend(selected_movie_name)

    col1 , col2 , col3 , col4  = st.columns(4)

    with col1:
        st.image(posters[0])
        st.markdown(f"[{names[0]}]({homepages[0]})")

    with col2:
        st.image(posters[1])
        st.markdown(f"[{names[1]}]({homepages[1]})")

    with col3:
        st.image(posters[2])
        st.markdown(f"[{names[2]}]({homepages[2]})")

    with col4:
        st.image(posters[3])
        st.markdown(f"[{names[3]}]({homepages[3]})")

    col5, col6, col7, col8  = st.columns(4)
    with col5:
        st.image(posters[4])
        st.markdown(f"[{names[4]}]({homepages[4]})")

    with col6:
        st.image(posters[5])
        st.markdown(f"[{names[5]}]({homepages[5]})")

    with col7:
        st.image(posters[6])
        st.markdown(f"[{names[6]}]({homepages[6]})")

    with col8:
        st.image(posters[7])
        st.markdown(f"[{names[7]}]({homepages[7]})")


    col9, col10, col11, col12 = st.columns(4)
    with col9:
        st.image(posters[8])
        st.markdown(f"[{names[8]}]({homepages[8]})")

    with col10:
        st.image(posters[9])
        st.markdown(f"[{names[9]}]({homepages[9]})")

    with col11:
        st.image(posters[10])
        st.markdown(f"[{names[10]}]({homepages[10]})")

    with col12:
        st.image(posters[11])
        st.markdown(f"[{names[11]}]({homepages[11]})")

# Debugging
# st.write(f"Selected movie: {selected_movie_name}")
# st.write("Homepages:")
# for homepage in homepages:
#     st.write(homepage)



import streamlit.components.v1 as components

st.text('most watched movies')

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

imageUrls = [
    fetch_poster(155),
    fetch_poster(19995),
    fetch_poster(24428),
    fetch_poster(293660),
    fetch_poster(157336),
    fetch_poster(68718),
    fetch_poster(118340),
    fetch_poster(70160),
    fetch_poster(76341),
    fetch_poster(550),
    fetch_poster(49026),
    fetch_poster(603),
    fetch_poster(68721),
    fetch_poster(1726),
    fetch_poster(120),
    fetch_poster(135397),
    fetch_poster(680),
    fetch_poster(49051),
    fetch_poster(278),
    fetch_poster(122),
]


image_links = [f"<a href='{fetch_homepage(movie_id)}' target='_blank'><img src='{url}'/></a>" for url, movie_id in zip(imageUrls, [155, 19995, 24428, 293660, 157336, 68718, 118340, 70160, 76341, 550, 49026, 603, 68721, 1726, 120, 135397, 680, 49051, 278, 122])]


imageCarouselComponent(imageUrls=imageUrls, height=300)

st.text('Highest rated movies')

imageCarouselComponent1 = components.declare_component("image-carousel-component1", path="frontend/public")

imageUrls1 = [
    fetch_poster(361505),
    fetch_poster(78373),
    fetch_poster(40963),
    fetch_poster(346081),
    fetch_poster(69848),
    fetch_poster(88641),
    fetch_poster(278),
    fetch_poster(43867),
    fetch_poster(238),
    fetch_poster(129),
    fetch_poster(244786),
    fetch_poster(240),
    fetch_poster(680),
    fetch_poster(550),
    fetch_poster(322745),
    fetch_poster(424),
    fetch_poster(1891),
    fetch_poster(155),
    fetch_poster(510),
    fetch_poster(30973),
]


image_links1 = [f"<a href='{fetch_homepage(movie_id)}' target='_blank'><img src='{url}'/></a>" for url, movie_id in zip(imageUrls1, [361505, 78373, 40963, 346081, 69848, 88641, 278, 43867, 238, 129, 244786, 240, 680, 550, 322745, 424, 1891, 155, 510, 30973])]


imageCarouselComponent1(imageUrls=imageUrls1, height=300)