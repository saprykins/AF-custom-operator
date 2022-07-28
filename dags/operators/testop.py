

#import libraries
# from airflow.models import BaseOperator
# from airflow.utils.decorators import apply_defaults
from airflow.models.baseoperator import BaseOperator

#You can inherit from other operator of course
class MyOwnOperator(BaseOperator):
    """
    Write docstring if needed
    """
    #Apply apply_defaults decorator
    def __init__(self, name: str, **kwargs) -> None:

        super().__init__(**kwargs)
        #Store attributes in class
        self.name = name

    def execute(self):
        message = f"Hello {self.name}"
        print(message)
        return message
