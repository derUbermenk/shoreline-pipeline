FROM apache/airflow:2.9.0-python3.10

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt