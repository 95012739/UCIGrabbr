FROM python:3.6-alpine
RUN adduser -D ucigrab
WORKDIR /home/ucigrab
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY controller.py ./
COPY pyfiles/* ./
RUN chown -R ucigrab:ucigrab ./
USER ucigrab
CMD uvicorn api:app --host 0.0.0.0 --port 5057 