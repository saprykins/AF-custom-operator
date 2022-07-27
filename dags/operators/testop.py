

#import libraries
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

#You can inherit from other operator of course
class MyOwnOperator(BaseOperator):
    """
    Write docstring if needed
    """
    #Apply apply_defaults decorator
    @apply_defaults
    def __init__(self,
                 param = "parameter if needed",
                 *args, **kwargs):

        super(MyOwnOperator, self).__init__(*args, **kwargs)
        #Store attributes in class
        self.param = param

    def execute():

        print ("test operator")
