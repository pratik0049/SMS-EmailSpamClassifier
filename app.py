# app.py
import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

# NLTK setup
nltk.download('punkt')
nltk.download('stopwords')
ps = PorterStemmer()

# Load model & vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


# EXACT SAME preprocessing function as training
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer

ps = PorterStemmer()  # initialize stemmer

def transform_text(text):
    text = text.lower()
    words = text.split()  # simple split instead of nltk.word_tokenize

    # Keep only alphanumeric words
    words = [word for word in words if word.isalnum()]

    # Remove stopwords and punctuation
    words = [word for word in words if word not in stopwords.words('english') and word not in string.punctuation]

    # Apply stemming
    words = [ps.stem(word) for word in words]

    return " ".join(words)


# Streamlit UI
st.set_page_config(page_title="📩 Spam Detector", page_icon="🚨", layout="centered")
st.title("📩 SMS / Email Spam Classifier")
st.write("Enter a message below and check if it is Spam or Not Spam.")

input_sms = st.text_area("✍️ Enter the message:")

if st.button("🔍 Predict"):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message first!")
    else:
        # Preprocess message
        transformed_sms = transform_text(input_sms)

        # Vectorize
        vector_input = vectorizer.transform([transformed_sms]).toarray()

        # Predict
        result = model.predict(vector_input)[0]

        # Show result
        if result == 1:
            st.error("🚨 This is **Spam Message**!")
        else:
            st.success("✅ This is **Not Spam**.")
