---
title: Academic Style Generator (GPT-2)
emoji: 🧠
colorFrom: gray
colorTo: purple
sdk: gradio
sdk_version: "4.26.0"
app_file: app.py
pinned: false
---
# 🧠 Academic Style Generator (GPT-2)

This Hugging Face Space features a fine-tuned **GPT-2 model** trained to generate formal, academic-style text using a large subset of research paper abstracts from arXiv.

## 💡 Instructions
- Enter an academic-style prompt (e.g., “Explain diffusion models in simple terms.”)
- Adjust `max_tokens` and `temperature` to control output length and creativity.
- Press "Submit" to generate a formal academic paragraph.

## 🚀 Model Details
- Base: `gpt2` (124M parameters)
- Fine-tuned: Cross-entropy on 500K arXiv abstracts
- Format: Plain-text input with token-level left-to-right generation

## 📦 Technologies Used
- 🤗 Transformers
- 🧠 GPT-2 full fine-tuning (no LoRA or quantization)
- 🔧 Gradio for web-based interaction

## 👨‍💻 Authors
Keer Ni, Muhammad Reza, Joshua Sun  
UC Davis | ECS271 Project