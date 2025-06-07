---
title: Academic Style Generator
emoji: 🎓
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: "4.26.0"
app_file: app.py
pinned: false
---

# 🎓 Academic Style Generator (Mistral 4-bit)

This Hugging Face Space features a 4-bit quantized **Mistral-7B model** fine-tuned to generate academic writing style text using contrastive methods.

## 💡 Instructions
- Type an academic prompt (e.g., “What is the role of neural networks in biology?”)
- Adjust `max_tokens` and `temperature` to refine the response.
- Hit "Submit" to generate academic-style content.

## 🚀 Model Details
- Base: `Mistral-7B-v0.1` (quantized)
- Fine-tuned: Contrastive loss on ArXiv abstracts + TED talks
- Quantization: 4-bit (NF4, bnb)

## 📦 Technologies Used
- 🤗 Transformers (with `trust_remote_code=True`)
- 🧠 BitsAndBytes 4-bit quantization
- 🔧 Gradio for fast and interactive UI

## 👨‍💻 Authors
Keer Ni, Muhammad Reza, Joshua Sun  
UC Davis | ECS271 Project
