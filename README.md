# Fake Job Posting Detection (SVM)

This project detects fraudulent job postings using classical machine learning.

## Model
- TF-IDF Vectorizer
- Linear SVM (class-weighted)

## Dataset
Kaggle Fake Job Postings Dataset

## Labels
- 0 → Real Job
- 1 → Fake Job

## How it works
1. Job text is cleaned
2. Converted to TF-IDF features
3. Classified using SVM

## Files
- `Fake_Job_Posting_Detection_SVM.ipynb` → training notebook
- `predict.py` → inference code

## Limitations
- Classical ML struggles with very short scam messages
- Transformer models perform better

## Model Weights
Trained model files are hosted on Hugging Face:
https://huggingface.co/lavenhub/fake-job-posting-detector-svm

## steps to test the model
- download app.py,tfidf.pkl,svm_model.pkl from files and version option
- save all the files in single folder loacally
- set up the enviroment in command prompt for the given folder where the files are stored
- run the command: pip install streamlit scikit-learn joblib
- execute: streamlit run app.py
- local host will get directed to a webpage to test the model
