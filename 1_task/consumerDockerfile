FROM python:3.6-alpine

WORKDIR /code
ADD consumer.py /code
ADD requirements.txt /code

RUN pip install -r /code/requirements.txt
CMD ["python", "/code/consumer.py"]
