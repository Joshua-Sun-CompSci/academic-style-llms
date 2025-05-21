import os
import json
import random
import re
from sklearn.model_selection import train_test_split

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

output_path = "data/data.txt"
with open(output_path, "w", encoding="utf-8") as f:
    for line in cleaned_data:
        f.write(line.strip() + "\n\n")

print(f"Saved data to {output_path}.")