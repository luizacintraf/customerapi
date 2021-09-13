# Django Simple API: Customer API

These is a simple API to get customers infos, it has some functions to update the database from a csv and add address coordinates

## Table of Contents

* [Features](#Features)
* [Requirements](#Requirements)
* [Setup](#Setup)
* [Setup database](#Setup-database)
* [Run](#Run)
* [Tests](#Tests)
* [Build with](#Build-with)
* [Authors](#Authors)

## Features
* Load a CSV file into your database
* Add coordinates based in address
* Run an API and get the database items

## Requirements
* Python 3.3 and up [Install](https://www.python.org/)
* virtualenv [Install](https://virtualenv.pypa.io/en/latest/)
* Google maps API key (if you want to populate the coordinates)[Tutorial](https://developers.google.com/maps/documentation/geocoding/cloud-setup)

## Setup

```sh
$ git clone https://github.com/luizacintraf/customerapi.git
$ virtualenv venv #create a virtual environment
$ source venv/bin/activate #activate the environment
(venv) $ cd app
(venv) $ python -m pip install -U pip setuptools
(venv) $ pip install -e .
(venv) $ python manage.py migrate
```
 
## Setup database

* First you need to create a .env file as the example.env and add your API_KEY
* If you will use the Customer model and the customer.csv to setup the database:
```sh
(venv) $ python manage.py load_csvdata --path=customers.csv --model_name=Customer --app_name=customers
(venv) $ python manage.py add_coordinates --model_name=Customer --app_name=customers --address_field=city --lat=latitude --lng=longitude
```

## Run

To see the project running you can use the command bellow: 

```sh
(venv)$ python manage.py runserver
``` 
It will open a page where you can perform get requests from costumer table

## Tests

```sh
(venv)$ python manage.py test costumers
```

## Built with
1. [DJANGO](https://www.djangoproject.com/) - Python framework


## Authors 
Luiza Cintra Fernandes  – luiza.fernandes@gmail.com
 
You can find me here at:
[Github](https://github.com/luizacintraf)
[LinkedIn](https://www.linkedin.com/in/luizacintrafernandes/)

