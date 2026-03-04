from app.pipelines.query_pipeline import query_pipeline
import logging, traceback

logger = logging.getLogger(__name__)

class QueryService:
    def process_structured(self, structured_query:dict):
        try:
            logger.info(f"Received structured_query : {structured_query}")
            result, structured_query, exec_time = query_pipeline.run_structured(structured_query=structured_query)
            logger.info(f"Execution Result : {result}")
            logger.info(f"Execution Time : {exec_time}")
            return {
                "success": True,
                "data": result,
                "structured_query": structured_query,
                "execution_time": exec_time
            }
        except Exception as e:
            logger.error(f"Error in structured query: {str(e)}")
            traceback.print_exc()
            return {"error":str(e), "success":False}
    
    def process_natural_language(self, user_query:str):
        try:
            logger.info(f"Received structured_query : {user_query}")
            result, structured_query, exec_time = query_pipeline.run_natural_language(user_query=user_query)
            logger.info(f"Execution Result : {result}")
            logger.info(f"Execution Time : {exec_time}")
            return {
                "success": True,
                "data": result,
                "structured_query": structured_query,
                "execution_time": exec_time
            }
        except Exception as e:
            logger.error(f"Error in NL (here) query: {str(e)}")
            traceback.print_exc()
            return {"error":str(e), "success":False}
        
    def process_natural_language_hf(self, user_query:str):
        try:
            logger.info(f"Received structured_query : {user_query}")
            result, structured_query, exec_time = query_pipeline.run_natural_language_hf(user_query=user_query)
            logger.info(f"Execution Result : {result}")
            logger.info(f"Execution Time : {exec_time}")
            return {
                "success": True,
                "data": result,
                "structured_query": structured_query,
                "execution_time": exec_time
            }
        except Exception as e:
            logger.error(f"Error in NL HF query: {str(e)}")
            traceback.print_exc()
            return {"error":str(e), "success":False}
    
query_service = QueryService()