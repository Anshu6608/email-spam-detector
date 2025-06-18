# 📧 Email Spam Detection App

This is a simple machine learning project built using **Naive Bayes** and **Flask** to detect whether an email is spam or not.

---

## 🔍 Features

- Uses a dataset of labeled spam/ham emails
- Preprocessing with TF-IDF vectorization
- Model trained using Naive Bayes
- Simple web interface built using Flask

---

## 🛠️ Installation & Running Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/email-spam-detector.git
   cd email-spam-detector
   
2. pip install flask scikit-learn pandas
 
3. set FLASK_APP=app.py  # on Windows
    flask run

4. Open in browser:
   [http://localhost:5000](http://localhost:5000)

---

## 🧠 Model Training

- Cleaned and tokenized text
- Vectorized with TF-IDF
- Trained a Multinomial Naive Bayes classifier

---

## 📁 Project Structure

email-spam-detector/
├── app.py
├── model.pkl
├── vectorizer.pkl
├── spam.csv
├── templates/
│ └── index.html
├── Email spam classifier.ipynb
└── README.md


---

## 🚀 Future Improvements

- Deploy online (e.g., Render, Streamlit, or Replit)
- Add email file upload or real-time classification
- Improve preprocessing with lemmatization and n-grams

---

## 🙌 Made with ❤️ by Anshu Singh


