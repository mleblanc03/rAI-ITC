import pandas as pd
import numpy as np
from pathlib import Path
from dateutil.parser import parse
from collections import Counter
from memory_profiler import profile

# Define a class for converting data types
class DataTypeConverter:
    def __init__(self, file_path: str, schema: dict = None):
        self.file_path = Path(file_path)  # Convert file path to Path object
        self.df = None  # Initialize DataFrame
        # Define default values for different data types
        self.default_values = {
            'datetime64[ns]': pd.Timestamp('1970-01-01'),
            'Int64': 0,
            'Float64': 0.0,
            'boolean': np.NaN,
            'string': np.NaN,
            'category': np.NaN,
        }
        self.schema = schema  # Initialize schema

    # Load data from file
    def load_data(self, nrows:int =None):
        # Check file extension and load data accordingly
        if self.file_path.suffix == '.csv':
            self.df = pd.read_csv(self.file_path, nrows=nrows).convert_dtypes()
        elif self.file_path.suffix == '.xlsx':
            self.df = pd.read_excel(self.file_path, nrows=nrows).convert_dtypes()
        else:
            raise ValueError("Unsupported file format")
    
    # Infer schema from data
    def infer_schema(self):
        schema = {}
        for col in self.df.columns:
            # Check for mixed data types in string columns
            if self.df[col].dtype == 'string':
                most_freq_type = self._get_most_freq_type(self.df[col])
                schema[col] = most_freq_type
                # Convert string columns with few unique values to category
                if most_freq_type == 'string':
                    n_unique = self.df[col].nunique()
                    if n_unique < 0.5 * len(self.df):
                        schema[col] = 'category'
            else:
                schema[col] = str(self.df[col].dtype)
        self.schema = schema
        return schema
    
    # Convert columns to inferred data types
    def convert(self):
        if self.schema is None:
            self.infer_schema()

        for col in self.df.columns:
            dtype = self.schema[col]

            # Convert column to appropriate data type
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

    # Check if a string can be parsed as a date
    def _is_date(self, string:str) -> bool:
        if string.isdigit():
                return False
        try:
            parse(string, ignoretz=True)
            return True
        except ValueError:
            return False
              
    # Infer data type from a string
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
    
    # Get the most frequent data type in a series
    def _get_most_freq_type(self, series:pd.Series) -> str:
        types = series.dropna().map(self._get_type_from_str)
        if types.empty:
            return None
        most_freq_type = Counter(types).most_common(1)[0][0]
        return most_freq_type    
        
    # Save DataFrame to file
    def save_data(self, output_path:str):
        output_path = Path(output_path)
        # Check file extension and save data accordingly
        if output_path.suffix == '.csv':
            self.df.to_csv(output_path, index=False)
        elif output_path.suffix == '.xlsx':
            self.df.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported output format")

    # Process data
    def process_data(self, output_path:str):
        self.load_data()
        self.infer_schema()
        self.convert()
        self.save_data(output_path)