import streamlit as st

st.title('Enter Movies')
numMovies = 2
movies = []
for i in range(numMovies):
    movie = st.text_input('Movie title', 'Enter Movie Title', key=i)
    movies.append(movie)
# movie1 = st.text_input('Movie title', 'Enter Movie Title', key = m1)
# movie2 = st.text_input('Movie title', 'Enter Movie Title')
entered = st.button('Submit')
if entered:
    st.title('Movies Entered!')
    i = 1
    for m in movies:
        st.write("Movie ", i, ": ", m)
        i += 1