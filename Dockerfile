FROM python:3.10-slim

WORKDIR app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./task_tracker ./run_script.sh ./

RUN chmod +x /app/run_script.sh

ENTRYPOINT ["/app/run_script.sh"]