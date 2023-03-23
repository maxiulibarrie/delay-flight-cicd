import subprocess as sp

from pipeline.train.prepare import prepare_train_data
from pipeline.train.train import train
from common.credential_decode import decode_save_credentials

from common.log_handler import Logger

logger = Logger()

if __name__ == '__main__':
    logger.log.info("Retrieving credentials.")
    decode_save_credentials()

    logger.log.info("Pull data and current model.")
    sp.run(['dvc','pull'])

    logger.log.info("Preparing Data.")
    prepare_train_data()

    logger.log.info("Starting Training Process.")
    train()

    #TODO: upload model to gs