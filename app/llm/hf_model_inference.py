import torch, logging
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig

logger = logging.getLogger(__name__)

class HFModelClient:

    def __init__(self):
        model_name = "microsoft/Phi-3-mini-4k-instruct"

        config = AutoConfig.from_pretrained(model_name)
        config.tie_word_embeddings = False
    
        print("Loading HF model...")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            dtype=torch.float16,
            device_map="auto"
        )

        print("HF model loaded.")

    def generate(self, prompt: str) -> str:

        inputs = self.tokenizer.apply_chat_template(
            prompt,
            return_tensors="pt",
            add_generation_prompt=True
        )

        device = self.model.device
        prompt_length = inputs["input_ids"].shape[1]
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=False
            )

        # logger.info(f"Prompt Length ----- {prompt_length}")
        response = self.tokenizer.decode(outputs[0][prompt_length:], skip_special_tokens=True)
        response = response.strip('`json')
        return response


hf_client = HFModelClient()