FROM python:3.6-alpine

WORKDIR /code
ADD requirements.txt /code
ADD manage.py /code
ADD questionnarie /code/questionnarie
RUN pip install -r /code/requirements.txt
ADD run.sh /code

CMD ["sh", "run.sh"]
