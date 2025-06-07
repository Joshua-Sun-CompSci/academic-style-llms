import os
import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel

# Get token from HF Space secret
hf_token = os.environ.get("HF_TOKEN")

# Adapter repo and base model
adapter_model = "markteammate/Mistral_academic_style_tune"
base_model = "mistralai/Mistral-7B-v0.1"

# Quantization config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4"
)

# Load tokenizer and base model with token (no login())
tokenizer = AutoTokenizer.from_pretrained(base_model, token=hf_token, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

base = AutoModelForCausalLM.from_pretrained(
    base_model,
    token=hf_token,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True
)

# Apply LoRA adapter
model = PeftModel.from_pretrained(base, adapter_model, token=hf_token)
model.eval()

def generate_academic_text(title, max_tokens=150, temperature=0.7):
    torch.cuda.empty_cache()
    title = title.strip()
    prompt = f"""### Instruction:
Write an academic paragraph given the title.

### Input: {title}

### Response:
"""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=temperature,
            do_sample=True,
            top_p=0.95,
        )
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract only the part after ### Response:
    if "### Response:" in decoded:
        return decoded.split("### Response:")[1].strip()
    else:
        return decoded.strip()

gr.Interface(
    fn=generate_academic_text,
    inputs=[
        gr.Textbox(lines=4, placeholder="Enter an academic topic or prompt...", label="Prompt"),
        gr.Slider(20, 512, value=150, step=10, label="Max Tokens"),
        gr.Slider(0.1, 1.5, value=0.7, step=0.1, label="Temperature"),
    ],
    outputs="text",
    title="🎓 Academic Style Text Generator",
    description="Generate academic-style text using Mistral-7B + LoRA. GPU + HF_TOKEN required.",
).launch()
