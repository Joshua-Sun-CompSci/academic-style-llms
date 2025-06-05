# 📚 Academic Writing Generator

This demo features a fine-tuned language model trained to generate academic-style text. 
It adapts GPT-2/Mistral to emulate scholarly tone, vocabulary, and structure.

## ✨ Try It Out
- **Input**: Topic or prompt (e.g., "Explain neural networks")
- **Output**: Coherent academic writing

## ⚙️ Model Info
- Base: GPT-2 / Mistral
- Training: ArXiv abstracts, TED talks, academic lectures
- Features: Contrastive loss, LoRA (optional), academic style classifier

## 🛠️ How It Works
- Tokenizer: AutoTokenizer
- Model: AutoModelForCausalLM
- Interface: Gradio on Hugging Face Spaces

## 🚀 Usage
Adjust the max tokens and temperature sliders to experiment with output style and length.

## 🧠 Authors
Keer Ni, Muhammad Reza, Joshua Sun  
UC Davis | ECS271 Project

## 📝 Citation
Model and dataset details available in [project proposal](link-to-pdf-if-hosted).
