import openai
import streamlit as st

openai.api_key = "YOUR_OPENAI_API_KEY_HERE"

def classify_sentiment(prompt, engine):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.5
    )

    sentiment = response.choices[0].text.strip()
    if sentiment == "Positive":
        return "positive"
    elif sentiment == "Negative":
        return "negative"
    else:
        return "neutral"

def main():
    # Set page title
    st.title("ChatGPT Web App Par Sayon")

    # Set up sidebar options
    engine_options = {
        "Davinci": {
            "Sentiment Analysis": "text-davinci-002"
        }
    }

    # Set up initial settings
    settings = {
        "engine": "Davinci",
        "mode": "Sentiment Analysis",
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
            engine_id = engine_options[settings["engine"]][settings["mode"]]
            prompt = f"Sentiment Analysis: {user_input}\nSentiment:"
            sentiment = classify_sentiment(prompt, engine_id)
            st.write(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
