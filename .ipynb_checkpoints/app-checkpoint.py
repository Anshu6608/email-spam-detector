from flask import Flask, request, render_template
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form["email_text"]
    email_cleaned = email.lower()
    email_vector = vectorizer.transform([email_cleaned])
    result = model.predict(email_vector)[0]
    label = "Spam" if result == 1 else "Ham"
    return render_template("index.html", result=label)

if __name__ == "__main__":
    app.run(debug=True)
