from .step import Step
from .log import config_logger


class Postflight(Step):
    def process(self, data, inputs, utils):
        logging = config_logger()
        logging.info('in postflight')
