import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

print("Torch version:", torch.__version__)
print("MPS available:", torch.backends.mps.is_available())

model_name = "microsoft/Phi-3-mini-4k-instruct"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("Model loaded.")

prompt = "Say hello in one sentence."

inputs = tokenizer(prompt, return_tensors="pt")

# Move to device
device = model.device
inputs = {k: v.to(device) for k, v in inputs.items()}

print("Generating...")

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        temperature=0.2,
        do_sample=False
    )

response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Response:")
print(response)