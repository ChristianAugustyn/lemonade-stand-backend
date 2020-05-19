# Lemonade Stand Backend

Sales tracking and reporting system to help lemonade sales. This application automatically creates reports for staff based on date ranges and calculates earnings from sales as well as total commission 

## Installation

Clone the git repository into the desired directory
```bash
$ git init
$ git clone https://github.com/ChristianAugustyn/lemonade-stand-backend.git
```
A directory named `lemonade-stand-backend` will be created, cd into it and create a python virtual environment
```bash
$ cd lemonade-stand-backend
$ python -m venv .
```
This project depends on the following python libraries:
- Django
- psycopg2

To install the dependencies, first activate the virtual env
```bash
$ source bin/activate
(lemonade-stand-backend) $ pip install Django
(lemonade-stand-backend) $ pip install psycopg
```

to ensure that the dependencies have been installed use pip freeze
```bash
(lemonade-stand-backend) $ pip freeze
```

## Database Preperation

Install postgresql and ensure that it has been added to your path, use the following link to install for your system:
- https://www.postgresql.org/download/

access the postgresql cli, create the database and a user
```bash
$ sudo -u postgres psql

postgres=# create database lemonade_stand;
postgres=# create user lemonade_admin;
postgres=# alter user lemonade_admin with encrypted password 'lemons123';
postgres=# grant all privileges on database lemonade_stand to lemonade_admin;
```

## Usage

To initialize the server, the apps in the django project must be migrated
```bash
$ source bin/activate
(lemonade-stand-backend) $ cd src
(lemonade-stand-backend) $ python manage.py makemigrations
(lemonade-stand-backend) $ python manage.py migrate
(lemonade-stand-backend) $ python manage.py runserver
```
- use `http://127.0.0.1:8000/admin/` to populate the models with products and staff

- `http://127.0.0.1:8000/sales/form/` to view and use the sale form

![](/images/sales_form.png)

- `http://127.0.0.1:8000/sales/report` to view and use the report form

![](/images/sales_report.png)

## ERD

![](/images/lemonade_stand_backend_ERD.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)