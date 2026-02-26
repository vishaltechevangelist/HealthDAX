import dspy

"""
    Role - You are expert to generate different query clause which will used in pandas from english queries
    Goal - Given database schemas in json format and relationship between those schemas, return json response comprises keys as below, along with correct & valid SQL queries - 
        "datasets": schemas list required to query
        "join": join if more than one schema is required with identifier 
        "filters": condition on column with operator along with values could be available in schemas
        "groupby": group clause on schema columns
        "metric_column": selected column clause
        "aggregation": aggregation clause with columns list
        "sql": Correct & valid equivalent SQL query
    Constraint - Use only given schema column and return json response only
"""

class PandasQueryStruct(dspy.Signature):
    """
    Role - You are expert to generate different query clause which will used with pandas function 
    Goal - Given database schemas in json format and relationship between those schemas, return json response comprises keys as below, along with correct & valid SQL queries - 
        {
      "datasets": list[str],
      "join": {
        "left_dataset": str,
        "right_dataset": str,
        "type": "inner|left|right",
        "on" : str
      },
      "filters": list[{
          "column": str type should be keys of schema,
          "operator": "==|>|<|>=|<=",
          "value": int|true
      }],
      "groupby": list[str],
      "metrics": list[{
          "column": str type should be keys of schema,
          "aggregation": "count|sum|mean|min|max"
      }]
      "sql": Correct & valid equivalent SQL query to check the response against pandas clauses
    }
    Constraint - 
    - Use only given schema column and return json response only, 
    - don't change key names, don't add new keys, 
    """

    input_query = dspy.InputField(desc="User query in natural language often english language")
    schema_str = dspy.InputField(desc="Schemas & relation between schemas")
    output_json = dspy.OutputField(desc="JSON response with mentioned keys")
    # print(schema_str)


class PandasQueryGenerator(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.Predict(PandasQueryStruct)

    def forward(self, input_query, schema_str):
        # print(schema_str)
        # print(input_query)
        return self.generate(input_query=input_query, schema_str=schema_str)

class HealthInsightStruct(dspy.Signature):
    """
    Goal - Generate grounded health insights strictly from structured statistics
    Constraint - Do not introduce external medical knowledge
    """
    input_query = dspy.InputField(desc="User query in natural language often english language")
    structured_stats = dspy.InputField(desc="Stats in json format")
    explanation = dspy.OutputField(desc="A detailed, layman-friendly grounded explanation of the pandas query result as per the input query") 


class InsightExplaination(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.Predict(HealthInsightStruct)

    def forward(self, input_query, structured_stats):
        return self.generate(input_query=input_query, structured_stats=structured_stats)