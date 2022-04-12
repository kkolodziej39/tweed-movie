import streamlit as st
import numpy as np

def addPoints(movieName, choice, totalNumMovies):
    moviePoints[movieName] += totalNumMovies - choice

if 'initialized' not in st.session_state:
    st.session_state.initialized = False

if 'movies_gathered' not in st.session_state:
    st.session_state.movies_gathered = False

if 'calculate' not in st.session_state:
    st.session_state.calculate = False

st.title('Tweed!')
numMovies = st.number_input('Enter the number of movies to be pitched', min_value=1, max_value=5, value=1, step=1)
numPeople = st.number_input('Enter the number of people pitching', min_value=3, max_value=10, value=3, step=1)
setUp = st.button('Submit')
if setUp:
    st.session_state.initialized = True

widgetKeys = np.arange(0,100, 1, dtype=int )
k = 0
if st.session_state.initialized:
    # numMovies = int(numMovies)
    # numPeople = int(numPeople)
    movies = []
    moviePoints = {}
    peopleMovie = {}
    for n in range(numPeople):
        toDisplay = "Enter Person " + str(n+1) + " Name"
        filler = "Person " + str(n+1)
        person = st.text_input(toDisplay, filler, key=widgetKeys[k])
        k += 1
        personsMovies = []
        for i in range(numMovies):
            movie = st.text_input('Movie title', 'Enter Movie Title', key=widgetKeys[k])
            movies.append(movie)
            moviePoints[movie] = 0
            personsMovies.append(movie)
            k += 1
        peopleMovie[person] = personsMovies

    entered = st.button('Submit', key=widgetKeys[k])
    k += 1
    if entered:
        st.session_state.movies_gathered = True

if st.session_state.movies_gathered:
    st.title('Movies Entered:')
    i = 1
    for m in movies:
        st.write("Movie ", i, ": ", m)
        i += 1

    st.title('Rank Movies!')
    for key, value in peopleMovie.items():
        subHead = key + " please rank the movies..."
        st.subheader(subHead)
        moviesToVoteOn = np.setdiff1d(movies, value)
        for choice in range(len(moviesToVoteOn)):
            newOption = 'Please select choice ' + str(choice+1)
            option = st.selectbox(
            newOption,
            moviesToVoteOn, key = widgetKeys[k])
            st.write('You selected:', option)
            addPoints(option, choice, len(moviesToVoteOn))
            k += 1
    determineWinner = st.button('Calculate Winner', key=widgetKeys[k])
    if determineWinner:
        st.session_state.calculate = True


if st.session_state.calculate:
    # get winner
    movieList = sorted(moviePoints.items(), key=lambda x: x[1], reverse=True)
    sortMovies = dict(movieList)
    st.write(sortMovies)