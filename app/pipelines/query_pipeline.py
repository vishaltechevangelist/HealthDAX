from app.pipelines.execution_engine import execution_engine
from app.llm.prompt_builder import prompt_builder
from app.llm.inference import ollama_client
import json
from app.services.validation_service import validation_service

class QueryPipeline:
    def run_structured(self, structured_query:dict):
        structured_query = validation_service.validate(structured_query=structured_query) 
        result = execution_engine.execute(structured_query=structured_query)
        return result
    
    def run_natural_language(self, user_query:str):
        prompt = prompt_builder.build(user_query=user_query)
        llm_response = ollama_client.generate(prompt=prompt)
        query_json = json.loads(llm_response)
        query_json = validation_service.validate(query_json)
        return execution_engine.execute(query_json)
    
query_pipeline = QueryPipeline()