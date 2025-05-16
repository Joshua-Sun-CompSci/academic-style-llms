import os
import json
import random
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

with open("data/sampled_arxiv.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def clean_text(text, max_length=1000):
    if not isinstance(text, str):
        return None

    text = re.sub(r"\$.*?\$", "", text)
    text = re.sub(r"\\\[.*?\\\]", "", text)
    text = re.sub(r"\\begin\{.*?\}.*?\\end\{.*?\}", "", text, flags=re.DOTALL)

    text = re.sub(r"\s+", " ", text).strip()

    return text[:max_length]


cleaned_data = []
for entry in data:
    abstract = entry.get("abstract") or entry.get("summary")
    cleaned = clean_text(abstract)
    if cleaned and len(cleaned) > 100:
        cleaned_data.append(cleaned)

print(f"{len(cleaned_data)} cleaned entries.")

train_texts, temp_texts = train_test_split(cleaned_data, test_size=0.2, random_state=42)
val_texts, test_texts = train_test_split(temp_texts, test_size=0.5, random_state=42)

os.makedirs("data/splits", exist_ok=True)

with open("data/splits/train.json", "w", encoding="utf-8") as f:
    json.dump(train_texts, f, ensure_ascii=False, indent=2)
with open("data/splits/val.json", "w", encoding="utf-8") as f:
    json.dump(val_texts, f, ensure_ascii=False, indent=2)
with open("data/splits/test.json", "w", encoding="utf-8") as f:
    json.dump(test_texts, f, ensure_ascii=False, indent=2)

print("Saved train/val/test splits.")
