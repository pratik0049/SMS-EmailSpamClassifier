

---

# 📩 SMS Spam Classifier

Welcome to the SMS Spam Classifier! This application leverages Natural Language Processing (NLP) and Machine Learning techniques to classify SMS messages as either **Spam** or **Not Spam**.

🔗 **Live Demo:** [https://sms-spam-classifyy.streamlit.app/](https://sms-spam-classifyy.streamlit.app/)

---

## 🚀 Features

* **User-Friendly Interface:** Input your SMS message and receive an instant classification.
* **Real-Time Processing:** Utilizes a trained machine learning model to predict the nature of the message.
* **Efficient Preprocessing:** Implements text normalization, tokenization, stopword removal, and stemming.

---

## 📊 Model Performance

The classifier has been evaluated on a standard SMS dataset, achieving the following metrics:

* **Accuracy:** 98.16%
* **Precision (Spam):** 98.28%
* **Confusion Matrix:**

[[901   2]
 [ 17 114]]

These metrics indicate a strong ability to correctly identify spam messages while minimizing false positives.

---

## 🧪 How It Works

1. **Text Input:** Users enter an SMS message into the provided text area.
2. **Text Preprocessing:** The input text undergoes:

   * Lowercasing
   * Tokenization
   * Removal of stopwords and punctuation
3. **Feature Extraction:** The processed text is transformed using a TF-IDF vectorizer.
4. **Prediction:** The transformed text is fed into a trained Naive Bayes model to classify the message.
5. **Output:** The app displays whether the message is "Spam" or "Not Spam" based on the model's prediction.

---

## 🛠️ Technologies Used

* **Streamlit:** For building the interactive web application.
* **scikit-learn:** For machine learning algorithms and model evaluation.
* **NLTK:** For natural language processing tasks.
* **Pickle:** For saving and loading the trained model and vectorizer.

---

## 📥 Setup Instructions

To run this application locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/pratik0049/sms-spam-classifier.git
   cd sms-spam-classifier
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```
