# iHello

A Simple Messaging Application Server

## Prerequisite
+ Python 3.7
+ Postgresql

## Setup

```
$ git clone https://github.com/caffeines/iHello
$ cp example.env .env # make necessary changes
$ python3 -m venv venv  # if not already created
$ source venv/bin/activate
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
