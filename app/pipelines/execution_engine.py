from app.data_handler.dataset_loader import dataset_loader
from app.utils.logger import logger

class ExecutionEngine:
    def __init__(self):
        self.df = dataset_loader.load()

    def apply_filters(self, df, filters):

        for f in filters:
            col = f['column']
            op = f['operator']

            if f['value'] is not None and f['value'] != '':
                val = int(f['value'])
                # logger.info("I am inside filter")
                if op == '==':
                    df = df[df[col] == val]
                elif op == '!=':
                    df = df[df[col] == val]
                elif op == '>':
                    df = df[df[col] > val]
                elif op == '<':
                    df = df[df[col] < val]
                elif op == '>=':
                    df = df[df[col] >= val]
                elif op == '<=':
                    df = df[df[col] <= val]
                else:
                    raise ValueError(f"Unsupported Error {op}")
        
        return df
    
    def apply_aggregation(self, df, groupby, metrics):
        if groupby:
            grouped = df.groupby(groupby)
        else:
            grouped = df

        results = {}

        for m in metrics:
            col = m["column"]
            agg = m["aggregation"]
            
            # print(f"Col -- {col}, Agg -- {agg}")
            if agg == "count":
                value = grouped[col].count()
            elif agg == "sum":
                value = grouped[col].sum()
            elif agg == "mean":
                value = grouped[col].mean()
            else:
                raise ValueError(f"Unsupported aggregation: {agg}")
            
            if hasattr(value, "item"):
                value = value.item()

            results[f"{agg}_{col}"] = value

        return results
    
    def execute(self, structured_query):
        df = self.df.copy()
        
        filters = structured_query.get('filters', [])
        groupby = structured_query.get('groupby', [])
        metrics = structured_query.get('metrics', [])

        df = self.apply_filters(df, filters=filters)
        
        result = self.apply_aggregation(df, groupby=groupby, metrics=metrics)

        return result
    

execution_engine = ExecutionEngine()