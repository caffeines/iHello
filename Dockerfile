FROM python:3.7
WORKDIR /code

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python3", "main.py"]
