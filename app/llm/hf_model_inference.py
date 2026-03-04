import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class HFModelClient:

    def __init__(self):
        model_name = "microsoft/Phi-3-mini-4k-instruct"

        print("Loading HF model...")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            dtype=torch.float16,
            device_map="auto"
        )

        print("HF model loaded.")

    def generate(self, prompt: str) -> str:

        inputs = self.tokenizer(prompt, return_tensors="pt")

        device = self.model.device
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=False
            )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
        return response


hf_client = HFModelClient()