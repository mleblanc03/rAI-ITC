import pandas as pd
import numpy as np
from pathlib import Path
from dateutil.parser import parse
from collections import Counter
from memory_profiler import profile

class DataTypeConverter:
    def __init__(self, file_path: str, schema: dict = None):
        self.file_path = Path(file_path)
        self.df = None
        #TODO add as parameters in Analysis
        self.default_values = {
            'datetime64[ns]': pd.Timestamp('1970-01-01'),
            'Int64': 0,
            'Float64': 0.0,
            'boolean': np.NaN,
            'string': np.NaN,
            'category': np.NaN,
        }
        self.schema = schema
       
    def load_data(self, nrows:int =None):
        if self.file_path.suffix == '.csv':
            self.df = pd.read_csv(self.file_path, nrows=nrows).convert_dtypes()
        elif self.file_path.suffix == '.xlsx':
            self.df = pd.read_excel(self.file_path, nrows=nrows).convert_dtypes()
        else:
            raise ValueError("Unsupported file format")
    
    def infer_schema(self):
        schema = {}
        for col in self.df.columns:
            if self.df[col].dtype == 'string':
                # Check for mixed data types
                most_freq_type = self._get_most_freq_type(self.df[col])
                schema[col] = most_freq_type
                if most_freq_type == 'string':
                    n_unique = self.df[col].nunique()
                    if n_unique < 0.5 * len(self.df):
                        schema[col] = 'category'
            else:
                schema[col] = str(self.df[col].dtype)
        self.schema = schema
        return schema
    
    def convert(self):
        if self.schema is None:
            self.infer_schema()

        for col in self.df.columns:
            dtype = self.schema[col]

            match dtype:
                case 'datetime64[ns]':
                    self.df[col] = pd.to_datetime(self.df[col], errors='coerce')\
                        .fillna(self.default_values['datetime64[ns]'])
                case 'Int64':
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce')\
                        .fillna(self.default_values['Int64'])
                case 'Float64':
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce')\
                        .fillna(self.default_values['Float64'])
                case 'string':
                    self.df[col] = self.df[col].fillna(self.default_values['string'])
                case 'category':
                    self.df[col] = self.df[col].astype('category').fillna(self.default_values['category'])


    def _is_date(self, string:str) -> bool:
        if string.isdigit():
                return False
        try:
            parse(string, ignoretz=True)
            return True
        except ValueError:
            return False
              
    def _get_type_from_str(self, string:str) -> str:
        if self._is_date(string):
            return 'datetime64[ns]'
        try:
            int(string)
            return 'Int64'
        except ValueError:
            try:
                float(string)
                return 'Float64'
            except ValueError:
                return 'string'
    
    def _get_most_freq_type(self, series:pd.Series) -> str:
        types = series.dropna().map(self._get_type_from_str)
        if types.empty:
            return None
        most_freq_type = Counter(types).most_common(1)[0][0]
        return most_freq_type    
        
    def save_data(self, output_path:str):
        output_path = Path(output_path)
        if output_path.suffix == '.csv':
            self.df.to_csv(output_path, index=False)
        elif output_path.suffix == '.xlsx':
            self.df.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported output format")

    def process_data(self, output_path:str):
        self.load_data()
        self.infer_types()
        self.save_data(output_path)
