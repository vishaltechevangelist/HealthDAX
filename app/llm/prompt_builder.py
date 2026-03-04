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
            - Do not share more example
            - Do not do few shot learning

            User Query:
            {user_query}"""
        return prompt
    
    def build_hf_prompt(self, user_query):
        schema = schema_registry.get_schemas()["columns"]

        system_message = f"""
            You are a healthcare analytics assistant.

            You MUST return ONLY valid JSON.

            The JSON must follow EXACTLY this schema:

            {{
            "filters": [{{"column": "", "operator": "", "value": ""}}],
            "groupby": [],
            "metrics": [{{"column": "", "aggregation": ""}}]
            }}

            Rules:
            - Do NOT invent new fields.
            - Only use these keys: filters, groupby, metrics.
            - Use only available columns.

            Available columns:
            {schema}

            Operators allowed:
            ==, !=, >, <, >=, <=

            Aggregations allowed:
            count, sum, mean

            Return JSON only.
            No explanations.
            """

        user_message = f"""
                Example:

                User Query:
                count male patients

                JSON:
                {{
                "filters": [{{"column": "Sex", "operator": "==", "value": "0"}}],
                "groupby": [],
                "metrics": [{{"column": "Patient_Number", "aggregation": "count"}}]
                }}

                Now convert this query:

                {user_query}
                """
        return [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]        
    
prompt_builder = PromptBuilder()