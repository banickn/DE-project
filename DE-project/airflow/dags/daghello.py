from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import requests
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
with models.DAG(
    "composer_sample_simple_greeting",
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_dag_args,
) as dag:
    def greeting():
        import logging

        logging.info("Hello World!")
    hello_python = python_operator.PythonOperator(
        task_id="hello", python_callable=greeting
    )

    def extract_data():
        response = requests.get('localhost:9000')
        print(response.text)