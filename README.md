# 📩 SMS Spam Detector

A machine learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using TF-IDF features and classical machine learning models, with a Streamlit web application for real-time predictions.

**Status: Completed ✅**

---

## 🎯 Problem Statement

Spam messages can waste time and may contain unwanted advertisements, scams, or misleading content.

The goal of this project is to build a machine learning system that can automatically classify SMS messages as:

- 🟢 **Ham** — legitimate message
- 🔴 **Spam** — unwanted or promotional message

The trained model is integrated into a Streamlit web application where users can enter a message and receive a prediction.

---

## 📊 Dataset

The project uses the **SMS Spam Collection** dataset.

- Total messages: **5,572**
- Ham messages: **4,825**
- Spam messages: **747**
- The dataset contains more ham messages than spam messages, making it an imbalanced classification problem.
- After cleaning and removing duplicate cleaned messages, **5,084 messages** remained.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Naive Bayes
- Logistic Regression
- Linear SVM
- GridSearchCV
- Joblib
- Streamlit
- Jupyter Notebook

---

## 🔍 Project Approach

### 1. Data Cleaning

The SMS messages were cleaned by:

- Converting text to lowercase
- Removing unnecessary punctuation and characters
- Removing duplicate cleaned messages

### 2. Feature Extraction

**TF-IDF (Term Frequency–Inverse Document Frequency)** was used to convert text messages into numerical features that machine learning models can understand.

The final tuned model used:

- Maximum features: **5,000**
- N-gram range: **(1, 2)**

This means the model considered both individual words and pairs of words.

### 3. Model Comparison

Three machine learning models were compared:

1. Multinomial Naive Bayes
2. Logistic Regression
3. Linear Support Vector Machine (SVM)

### 4. Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- 5-fold Cross-Validation

F1-score was given importance because the dataset is imbalanced and both false positives and false negatives matter in spam detection.

### 5. Hyperparameter Tuning

GridSearchCV was used to tune the Linear SVM model.

The best parameters found were:

```text
C = 10
TF-IDF max_features = 5000
TF-IDF ngram_range = (1, 2)