import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "gpt2"  # Update later with your fine-tuned model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_academic_text(prompt, max_tokens, temperature):
    if not prompt.strip():
        return "❗ Please enter a valid prompt."
    try:
        inputs = tokenizer(prompt.strip(), return_tensors="pt", truncation=True, max_length=512)
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=temperature,
        )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text[len(prompt):].strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

iface = gr.Interface(
    fn=generate_academic_text,
    inputs=[
        gr.Textbox(lines=5, placeholder="Enter a topic, sentence, or academic question...", label="Prompt"),
        gr.Slider(20, 300, value=100, step=10, label="Max New Tokens"),
        gr.Slider(0.1, 1.5, value=0.7, step=0.1, label="Temperature")
    ],
    outputs=gr.Textbox(label="Generated Academic Text"),
    title="📚 Academic Writing Generator",
    description=(
        "This demo showcases a GPT-based model fine-tuned to emulate academic writing style. "
        "Try entering an abstract idea or question, and explore how the model responds with scholarly tone."
    ),
    examples=[
        ["What are the main challenges of using deep learning in medicine?", 100, 0.7],
        ["Explain the impact of climate change on agricultural productivity.", 120, 0.8],
        ["Why is contrastive learning effective for representation learning?", 80, 0.6],
    ],
    theme="soft"
)

iface.launch()
