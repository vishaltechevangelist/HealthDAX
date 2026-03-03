from app.pipelines.query_pipeline import query_pipeline

class QueryService:
    def process(self, structure_query:dict):
        return query_pipeline.run(structured_query=structure_query)
    
query_service = QueryService()