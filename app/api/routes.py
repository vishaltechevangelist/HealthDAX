from fastapi import APIRouter
from app.data_handler.schema_registry import schema_registry
# from app.pipelines.execution_engine import execution_engine
from app.services.query_service import query_service

router = APIRouter()

@router.get("/health")
def health_check():
    return {'status':'Ok', }

@router.get('/schema')
def get_schema():
    return schema_registry.get_schemas()

@router.get('/test-execution')
def test_execution():
    structured_query = {
        "filters": [
            {"column": "Sex", "operator": "==", "value": 1},
            {"column": "Blood_Pressure_Abnormality", "operator": "==", "value": 1}
        ],
        "groupby": [],
        "metrics": [
            {"column": "Patient_Number", "aggregation": "count"}
        ]
    }
    # return execution_engine.execute(structured_query)
    return query_service.process(structure_query=structured_query)



