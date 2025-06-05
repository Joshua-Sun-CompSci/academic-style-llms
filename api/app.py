from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import gradio as gr

# model_name = "markteammate/Mistral_academic_style_tune"

# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

model_name = "gpt2"  # or your own fine-tuned GPT-2 model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_academic_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

gr.Interface(
    fn=generate_academic_text,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt..."),
    outputs="text",
    title="📚 Academic Style Generator",
    description="Enter a prompt and generate text in academic tone using a Mistral fine-tuned model."
).launch()
