from app.pipelines.execution_engine import execution_engine

class QueryPipeline:
    def run(self, structured_query:dict):
        result = execution_engine.execute(structured_query=structured_query)
        return result
    
query_pipeline = QueryPipeline()