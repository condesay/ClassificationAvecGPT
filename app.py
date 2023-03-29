import openai
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification

openai.api_key = "YOUR_API_KEY_HERE"

def classify_text(text, model, categories):
    # Tokenize input text
    tokens = model.tokenizer(text, truncation=True, padding=True, return_tensors="pt")
    # Generate output logits
    output = model(**tokens).logits
    # Get predicted category
    category_index = output.argmax().item()
    predicted_category = categories[category_index]
    return predicted_category

def main():
    # Set page title
    st.title("ChatGPT Web App Par Sayon")

    # Set up sidebar options
    engine_options = {
        "Davinci": {
            "Text": "text-davinci-003",
            "Code": "code-davinci-002"
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

if __name__ == '__main__':
    main()
