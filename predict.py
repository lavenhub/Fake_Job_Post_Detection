import joblib, re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# NOTE: user will load .pkl locally
def load_model():
    svm_model = joblib.load("svm_model.pkl")
    tfidf = joblib.load("tfidf.pkl")
    return svm_model, tfidf

def predict(text, model, vectorizer):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    return "Fake Job" if model.predict(vec)[0] == 1 else "Real Job"
