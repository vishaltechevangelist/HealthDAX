from app.data_handler.dataset_loader import dataset_loader

class SchemaRegistry:
    def __init__(self):
        self.columns = dataset_loader.get_columns()

    def get_schemas(self):
        return {'columns': self.columns}
    
schema_registry = SchemaRegistry()