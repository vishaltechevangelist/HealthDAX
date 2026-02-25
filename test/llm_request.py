import requests

def query_to_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

print(query_to_llm("Explain why high BMI may correlate with blood pressure abnormalities."))