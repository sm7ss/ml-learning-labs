from omegaconf import DictConfig, OmegaConf
import hydra
import logging

from validation.config_validation import Validation

logging.basicConfig(level=logging.INFO, format='%(levelname)s-%(asctime)s-%(message)s')
logger= logging.getLogger(__name__)

@hydra.main(config_path='../config', config_name='config', version_base=None)
def validation_data(cfg: DictConfig) -> None: 
    dict_config= OmegaConf.to_container(cfg, resolve=True)
    
    try: 
        validation= Validation(**dict_config)
        logger.info('Succesful validation')
    except Exception as e: 
        logger.error(f'There are problems in validating fields:\n{e}')
        raise ValueError(f'There are problems in validating fields:\n{e}')
    
    print(validation)

if __name__ == '__main__': 
    validation_data()


