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

        import torch

        if torch.backends.mps.is_available():
            torch.mps.empty_cache()

        inputs = self.tokenizer.apply_chat_template(
            prompt,
            return_tensors="pt",
            add_generation_prompt=True
        )

        device = self.model.device
        inputs = {k: v.to(device) for k, v in inputs.items()}

        prompt_length = inputs["input_ids"].shape[1]

        with torch.inference_mode():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=500,
                do_sample=False,
                use_cache=True,
                pad_token_id=self.tokenizer.eos_token_id
            )

        response = self.tokenizer.decode(
            outputs[0][prompt_length:],
            skip_special_tokens=True
        )

        return response.strip("`json").strip()

hf_client = HFModelClient()