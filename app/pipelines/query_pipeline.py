from app.pipelines.execution_engine import execution_engine
from app.llm.prompt_builder import prompt_builder
from app.llm.inference import ollama_client
from app.llm.hf_model_inference import hf_client
import json, time, logging
from app.services.validation_service import validation_service

logger = logging.getLogger(__name__)

class QueryPipeline:
    def run_structured(self, structured_query:dict):
        start = time.time()
        structured_query = validation_service.validate(structured_query=structured_query) 
        result = execution_engine.execute(structured_query=structured_query)
        end = time.time()
        return result, structured_query, (end - start)*1000
    
    def run_natural_language(self, user_query:str):
        start = time.time()
        prompt = prompt_builder.build(user_query=user_query)
        llm_response = ollama_client.generate(prompt=prompt)
        query_json = json.loads(llm_response)
        query_json = validation_service.validate(query_json)
        result = execution_engine.execute(query_json)
        end = time.time()
        return result, query_json, (end-start)*1000
    
    def run_natural_language_hf(self, user_query:str):
        start = time.time()
        # logger.info(f"user query {user_query}")
        prompt = prompt_builder.build_hf_prompt(user_query=user_query)
        # logger.info(f"prompt {prompt}")
        llm_response = hf_client.generate(prompt=prompt)
        # logger.info(f"raw response ====== {llm_response}")
        query_json = json.loads(llm_response)
        query_json = validation_service.validate(query_json)
        result = execution_engine.execute(query_json)
        end = time.time()
        return result, query_json, (end-start)*1000

    
query_pipeline = QueryPipeline()