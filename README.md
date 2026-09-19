# 📩 SMS Spam Detector

A machine learning project that classifies SMS messages as **spam** or **ham (not spam)** using TF-IDF features and classical ML models, with a Streamlit web app for live predictions.

> 🚧 **Status:** In progress (Week 1 of 3) — update this as you go!

<!-- Add a screenshot or GIF of your app here in Week 3 -->
<!-- ![Demo](images/demo.gif) -->

---

## 📌 Problem Statement

Spam messages waste time and can be used for scams and phishing. The goal of this project is to build a model that automatically detects spam SMS messages with high precision and recall.

## 📊 Dataset

- **Name:** SMS Spam Collection
- **Source:** [Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) / [UCI ML Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)
- **Size:** ~5,500 messages (~87% ham, ~13% spam)
- **Note:** The dataset is *imbalanced*, so accuracy alone is not a good metric — this project focuses on precision, recall and F1-score.

## 🛠️ Tech Stack

- Python 3.9+
- pandas, NumPy
- scikit-learn
- NLTK
- Matplotlib / Seaborn
- Streamlit (for the web app)

## 📁 Project Structure

```
spam-detector/
├── data/               # Dataset (not committed — see data/README.md)
├── notebooks/          # Jupyter notebooks (EDA, model training)
├── src/                # Reusable Python code (preprocessing, etc.)
├── models/             # Saved trained models
├── app/                # Streamlit app (Week 3)
├── images/             # Screenshots / plots for the README
├── requirements.txt
└── README.md
```

## 🔬 Approach

1. **Data cleaning** — lowercasing, removing punctuation/numbers/extra spaces
2. **Feature extraction** — TF-IDF vectorization
3. **Modelling** — Multinomial Naive Bayes (baseline), then Logistic Regression and SVM
4. **Evaluation** — Precision, Recall, F1-score, Confusion Matrix
5. **Deployment** — Streamlit app for real-time prediction

## 📈 Results

<!-- Fill this in after Week 2 -->

| Model                | Accuracy | Precision (Spam) | Recall (Spam) | F1 (Spam) |
|----------------------|----------|------------------|---------------|-----------|
| Naive Bayes          |          |                  |               |           |
| Logistic Regression  |          |                  |               |           |
| SVM                  |          |                  |               |           |

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/spam-detector.git
cd spam-detector

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download the dataset and place spam.csv inside data/ (see data/README.md)

# 5. Run the notebooks in notebooks/ (or, after Week 3, launch the app)
streamlit run app/app.py
```

## 💡 What I Learned

<!-- Fill this in at the end: 3-4 honest bullet points -->

-
-
-

## 🔮 Future Improvements

- Try word embeddings or a small deep learning model
- Hyperparameter tuning with GridSearchCV
- Deploy the app on Streamlit Community Cloud
- Extend to fake-news detection

## 👤 Author

**Your Name** — 3rd Semester, B.E./B.Tech (AIML)
[GitHub](https://github.com/<your-username>) · [LinkedIn](https://linkedin.com/in/<your-profile>)
