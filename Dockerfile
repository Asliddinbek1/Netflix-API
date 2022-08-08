FROM python:3.7

WORKDIR /code

COPY . .

RUN pip install -requiremennts.txt

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]