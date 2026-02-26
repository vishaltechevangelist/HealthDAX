import streamlit as st
import pandas as pd
import dspy, sys, os, json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import LLM_MODEL_NAME, LLM_SRV_URL, DATASET_FILE1, DATASET_FILE2, DATASET1_SCHEMA, DATASET2_SCHEMA, RELATIONSHIP, DATASET_FILE_PATH
from config import DATASET_FILE_PATH, DATASET1_SCHEMA_RENAME, DATASET2_SCHEMA_RENAME
from helpers import helper_functions

@st.cache_resource
def get_configured_dspy_llm():
    try:
        lm = dspy.LM(model=LLM_MODEL_NAME, api_base=LLM_SRV_URL)
        dspy.settings.configure(lm=lm)
    except Exception as e:
        st.warning("LLM configuration failed. Ensure Ollama Llama3 is running.")
        st.error(str(e))
    return lm

lm = get_configured_dspy_llm()

from classes import dspy_insight_explanation

st.set_page_config(page_title="Healthcare GenAI System", layout="wide")
st.title("Healthcare GenAI System")

df1 = helper_functions.load_datasets(os.path.join(DATASET_FILE_PATH, DATASET_FILE1), DATASET1_SCHEMA_RENAME)
df2 = helper_functions.load_datasets(os.path.join(DATASET_FILE_PATH, DATASET_FILE2), DATASET2_SCHEMA_RENAME)
dataframes = {
        "dataset1": df1,
        "dataset2": df2
}

schema_bundle = {
    "dataset1": DATASET1_SCHEMA,
    "dataset2": DATASET2_SCHEMA,
    "relationship": RELATIONSHIP
}
schema_str = json.dumps(schema_bundle, indent=2)

# st.write("I am here")
# st.dataframe(df2.head())
# st.dataframe(df2.head())

st.subheader("Ask a Healthcare Question")
user_question = st.text_input(
    "Example: Are smokers more likely to have chronic kidney disease?"
)

if st.button("Run Analysis"):
    query_obj = dspy_insight_explanation.PandasQueryGenerator()
    result = query_obj(input_query=user_question, schema_str=schema_str)

    print(result.output_json)
    # sys.exit(0)
    query_result = helper_functions.execute_structured_query(dataframes, json.loads(result.output_json))
    # st.write(result.output_json)
    # print(query_result)
    # st.dataframe(query_result)
    # sys.exit(0)
    st.subheader("LLM Explanation")
    try:
        explain_obj = dspy_insight_explanation.InsightExplaination()
        llm_response = explain_obj(input_query=user_question, structured_stats=query_result)
        st.markdown(helper_functions.format_output(llm_response.explanation), unsafe_allow_html=True)
    except Exception as e:
        st.warning("LLM explanation failed. Ensure Ollama Llama3 is running.")
        st.error(str(e))