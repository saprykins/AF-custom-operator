

#import libraries
# from airflow.models import BaseOperator
# from airflow.utils.decorators import apply_defaults
from airflow.models.baseoperator import BaseOperator

#You can inherit from other operator of course

from google.cloud import logging


class MyOwnOperator(BaseOperator):
    """
    Write docstring if needed
    """
    #Apply apply_defaults decorator
    def __init__(self, name: str, **kwargs) -> None:

        super().__init__(**kwargs)
        #Store attributes in class
        self.name = name

    def execute(self, context):
        message = f"Hello {self.name}"
        logging_client = logging.Client()
        log_name = "_Default"
        logger = logging_client.logger(log_name)
        logger.log_text(message)
        
        print(message)
        return message
