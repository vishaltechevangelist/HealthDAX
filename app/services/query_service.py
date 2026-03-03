from app.pipelines.query_pipeline import query_pipeline

class QueryService:
    def process_structured(self, structured_query:dict):
        try:
            return query_pipeline.run_structured(structured_query=structured_query)
        except Exception as e:
            return {"error":str(e)}
    
    def process_natural_language(self, user_query:str):
        try:
            return query_pipeline.run_natural_language(user_query=user_query)
        except Exception as e:
            return {"error":str(e)}
    
query_service = QueryService()