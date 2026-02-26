# HealthDAX -- GenAI Powered Healthcare Data Insight System

## Overview

HealthDAX is an end-to-end GenAI-driven healthcare analytics system that
converts **natural language queries** into executable **Pandas
operations**, processes structured datasets, and returns interpretable
health insights using a local LLM (LLaMA via Ollama).

This project demonstrates:

-   Schema-aware query understanding
-   Natural Language -> Structured JSON query conversion
-   Secure Pandas execution layer
-   LLM-based explanation generation 
-   Modular and extensible architecture

------------------------------------------------------------------------

## Architecture Overview

**User Query (Natural Language - English)** -> **LLM (LLaMA via Ollama)|** -> **Structured JSON Query have pandas clauses** -> **Query Executor** -> **Computed Result** -> **LLM Explanation Generator** -> **Final Insight Response**

------------------------------------------------------------------------

## Project Structure
healthdax\
├── app.py\
├── classes\
│   └── dspy_insight_explanation.py
├── config.py
├── data\
│   ├── processed\
│   │   └── patient_health_data.csv
│   └── raw\
│       ├── Health Dataset 1.xlsm
│       └── Health Dataset 2.xlsm
├── helpers\
│   └── helper_functions.py
├── notebooks\
│   ├── create_schema_llm.ipynb
│   ├── explore-dataset.ipynb
│   └── explore_pandasai.ipynb
├── requirements.txt
└── test\
    ├── llm_request.py
    ├── test_nl2pd_query.py
    ├── test_ollama_dspy.py
    └── test_pandas.py

------------------------------------------------------------------------

## Steps for running the project (macOS/Linux)

### 1. Create Virtual Environment and activate it

-   python3 -m venv venv
-   source venv/bin/activate

### 2. Clone repository (ask for datasets from authorised entity/person)

-   git clone https://github.com/your-username/healthdax.git
-   cd healthdax
-   mkdir -p data 
    #### Copy your dataset files manually into /data folder

### 3. Install dependencies

-   pip install --upgrade pip
-   pip install -r requirements.txt

### 4. Ollama Setup 

#### macOS
-    brew install ollama
-    ollama serve
-    ollama pull llama3
-    ollama run llama3
-    http://localhost:11434 (default url)

### 5. Update config.py variables as per required setup

####  Dataset file path (absolute or relative)
-   DATASET_FILE_PATH = "data/dataset1.xlsx"

#### LLM Model Name
-   LLM_MODEL_NAME = "llama3"

#### LLM Server URL
-   LLM_SRV_URL = "http://localhost:11434"

#### 6. Start streamlit app

-   streamlit run app.py
-   http://localhost:8501 (HealthDAX url will be open in browser)

------------------------------------------------------------------------

## Key Components

### 1. Schema Loader

-   Loads dataset metadata
-   Provides column awareness to LLM
-   Ensures safe query generation

### 2. Query Generator from LLM

-   Converts natural language into structured JSON format
-   Handles:
    -   Filters
    -   Aggregations
    -   GroupBy
    -   Joins
    -   Metrics

Example JSON:

{ "datasets": ["dataset1"], "filters": [ {"column": "sex",
"operator": "==", "value": 0} ], "groupby": [], "metrics": [
{"column": "age", "operation": "mean"} ] }

------------------------------------------------------------------------

### 3. Query Executor

-   Executes structured JSON safely
-   Avoids unsafe `exec()` usage
-   Supports:
    -   Filtering
    -   Aggregation
    -   Grouping
    -   Joins

------------------------------------------------------------------------

### 4. Explanation Generator

-   Sends computed results back to LLaMA
-   Produces human-readable healthcare insights

Example Output:

The total count of female patients is **992**, which represents the number of women who have been counted in our dataset.

------------------------------------------------------------------------

## Sample Query

Question: What are the total count of female patients?

Pipeline: - LLM generates structured JSON - Pandas executes query -
Result sent back to LLM for explanation

------------------------------------------------------------------------

## Design Principles

-   No direct execution of LLM-generated Python code
-   Structured intermediate representation (JSON)
-   Schema-aware validation
-   Easily extensible for Streamlit deployment

------------------------------------------------------------------------

## Future Enhancements

-   Add validation layer for production safety
-   Deploy using Streamlit Cloud
-   Add dashboard visualizations
-   Add healthcare risk prediction models

------------------------------------------------------------------------

## Tech Stack

-   Python
-   Pandas
-   DSPy (optional)
-   Ollama
-   LLaMA 3
-   Streamlit (planned deployment)

------------------------------------------------------------------------

## Author

Vishal Saxena\
Applied Data Science \| Healthcare AI\
Aspiring Data Scientist -- Healthcare Domain
