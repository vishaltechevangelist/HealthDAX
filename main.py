import pandas as pd
import scipy.stats as stats
import dspy

lm = dspy.LM(
    model="ollama/llama3",             
    api_base="http://localhost:11434"
)

dspy.configure(lm=lm)

from config import DATASET1_SCHEMA, DATASET2_SCHEMA, RELATIONSHIP
from classes import dspy_insight_explanation
#from helpers import execute_structured_query, aggregate_activity

def aggregate_activity(df2):
    activity = (
        df2.groupby("patient_number")["physical_activity_steps_per_day"]
        .mean()
        .reset_index()
        .rename(columns={"physical_activity_steps_per_day": "avg_steps"})
    )
    return activity


def execute_structured_query(datasets, query):
    df = datasets[query["datasets"][0]]

    # Join if needed
    if query.get("join"):
        right_df = datasets[query["join"]["right"]]
        df = df.merge(right_df, on=query["join"]["on"])

    # Filters
    for f in query.get("filters", []):
        col, op, val = f["column"], f["operator"], f["value"]
        if op == "==":
            df = df[df[col] == val]
        elif op == ">":
            df = df[df[col] > val]
        elif op == "<":
            df = df[df[col] < val]

    # Aggregation
    result = getattr(
        df.groupby(query["groupby"])[query["metric_column"]],
        query["aggregation"]
    )()

    return result


df1 = pd.read_excel('/Users/vishalsaxena/Documents/DS_Workspace/healthdax/data/raw/Health Dataset 1.xlsm')
df2 = pd.read_excel('/Users/vishalsaxena/Documents/DS_Workspace/healthdax/data/raw/Health Dataset 2.xlsm')

df1 = df1.rename(columns={
    "Patient_Number": "patient_number",
    "Blood_Pressure_Abnormality": "blood_pressure_abnormality",
    "Level_of_Hemoglobin": "level_of_hemoglobin",
    "Genetic_Pedigree_Coefficient*": "genetic_pedigree_coefficient",
    "Age": "age",
    "BMI": "bmi",
    "Sex": "sex",
    "Pregnancy": "pregnancy",
    "Smoking": "smoking",
    "Level_of_Stress  (Cortisol Secretion)": "level_of_stress",
    "Chronic_kidney_disease": "chronic_kidney_disease",
    "Adrenal_and_thyroid_disorders": "adrenal_thyroid_disorders"
})

df2 = df2.rename(columns={
    "Patient_Number": "patient_number",
    "Day_Number": "day_number",
    "Physical_activity": "physical_activity_steps_per_day"
})

# Aggregate dataset2
activity_df = aggregate_activity(df2)

# Prepare datasets dictionary
datasets = {
    "dataset1": df1,
    "activity": activity_df
}


# -----------------------------
# 2. Example Structured Query
# -----------------------------
query = {
    "datasets": ["dataset1", "activity"],
    "join": {
        "right": "activity",
        "on": "patient_number"
    },
    "filters": [],
    "groupby": "smoking",
    "metric_column": "chronic_kidney_disease",
    "aggregation": "mean"
}

result = execute_structured_query(datasets, query)

print("\n=== Aggregated Result ===")
print(result)

explain_obj = dspy_insight_explanation.InsightExplaination()
result = explain_obj(structured_stats=result)

print("\n=== LLM Explanation ===")
print(result.explanation)