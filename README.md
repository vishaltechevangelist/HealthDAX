# HealthDAX – AI Powered Healthcare Data Analytics Assistant

HealthDAX is an AI-powered analytics assistant designed to query and analyze healthcare datasets using Large Language Models (LLMs).
It enables users to ask natural language questions about healthcare data and receive structured insights generated through an AI-driven query pipeline.

The system combines **FastAPI, LLM inference, structured data pipelines, and a lightweight UI** to deliver intelligent healthcare analytics.

---

# Key Features

• Natural language query interface for healthcare datasets
• LLM-powered query generation and reasoning
• FastAPI backend for scalable API services
• Modular query pipeline architecture
• Dataset schema registry and validation
• Execution engine for structured analytics
• Logging and evaluation framework
• Containerized deployment with Docker

---

# System Architecture

User Query
↓
UI Interface
↓
FastAPI Backend
↓
Query Service
↓
Prompt Builder
↓
LLM Inference
↓
Query Pipeline
↓
Execution Engine
↓
Dataset Handler
↓
Structured Results

---

# Project Structure

```
healthdax/
│
├── app/
│   ├── api/                 # API routes and schemas
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   ├── core/                # Core configs and logging
│   │   ├── config.py
│   │   └── logging_config.py
│   │
│   ├── data_handler/        # Dataset loading and schema registry
│   │   ├── dataset_loader.py
│   │   └── schema_registry.py
│   │
│   ├── llm/                 # LLM inference and prompt generation
│   │   ├── inference.py
│   │   ├── hf_model_inference.py
│   │   └── prompt_builder.py
│   │
│   ├── pipelines/           # Query processing pipeline
│   │   ├── query_pipeline.py
│   │   └── execution_engine.py
│   │
│   ├── services/            # Business logic services
│   │   ├── query_service.py
│   │   ├── validation_service.py
│   │   └── cache_service.py
│   │
│   ├── utils/               # Utility modules
│   │   └── logger.py
│   │
│   └── main.py              # FastAPI application entrypoint
│
├── data/                    # Healthcare datasets
│
├── logs/                    # Application logs
│
├── scripts/                 # Evaluation and query generation scripts
│
├── ui.py                    # User interface
│
├── Dockerfile               # Container configuration
├── run.sh                   # Application start script
├── requirements.txt         # Python dependencies
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/healthdax.git
cd healthdax
```

---

# Create Python Environment

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```
MODEL_PATH=<local_or_hf_model>
DATASET_PATH=./data
LOG_LEVEL=INFO
```

---

# Running the Application (Local)

Start the backend server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at:

```
http://localhost:8000
```

Interactive API docs:

```
http://localhost:8000/docs
```

---

# Running the UI

```
python ui.py
```

---

# Running with Docker

Build container:

```bash
docker build -t healthdax .
```

Run container:

```bash
docker run -p 8000:8000 healthdax
```

---

# Example API Request

POST request:

```
POST /query
```

Example body:

```
{
  "query": "What is the average age of patients with diabetes?"
}
```

Example response:

```
{
  "success": true,
  "result": "Average age of diabetes patients is 54.2 years"
}
```

---

# Evaluation Scripts

Evaluation scripts help measure query accuracy and pipeline performance.

Generate test queries:

```
python scripts/query_gen.py
```

Run evaluation:

```
python scripts/evaluate_execution.py
```

---

# Logging

Logs are stored in:

```
logs/app.log
logs/error.log
```

Logging configuration is defined in:

```
app/core/logging_config.py
```

---

# Deployment Options

HealthDAX can be deployed on:

• Hugging Face Spaces
• AWS EC2
• Docker containers
• Kubernetes clusters
• Local inference servers

---

# Use Cases

Healthcare analytics assistant
Clinical dataset exploration
Medical research data querying
AI-powered BI interface for healthcare

---

# Future Improvements

• Retrieval Augmented Generation (RAG) integration
• Multi-dataset support
• SQL generation pipeline
• Vector database integration
• Authentication and user management
• Production monitoring and observability

---

# License

MIT License

---

# Author

Vishal Saxena
Applied Data Science & AI – IIT Delhi
