FROM python:3.8

ADD ./ ./

RUN pip install -r requirements.txt

CMD ["python3","-u", "api.py"]