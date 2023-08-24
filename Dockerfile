FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt && mkdir /app/config && /app/model

COPY ./squad-service.py /app/
COPY ./model/*.py /app/model/

CMD ["uvicorn", "squad-service:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]