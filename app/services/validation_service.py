from app.data_handler.schema_registry import schema_registry

class ValidationService:
    ALLOWED_OPERATORS = {"==", "!=", ">", "<", ">=", "<="}
    ALLOWED_AGGREGATION = {"count", "sum", "mean"}

    def validate(self, structured_query:dict):
        schema_column = schema_registry.get_schemas()['columns']

        for fil in structured_query.get('filters', []):
            if fil['column'] not in schema_column:
                raise ValueError(f"Invalid Column in filter: {fil['column']}")
            
            if fil['operator'] not in self.ALLOWED_OPERATORS:
                raise ValueError(f"Invalid Operator {fil['operator']}")
            
            for met in structured_query.get('metrics', []):
                if met['column'] not in schema_column:
                    raise ValueError(f"Invalid column {met['column']}")
                
                if met['aggregation'] not in self.ALLOWED_AGGREGATION:
                    raise ValueError(f"Invalid aggregation {met['aggregation']}")
                
            return structured_query
        
validation_service = ValidationService()