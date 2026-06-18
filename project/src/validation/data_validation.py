from pydantic import BaseModel, model_validator
from typing import Union, List

from pathlib import Path
from hydra.utils import get_original_cwd
import polars as pl

import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s-%(asctime)s-%(message)s')
logger= logging.getLogger(__name__)

class DataValidation(BaseModel):
    dataset: str
    target: str
    features: Union[List[str], None]
    
    @model_validator(mode='after')
    def data_validation(self): 
        path= Path(get_original_cwd())
        self.dataset= path / 'project' / 'config' / 'data' / 'raw' / self.dataset
        
        if not self.dataset.exists(): 
            logger.error(f'File {self.dataset.name} doesnt exist in {self.dataset}')
            raise FileNotFoundError(f'File {self.dataset.name} doesnt exist in {self.dataset}')
        if self.dataset.suffix != '.csv': 
            logger.error(f'File {self.dataset.name} should be a .csv')
            raise ValueError(f'File {self.dataset.name} should be a .csv')
        
        columns= pl.read_csv(self.dataset, n_rows=10, null_values=['tbd', 'TBD', 'N/A', 'nan'], separator=';').columns
        
        if self.target not in columns: 
            logger.error(f'Column {self.target} should be in the dataframe. Available columns:\n{columns}')
            print(columns)
            raise ValueError(f'Column {self.target} should be in the dataframe. Available columns:\n{columns}')
        
        features= self.features
        if features is None: 
            self.features= [col for col in columns if col != self.target]
        else: 
            for col in features:
                if col not in columns:
                    logger.error(f'Column {self.target} should be in the dataframe.\nAvailable columns:{columns}')
                    raise ValueError(f'Column {self.target} should be in the dataframe.\nAvailable columns:{columns}')
        
        return self



