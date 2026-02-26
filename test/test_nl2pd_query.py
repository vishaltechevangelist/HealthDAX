import dspy, sys, os, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DATASET1_SCHEMA, DATASET2_SCHEMA, RELATIONSHIP

# Configure DSPy to use local Ollama model
lm = dspy.LM(
    model="ollama/llama3",             
    api_base="http://localhost:11434",
    temperature=0,
    top_p=1
)

dspy.configure(lm=lm)

from classes import dspy_insight_explanation

schema_bundle = {
    "dataset1": DATASET1_SCHEMA,
    "dataset2": DATASET2_SCHEMA,
    "relationship": RELATIONSHIP
}

schema_str = json.dumps(schema_bundle, indent=2)

query_obj = dspy_insight_explanation.PandasQueryGenerator()

# question = """What is the average age of patients"""
# question =  """Who is more chronic male or female """
# question = """Find patient who walks less than 20000 daily"""
# question = "what is the count of male patients"
# question = "Find health data of patients whose age less than 45"
question = "How many patient walks for 10 days"


result = query_obj(input_query=question, schema_str=schema_str)

print(result.output_json)
