import dspy, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configure DSPy to use local Ollama model
lm = dspy.LM(
    model="ollama/llama3",             
    api_base="http://localhost:11434"
)

dspy.configure(lm=lm)

from classes import dspy_insight_explanation

explain_obj = dspy_insight_explanation.InsightExplaination()

stats = """
BP abnormality rate among smokers: 62%
BP abnormality rate among non-smokers: 28%
Average BMI among smokers: 29.8
Average BMI among non-smokers: 24.1
"""

result = explain_obj(structured_stats=stats)

print(result.explaination)