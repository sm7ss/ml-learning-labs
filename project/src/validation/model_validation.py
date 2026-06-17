from pydantic import BaseModel, field_validator
from typing import Optional, Literal
import psutil

import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s-%(asctime)s-%(message)s')
logger= logging.getLogger(__name__)

class DecisionTreeRegressor(BaseModel):
    name: Literal["decision_tree_regressor"] = 'decision_tree_regressor'
    n_estimators: Optional[int]
    max_depth: Optional[int]
    min_sample_split: Optional[int]
    min_sample_leaf: Optional[int]
    class_weight: Literal['balanced', 'balanced_subsample']
    n_jobs: Optional[int]
    
    @field_validator('n_jobs')
    def n_jobs_calculate(cls, v): 
        c= psutil.cpu_count(logical=True) - 2 
        if not v: 
            logger.warning(f'The number of cpus will be used: {c} leaving two for system')
            return c
        else:
            if v > c:
                logger.warning(f'The number of CPU cores is greater than the allowed one ({v} - {c}). The new number of cpus used will be {c}')
                return c
            else: 
                return c

class RandomForestClassifier(BaseModel): 
    name: Literal["decision_tree_classifier"] = 'decision_tree_classifier'
    max_depth: Optional[int]
    min_sample_split: Optional[int]
    min_sample_leaf: Optional[int]
    class_weight: Literal['balanced', 'balanced_subsample']

class DecisionTreeClassifier(BaseModel): 
    name: Literal["random_forest_classifier"] = 'random_forest_classifier'
    n_estimators: Optional[int]
    max_depth: Optional[int]
    min_sample_split: Optional[int]
    min_sample_leaf: Optional[int]
    class_weight: Literal['balanced', 'balanced_subsample']
    n_jobs: Optional[int]
    
    @field_validator('n_jobs')
    def n_jobs_calculate(cls, v): 
        c= psutil.cpu_count(logical=True) - 2 
        if not v: 
            logger.warning(f'The number of cpus will be used: {c} leaving two for system')
            return c
        else:
            if v > c:
                logger.warning(f'The number of CPU cores is greater than the allowed one ({v} - {c}). The new number of cpus used will be {c}')
                return c
            else: 
                return c

