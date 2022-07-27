
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from airflow.models import DAG
from airflow.utils.task_group import TaskGroup

# from operators.bq_simple_operator import BqSimpleOperator
#from utils.gcp_connection import get_gcp_connection_id
#from utils.query_param import query_param

# from operators.bq_table_copy_operator import BqTableCopyOperator
from operators.testop import MyOwnOperator




with DAG(
        dag_id='PRT_Test_Daily',
        schedule_interval='00 7 * * *',
        catchup=False,
        #default_args=DEFAULT_ARGS,
        template_searchpath='/',
) as dag:
    with TaskGroup('load') as load:
        gen_bq_load_site(
            project_id=PROJECT,
            trigram=TRIGRAM,
        )
    load
