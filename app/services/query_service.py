from app.pipelines.query_pipeline import query_pipeline

class QueryService:
    def process_structured(self, structured_query:dict):
        return query_pipeline.run_structured(structured_query=structured_query)
    
    def process_natural_language(self, user_query:str):
        return query_pipeline.run_natural_language(user_query=user_query)
    
query_service = QueryService()