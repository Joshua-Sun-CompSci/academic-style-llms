import os
import json
import random
from kagglehub import dataset_download

download_dir = dataset_download("Cornell-University/arxiv")

for filename in os.listdir(download_dir):
    if filename.endswith(".json") or filename.endswith(".jsonl"):
        OG_PATH = os.path.join(download_dir, filename)
        break
else:
    raise FileNotFoundError("No .json or .jsonl file found in downloaded dataset directory")

print(f"Found data file at: {OG_PATH}")

output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "sampled_arxiv.json")

print("Reading lines...")
with open(OG_PATH, "r", encoding="utf-8") as f:
    all_entries = [json.loads(line) for line in f]

print(f"Total entries: {len(all_entries)}")

print("Sampling 500,000 entries...")
sampled_data = random.sample(all_entries, k=500_000)

print(f"Saving sampled data to {output_file}...")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(sampled_data, f, ensure_ascii=False, indent=2)

print(f"✅ Done! Sampled data saved at: {output_file}")
