import streamlit as st
import pandas as pd

@st.cache_data
def load_datasets(dataset_schema_file, rename_col_dict):
    df = pd.read_excel(dataset_schema_file)
    df = df.rename(columns=rename_col_dict)
    return df


def execute_structured_query(datasets, query):
    
    df = datasets[query["datasets"][0]]
    # print(df)
    # sys.exit(0)
    
    if query.get("join") and query["join"]["right_dataset"] is not None and query["join"]["left_dataset"] is not None:
        right_df = datasets[query["join"]["right_dataset"]]
        df = df.merge(right_df, on=query["join"]["on"])
    
    for f in query.get("filters", []):
        col, op, val = f["column"], f["operator"], f["value"]
        val = int(val)
        # print(col, op, val)
        # st.dataframe(df.columns)
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
        if aggregate_function == 'count':
            if query["metrics"][0]["column"] is None or query["metrics"][0]["column"] == "":
                return len(df)
            else:
                return df[query["metrics"][0]["column"]].count()
        result = getattr(df[query["metrics"][0]["column"]], aggregate_function)()

    return result

def format_output(display_output):
    return f'<div style="background-color:#2b6cb0;color:white;border-left:6px solid #2196F3;padding:10px 16px;border-radius:8px;">{display_output}</div>'


def aggregate_activity(df2):
    activity = (
        df2.groupby("patient_number")["physical_activity_steps_per_day"]
        .mean()
        .reset_index()
        .rename(columns={"physical_activity_steps_per_day": "avg_steps"})
    )
    return activity