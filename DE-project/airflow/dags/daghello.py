import datetime
from airflow import DAG
from airflow import models

from airflow.operators import python_operator
import pandas as pd
import requests
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}
with models.DAG(
    "DE-test",
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_args,
) as dag:
    def greeting():
        import logging
        logging.info("Hello World!")


    def extract_data():
        import logging
        response = requests.get('http://localhost:9000')

        df = pd.read_json(response.text)
        logging.info(df)

    hello_python = python_operator.PythonOperator(
        task_id="hello", python_callable=greeting
        )
    extract_python = python_operator.PythonOperator(
        task_id="extract", python_callable=extract_data
        )
    hello_python >> extract_python