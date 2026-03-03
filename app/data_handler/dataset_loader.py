import pandas as pd
from app.core.config import get_settings

class DatasetLoader:
    def __init__(self):
        self._df = None

    def load(self):
        if self._df is None:
            self._df = pd.read_excel(settings.DATASET_FILE_PATH)
        return self._df

    def get_columns(self):
        df = self.load()
        return list(df.columns)

settings = get_settings()
dataset_loader = DatasetLoader() 