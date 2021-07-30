# iHello

A Simple Messaging Application Server

## Prerequisit
+ Python 3.7
+ Postgresql

## Setup

```
$ git clone https://github.com/caffeines/iHello
$ cp example.env .env
$ pip3 install -r requirements.txt
$ python3
$ import server.database.models
$ from server.database.client import db
$ db.create_all()
```

## Run application

```
$ flask run
```
