import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DATASET1_SCHEMA_RENAME, DATASET2_SCHEMA_RENAME

dataset1 = pd.read_excel('/Users/vishalsaxena/Documents/DS_Workspace/healthdax/data/raw/Health Dataset 1.xlsm')
dataset2 = pd.read_excel('/Users/vishalsaxena/Documents/DS_Workspace/healthdax/data/raw/Health Dataset 2.xlsm')

dataset1 = dataset1.rename(columns=DATASET1_SCHEMA_RENAME)
dataset2 = dataset2.rename(columns=DATASET2_SCHEMA_RENAME)

# print(dataset1.head())
# print(dataset1.columns)

dataframes = {
        "dataset1": dataset1,
        "dataset2": dataset2
}

json_for_pandas = { 
  "datasets": ["dataset1", "dataset2"],
  "join": {
    "left_dataset": "dataset1",
    "right_dataset": "dataset2",
    "type": "inner",
    "on": "patient_number",
  },
  "filters": [
    {
      "column": "physical_activity_steps_per_day",
      "operator": "<",
      "value": 5000
    }
  ],
  "groupby": [],
  "metrics": [],
  "sql": "SELECT * FROM dataset1 INNER JOIN dataset2 ON dataset1.patient_number = dataset2.patient_number WHERE dataset2.physical_activity_steps_per_day < 5000"
}

# json_for_pandas = {
#   "datasets": ["dataset1"],
#   "filters": [],
#   "groupby": [],
#   "metrics": [
#     {
#       "column": "age",
#       "aggregation": "mean"
#     }
#   ],
#   "sql": "SELECT AVG(age) FROM dataset1;"
# }

# json_for_pandas = {
#   "datasets": ["dataset1", "dataset2"],
#   "join": {
#     "left_dataset": "dataset1",
#     "right_dataset": "dataset2",
#     "type": "inner",
#     "on" : "patient_number"
#   },
#   "filters": [
#     {
#       "column": "physical_activity_steps_per_day",
#       "operator": "<",
#       "value": 20000
#     }
#   ],
#   "groupby": [],
#   "metrics": [],
#   "sql": "SELECT * FROM dataset1 INNER JOIN dataset2 ON dataset1.patient_number = dataset2.patient_number WHERE dataset2.physical_activity_steps_per_day < 20000"
# }

# json_for_pandas = {
#   "datasets": ["dataset1"],
#   "join": {
#     "left_dataset": "dataset1",
#     "right_dataset": None,
#     "type": "inner",
#     "on" : "patient_number"
#   },
#   "filters": [
#     {
#       "column": "age",
#       "operator": "<",
#       "value": 45
#     }
#   ],
#   "groupby": [],
#   "metrics": [],
#   "sql": "SELECT * FROM dataset1 WHERE age < 45"
# }

json_for_pandas = {
  "datasets": ["dataset1", "dataset2"],
  "join": {
    "left_dataset": "dataset1",
    "right_dataset": "dataset2",
    "type": "inner",
    "on" : "patient_number"
  },
  "filters": [],
  "groupby": ["patient_number", "day_number"],
  "metrics": [
    {
      "column": "physical_activity_steps_per_day",
      "aggregation": "count"
    }
  ],
  "sql": "SELECT COUNT(physical_activity_steps_per_day) FROM dataset1 INNER JOIN dataset2 ON patient_number WHERE day_number <= 10"
}

def execute_structured_query(datasets, query):
    df = datasets[query["datasets"][0]]
    # print(df)
    # sys.exit(0)
    
    if query.get("join") and query["join"]["right_dataset"] is not None:
        right_df = datasets[query["join"]["right_dataset"]]
        df = df.merge(right_df, on=query["join"]["on"])
    
    for f in query.get("filters", []):
        col, op, val = f["column"], f["operator"], f["value"]
        if op == "==":
            df = df[df[col] == val]
        elif op == ">":
            df = df[df[col] > val]
        elif op == "<":
            df = df[df[col] < val]

    if len(query['groupby'])==0 and len(query["metrics"])==0:
        return df
    elif len(query['groupby'])>0 and len(query["metrics"])>0:
        result = getattr(
            df.groupby(query["groupby"])[query["metrics"][0]["column"]],
            query["metrics"][0]["aggregation"]
        )()
    elif len(query['metrics'])>0 and len(query['groupby']) == 0:
        aggregate_function = query["metrics"][0]["aggregation"]
        result = getattr(df[query["metrics"][0]["column"]], aggregate_function)()

    return result

result = execute_structured_query(dataframes, json_for_pandas)
print(result)