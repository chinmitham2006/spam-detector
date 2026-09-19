import re


def clean_text(text: str) -> str:
    """Basic text cleaning used for BOTH training and prediction.

    Keeping this in one place guarantees the app (Week 3) cleans
    text exactly the same way as the training notebook.
    """
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", " ", text)   # keep only letters and spaces
    text = re.sub(r"\s+", " ", text).strip()  # collapse extra whitespace
    return text
