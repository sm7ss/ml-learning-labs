from pydantic import BaseModel, Field
from typing import Union

from .data_validation import DataValidation
from .model_validation import RandomForestClassifier, DecisionTreeClassifier, DecisionTreeRegressor

import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s-%(asctime)s-%(message)s')
logger= logging.getLogger(__name__)

class TrainingValidation(BaseModel): 
    test_size: float= Field(ge=0.01, le=0.99)
    random_state: int= Field(gt=0)
    cv_folds: int= Field(gt=0, le=10)

class Validation(BaseModel): 
    data: DataValidation
    model: Union[RandomForestClassifier, DecisionTreeClassifier, DecisionTreeRegressor]= Field(discriminator='name')
    training: TrainingValidation

