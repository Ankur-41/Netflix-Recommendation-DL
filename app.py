import pickle
import string
import numpy as np 
import pandas as pd
import streamlit as st

# Loading the dataset
df = pd.read_csv('netflix_titles.csv')

# Loading the similarity model
with open('similarity.pkl','rb') as file:
    similarity = pickle.load(file)


# Streamlit App UI
st.set_page_config(page_title='Movie Recommendation')
st.title('Netflix Movie Recommendation')
st.write('Enter the last movie title that you had watched 👇')
user_inp = st.text_input('Movie title here : ')


movies = []
def recommend(user_inp): 
    title = user_inp.lower()
    ind = df[df['title'].str.lower() == title]
    if len(ind) == 0:
        return None
    else:
        ind = ind.index[0]
        scores = list(enumerate(similarity[ind]))
        top_scores = sorted(scores,key=lambda x:x[1],reverse=True)[1:6]
        for i in top_scores: 
            movies.append(df.iloc[i[0]]['title'])
    return movies


if st.button('Show Recommendation'):
    if user_inp.strip() == '':
        st.warning('Please enter a movie title first.')
    else:
        output = recommend(user_inp)
        if output is None:
            st.warning('This movies is not present in our dataset so we cant give you recommendation.')
        else:
            for movie in output:
                st.write(movie.title())



