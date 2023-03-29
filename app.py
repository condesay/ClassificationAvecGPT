import openai
import streamlit as st
from streamlit_chat import message

openai.api_key = "YOUR_API_KEY_HERE"

def classify_document(prompt, engine):
    completion = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.0,
    )

    label = completion.choices[0].text
    return label.strip()

def main():
    # Set page title
    st.title("ChatGPT Web App Par Sayon")

    # Set up sidebar options
    engine_options = {
        "Davinci": {
            "Text": "text-davinci-003",
            "Code": "code-davinci-002",
            "Classification": "text-davinci-003"
        }
    }

    # Set up initial settings
    settings = {
        "engine": "Davinci",
        "mode": "Text",
        "temperature": 0.7,
        "max_tokens": 190,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }

    # get user API key
    api_key = st.text_input("Entrez votre clé OpenAI API Key:", type="password")
    
    if api_key:
        openai.api_key = api_key

        # get user input
        user_input = st.text_input("Entrez votre texte à classifier:")

        # classify input text
        if user_input:
            label = classify_document(user_input, engine_options[settings["engine"]]["Classification"])
            st.write("La classification du texte est:", label)


if __name__ == '__main__':
    main()
