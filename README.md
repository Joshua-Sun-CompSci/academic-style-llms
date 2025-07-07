# 📚 Academic Style Tuning for LLMs

This project explores the fine-tuning of large language models (LLMs), specifically GPT-2 and Mistral-7B, to better emulate formal academic writing. Using a curated subset of arXiv abstracts, we demonstrate how domain-specific fine-tuning can enhance stylistic fidelity in scholarly communication—though limitations like hallucinations and generic phrasing remain.

## 👨‍💻 Team Members

- **Joshua Sun** (zysun@ucdavis.edu)
- **Keer Ni** (knni@ucdavis.edu)  
- **Muhammad Reza** (msreza@ucdavis.edu) 

## 📁 Repository Structure

- 🗂️ Main Project: **[This repo]**
- 🔬 GPT-2 Fine-Tuning: [markteammate/GPT-2_academic_style_tune](https://huggingface.co/markteammate/GPT-2_academic_style_tune)
- 🔬 Mistral-7B Fine-Tuning (QLoRA): [markteammate/Mistral_academic_style_tune](https://huggingface.co/markteammate/Mistral_academic_style_tune)

## 🔍 Motivation

While LLMs such as GPT-2 are powerful, they often produce text that lacks the tone, structure, and clarity expected in academia. Our goal was to improve stylistic alignment for use in academic writing assistants, research tools, and educational applications.

## 🧠 Models

| Model         | Method       | Params | Fine-Tuning Technique     |
|---------------|--------------|--------|----------------------------|
| GPT-2 (124M)  | Full training | 124M   | Cross-entropy loss         |
| Mistral-7B    | QLoRA        | 7B     | Causal LM with prompts     |

Both models were fine-tuned on ~500K abstracts from the arXiv dataset.

## 🛠️ Methodology

- **Preprocessing**: Abstract cleaning, LaTeX removal, length standardization, GPT-2 BPE tokenization.
- **Training**:
  - GPT-2: Plain-text format, trained for 1.2 epochs.
  - Mistral-7B: Prompt-target pairs (title → abstract), trained with QLoRA for 1 epoch.
- **Evaluation**: Human-centered evaluation focused on academic tone, fluency, and coherence.

## 📈 Results

- GPT-2 showed improvement in tone but struggled with coherence and syntax.
- Mistral-7B was more fluent but often produced generic or shallow content.
- Both models suffered from hallucinations and logical inconsistencies.

## 💡 Key Insights

- Light fine-tuning alone is insufficient for high-quality academic generation.
- Parameter-efficient methods like QLoRA can adapt larger models with limited resources.
- Evaluation must be human-centered to assess stylistic and logical performance.

## 🚀 Future Work

- Use full 2.7M arXiv dataset
- Experiment with more powerful base models (e.g., Mixtral, Deepseek)
- Introduce retrieval-augmented generation and citation grounding

## 📎 Report

👉 [Final Project Report (PDF)](./ECS%20271%20Final%20Project%20Report.pdf)
