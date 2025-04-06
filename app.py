import requests
import streamlit as st

st.set_page_config(page_title="The Great Dictionary", page_icon=":book:")
st.title("The Great Dictionary")

st.text("A english language online dictionary.")

word = st.text_input("Enter the word :")

if st.button("Search") or word:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        word_data = data[0]

        # Get first definition
        first_definition = word_data['meanings'][0]['definitions'][0]['definition']
        st.text(f"Definition of '{word}' : {first_definition}")

        # Get example
        try :
            example = word_data['meanings'][0]['definitions'][0]['example']
            st.text(f"Example of '{word}' in a sentence : {example}")
        except :
            st.text(f"No example found for this word : {word}")
    else:
        st.text(f"Word not found : {word}")

st.markdown(
    """
    <hr>
    <div style='text-align: center; padding-top: 10px; font-size: 14px; color: gray;'>
        Built with ❤️ by Arijeet Dutta using Streamlit and Dictionary API.
    </div>
    """,
    unsafe_allow_html=True
)