FROM python:3.6-alpine
RUN adduser -D ucigrabbr
WORKDIR /home/ucigrabbr
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY pyfiles/* ./
RUN chown -R ucigrabbr:ucigrabbr ./
USER ucigrabrr
CMD uvicorn api:app --host 0.0.0.0 --port 5057 