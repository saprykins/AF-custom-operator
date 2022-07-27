from datetime import datetime, timedelta

TRIGRAM = 'PRT'
BIGRAM = 'PT'
LANGAGE = 'UK'
ENV = '{{ var.value.env }}'
PROJECT = f'ari-data-dp-airflow-prt'

DEFAULT_ARGS = {
    'owner': 'airflow',
    'start_date': datetime(2019, 6, 18),
    'depends_on_past': False,
    'email': ['sv@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'max_active_runs': 1,
    'retry_delay': timedelta(minutes=5)
}
