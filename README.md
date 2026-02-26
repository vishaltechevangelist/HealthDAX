# HealthDAX -- GenAI Powered Healthcare Data Insight System

## Overview

HealthDAX is an end-to-end GenAI-driven healthcare analytics system that
converts **natural language queries** into executable **Pandas
operations**, processes structured datasets, and returns interpretable
health insights using a local LLM (LLaMA via Ollama).

This project demonstrates:

-   Schema-aware query understanding
-   Natural Language → Structured JSON query conversion
-   Secure Pandas execution layer
-   LLM-based explanation generation 
-   Modular and extensible architecture

------------------------------------------------------------------------

## 🏗️ Architecture Overview

User Query (Natural Language - English) -> LLM (LLaMA via Ollama) -> Structured JSON Query have pandas clauses -> Query Executor -> Computed Result\
-> LLM Explanation Generator -> Final Insight Response

------------------------------------------------------------------------

## Project Structure



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

{ "datasets": \["dataset1"\], "filters": \[ {"column": "sex",
"operator": "==", "value": 0} \], "groupby": \[\], "metrics": \[
{"column": "age", "operation": "mean"} \] }

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
