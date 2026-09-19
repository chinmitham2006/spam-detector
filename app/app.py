import sys
from pathlib import Path

import joblib
import numpy as np
import streamlit as st

# Make `src/` importable when running `streamlit run app/app.py` from the repo root
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from src.preprocess import clean_text  # noqa: E402

MODEL_PATH = ROOT / "models" / "spam_classifier.pkl"

st.set_page_config(page_title="SMS Spam Detector", page_icon="📩")


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


def predict(model, text: str):
    """Return (label, confidence between 0 and 1 for the predicted label)."""
    cleaned = clean_text(text)
    pred = int(model.predict([cleaned])[0])

    if hasattr(model, "predict_proba"):
        spam_prob = float(model.predict_proba([cleaned])[0][1])
    else:
        # LinearSVC has no predict_proba, so squash the decision score into 0-1
        score = float(model.decision_function([cleaned])[0])
        spam_prob = 1 / (1 + np.exp(-score))

    confidence = spam_prob if pred == 1 else 1 - spam_prob
    return pred, confidence


st.title("📩 SMS Spam Detector")
st.write(
    "Paste an SMS message below and the model will tell you whether it looks "
    "like **spam** or a normal (**ham**) message."
)

model = load_model()

EXAMPLES = {
    "Choose an example...": "",
    "Spam example": "WINNER!! You have won a free prize. Call now to claim your reward!",
    "Ham example": "Hey, are we still meeting at the library at 5 today?",
}
choice = st.selectbox("Try an example", list(EXAMPLES.keys()))

message = st.text_area("Your message", value=EXAMPLES[choice], height=150)

if st.button("Check message"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        label, confidence = predict(model, message)
        if label == 1:
            st.error(f"🚨 Spam  (confidence: {confidence:.0%})")
        else:
            st.success(f"✅ Not spam  (confidence: {confidence:.0%})")

st.caption(
    "Built with scikit-learn, TF-IDF and Streamlit. "
    "Confidence is approximate for models without probability outputs."
)