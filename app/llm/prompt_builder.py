from app.data_handler.schema_registry import schema_registry

class PromptBuilder:
    def build(self, user_query:str)->str:
        schema = schema_registry.get_schemas()
        prompt = f"""
            You are a healthcare analytics assistant.

            Available columns:
            {schema["columns"]}

            Convert the user query into this JSON format:

            {{
            "filters": [{{"column": "", "operator": "", "value": ""}}],
            "groupby": [],
            "metrics": [{{"column": "", "aggregation": ""}}]
            }}

            Rules:
            - Use only available columns.
            - Allowed operators: ==, !=, >, <, >=, <=
            - Allowed aggregations: count, sum, mean
            - Return ONLY valid JSON.
            - Do not explain anything.
            - For sex: use 1 for female, 0 for male.
            - For blood_pressure_abnormality: use 1 for abnormal, 0 for normal.

            User Query:
            {user_query}"""
        return prompt
    
prompt_builder = PromptBuilder()