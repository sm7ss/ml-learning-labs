import hydra 
from omegaconf import DictConfig, OmegaConf
import polars as pl 
from pydantic import BaseModel, model_validator, Field, field_validator
from pathlib import Path
import psutil

from typing import Optional, Literal, Union, List
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s-%(asctime)s-%(message)s')
logger= logging.getLogger(__name__)

class DecisionTreeVal(BaseModel):
    name: Literal['decision_tree_classifier']= 'decision_tree_classifier'
    max_depth: Optional[int]
    min_sample_split: Optional[int]
    min_sample_leaf: Optional[int]
    class_weight: Optional[Literal['balanced']]

class DecisionTreeRegressor(BaseModel):
    name: Literal['decision_tree_regressor']= 'decision_tree_regressor'
    max_depth: Optional[int]
    min_sample_split: Optional[int]
    min_sample_leaf: Optional[int]

class RandomForest(BaseModel):
    name: Literal['random_forest'] = 'random_forest'
    n_estimators: Optional[int]
    max_depth: Optional[int]
    min_sample_split: Optional[int]
    min_sample_leaf: Optional[int]
    class_weight: Optional[Literal['balanced']]
    n_jobs: Optional[int]
    
    @field_validator('n_jobs')
    def n_jobs_(cls, v): 
        n_cpus= psutil.cpu_count(logical=True) - 2
        if v is None: 
            v= n_cpus
            logger.warning(f'Number of cpus will be used: {v}')
            return v
        else: 
            if v > n_cpus: 
                logger.warning(f'Cpus number was changed to "{n_cpus}" since previously "{v}" there were more than allowed per system')
                return n_cpus
            else: 
                return v

class DataVal(BaseModel):
    path: str
    target: str
    features: Union[List[str], str, None]
    
    @model_validator(mode='after')
    def val_columns(self): 
        path_name= self.path
        self.path= Path(__file__).parent.parent / 'config' / 'data' / path_name
        
        if not self.path.exists(): 
            logger.error(f'File {path_name} doesnt exist')
            raise FileNotFoundError(f'File {path_name} doesnt exist')
        if self.path.suffix != '.csv': 
            logger.error(f'File {path_name} should be a .csv')
            raise ValueError(f'File {path_name} should be a .csv')
        
        columns= pl.read_csv(self.path, n_rows=10).columns
        if self.target not in columns: 
            logger.info(f'The columns "{self.target}" doesnt exist in frame.\nColumns available: {columns}')
            raise ValueError(f'The columns "{self.target}" doesnt exist in frame.\nColumns available: {columns}')
        
        if isinstance(self.features, list): 
            for col in self.features: 
                if col not in columns: 
                    logger.info(f'The columns "{self.features}" doesnt exist in frame.\nColumns available: {columns}')
                    raise ValueError(f'The columns "{self.features}" doesnt exist in frame.\nColumns available: {columns}')
                if col == self.target: 
                    logger.error('Columns for features cant have the target')
                    raise ValueError('Columns for features cant have the target')
        elif isinstance(self.features, str):
            if self.features not in columns: 
                logger.info(f'The columns "{self.features}" doesnt exist in frame.\nColumns available: {columns}')
                raise ValueError(f'The columns "{self.features}" doesnt exist in frame.\nColumns available: {columns}')
            if col == self.target: 
                logger.error('Columns for features cant have the target')
                raise ValueError('Columns for features cant have the target')
        else: 
            self.features= columns.remove(self.target)
            logger.warning(f'Columns will be used for features: {columns}')
        
        return self

class Training(BaseModel): 
    test_size: float= Field(ge=0.01, le=100)
    random_state: int= Field(ge=0)

class ConfigVal(BaseModel):
    model: Union[DecisionTreeVal, DecisionTreeRegressor, RandomForest]= Field(..., discriminator='name')
    data: DataVal
    training: Training

@hydra.main(
    version_base=None, 
    config_path='../config', 
    config_name='config'
)
def main(cfg: DictConfig) -> None:
    dict_config= OmegaConf.to_container(cfg, resolve=True)
    
    try: 
        validate_cfg= ConfigVal(**dict_config)
        logger.info(f'Successful validation')
    except Exception as e:
        logger.error(f'There are problems in validating fields:\n{e}')
    
    print(validate_cfg)

if __name__ == '__main__': 
    main()



