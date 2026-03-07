import pandas as pd
from app.core.config import get_settings

class DatasetLoader:
    def __init__(self):
        self._df = None

    def load(self):
        if self._df is None:
            self._df = pd.read_excel(settings.DATASET_FILE_PATH)
            # print(f"{self._df}")
            self._df = self.handle_missing_values()
            # print(f"{self._df}")
        return self._df
    
    def handle_missing_values(self):
        df = self._df.copy()
        df.loc[(['Sex'] == 0) & (df['Pregnancy'].isnull()), 'Pregnancy'] = 0
        df.loc[(['Sex'] == 0) & (df['Pregnancy'].isnull()), 'Pregnancy'] = 1
        
        df['alcohol_consumption_per_day'] = df['alcohol_consumption_per_day'].fillna(0)

        median_GPC = df['Genetic_Pedigree_Coefficient'].median()
        df['Genetic_Pedigree_Coefficient'] = df['Genetic_Pedigree_Coefficient'].fillna(median_GPC)
        return df

    def get_columns(self):
        df = self.load()
        # print(f"{df.columns}")
        return list(df.columns)

settings = get_settings()
dataset_loader = DatasetLoader() 