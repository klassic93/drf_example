Documentation to RESTful project
=============

1. [Download project](#Download)
2. [Virtual environment](#Venv)
3. [Requirements](#Requirements)
4. [Creating database](#Database)
4. [Run project](#Start)

## API

* Get or Create users:


     /api/v1/users/
     
* Get one user via primary key (```<pk>```) and change him:

     
     /api/v1/users/<pk>/
     
* Get or Create books:


     /api/v1/books/
     
* Get one book via primary key (```<pk>```) and change it:


     /api/v1/books/<pk>/
     
     
* Get only available books:


     /api/v1/books/free/
     
* Get rating books where popularity from 1 to 100:


     /api/v1/books/?popularity=<int:value>


## Download
The first you have to go you empty directory

     $ cd /you/empty/dirrectory/for/example

After you can use this command:
     
     $ git clone https://github.com/klassic93/inovice_group.git
     
## Venv

You can use this command for creating virtual environment:

     $ python3 -m venv venv
     
Mor info about virtual environment you can find [here](https://docs.python.org/3/library/venv.html)

After installing we should activate this environment:

     $ source venv/bin/activate
## Requirements

Next we have to install all requirements:

     (venv) $ pip install -r requirements.txt
     
Lets check our requirements:

     (venv) $ pip list
     
Expect to see these modules:

        Django (2.2.4)
        django-filter (2.2.0)
        djangorestframework (3.10.2)
        pip (9.0.3)
        psycopg2 (2.8.3)
        pytz (2019.2)
        setuptools (39.0.1)
        sqlparse (0.3.0)

If we see all of these everything ok and we can continue

You can also install each module using this command:
     
     (venv) $ pip install <some module>
## Database
Before moving on to launching the project we need to create our database
and add configs to [settings](https://github.com/klassic93/inovice_group/blob/master/inovice_group/settings.py)
 django
 
 We must have established PostgreSQL. [Here](https://www.godaddy.com/garage/how-to-install-postgresql-on-ubuntu-14-04/)
 you can view how to do it. We`ll use user name ***inovice*** and database name the same.
 You can use another names, but you should take it in the future
 
 Go to postgres:
      
      $ psql -U postgres
      
Create database:

     postgres=# CREATE DATABASE inovice;
      
Next create user:

     postgres=# CREATE USER inovice WITH PASSWORD '';
     
Configure access:
     
     postgres=# ALTER ROLE inovice SET client_encoding to 'utf8';
     postgres=# ALTER ROLE inovice SET default_transaction_isolation TO 'read committed';
     postgres=# ALTER ROLE inovice SET timezone TO 'UTC';
     
     postgres=# GRANT ALL PRIVILEGES ON DATABASE inovice TO inovice;

Ok. After that lets add our configs to settings file:
 
 ```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inovice',   #name our database
        'USER' : 'inovice',  #name our user
        'PASSWORD' : '',     #our password for access
        'HOST' : '127.0.0.1',
        'PORT' : '5432'
    }
}
```

## Start
At the end we do migration:

     (venv) $ python manage.py makemigration
     (venv) $ python manage.py migrate

or shorter:

     (venv) $ ./manage.py makemigration
     (venv) $ ./manage.py migrate
     
and run server

     (venv) $ ./manage.py runserver
     
go to [http://127.0.0.1:8000/api/v1/users/](http://127.0.0.1:8000/api/v1/users/)

Congratulations! You can use [this api](#API)