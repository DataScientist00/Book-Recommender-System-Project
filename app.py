
import pickle
import streamlit as st
import numpy as np


st.title('Book Recommender System Using Machine Learning 📚')
model = pickle.load(open('model.pkl','rb'))
book_names = pickle.load(open('book_names.pkl','rb'))
final_rating = pickle.load(open('final_rating.pkl','rb'))
book_pivot = pickle.load(open('book_pivot.pkl','rb'))


def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url



def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    _ , suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for j in books:
                books_list.append(j)
    return books_list , poster_url       


st.write(f"Total books available: {len(book_names)}")

selected_books = st.selectbox(
    "Type or select a book from the dropdown",book_names)

if st.button('Show Recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)
    
    st.subheader("Recommended Books 📚")
    
    # Create a row of 5 columns
    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            # Generate Google search URL
            google_search_url = f"https://www.google.com/search?q={recommended_books[i+1].replace(' ', '+')} + book"

            st.markdown(
                f"""
                <div style="text-align: center; padding: 10px; border-radius: 10px; background-color: #f9f9f9; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                    <a href="{google_search_url}" target="_blank">
                        <img src="{poster_url[i+1]}" width="120" style="border-radius: 8px; cursor: pointer;">
                    </a><br>
                    <p style="font-weight: bold; color: #333;">{recommended_books[i+1]}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )

