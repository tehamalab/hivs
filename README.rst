====
Hivs
====
HIV Services Information Management System.


Built using Python/Django.

- Django https://www.djangoproject.com/
- Python https://www.python.org/
 

Development Installation
=========================

The development installation process is similar to any standard Django project.

Database
--------
The project is built to use PostgreSQL database with PostGIS extension enabled.

To set things up you need create a PostgreSQL database, a database user and
enable PostGIS extension in advance. Note the details about your database name
and database user credentials so that you can apply them on project configuration.


For example on Ubuntu ...

Install postgresql

.. code:: bash

    sudo apt-get install postgresql postgresql-contrib libpq-dev

Make sure the Postgresql server is running

.. code:: bash

    sudo service postgresql start

Login as `postgres` (Postgresql admin user)

.. code:: bash

    sudo su - postgres

While logged in as `postgres` create the project database 

.. code:: bash

    createdb hivs

Connect to the database shell

.. code:: bash

    psql hivs

While you are in the database shell create the database user, grant appropriate privillages to the user and enable Hstore.

.. code:: bash

    CREATE USER hivs WITH PASSWORD '<hivs or your_dbuser_password>';
    GRANT ALL PRIVILEGES ON DATABASE hivs TO hivs;
    CREATE EXTENSION hivs;
    exit;

Logout as `postgres` user

.. code:: bash

    exit

Make sure you remember your database credentials because they are goint to be used later
in your project configuration.


Python virtual environment
--------------------------
It it highly recommended to use Python utilities like virtualenv or virtualenvwrapper
or a similar alternative in order to work within a virtual environment for better
Python dependancies management.

For more information about usage of Python virtual environments please search
for available resources online.

Create and virtual activate a virtualenvironment for the project


Project setup
-------------

Download the source code

.. code:: bash

    git clone https://github.com/tehamalab/hivs.git


Go to project root

.. code:: bash

    cd hivs


make sure your python virtual environment is active then use pip to install project requirements.

.. code:: bash

    pip install -r requirements.txt


Change your project settings according to your requirements.
For example change your database setting to reflet your existing setup and enable debug mode.

.. code:: bash

    # .env file

    DEBUG = True
    DATABASE_PASSWORD = '<your db password>'


Local project setting which are not supposed to be tracked by git settings modified by

- using system environment variables
- using environment variables written in ``.env`` file at the project root


Otherwise you can edit the ``hivs/settings.py`` file directly.
For more information on available settings please consult Django documentation

Check if things are ok

.. code:: bash

    ./manage.py check


Create database tables

::

    ./manage.py migrate


Create a superuser for administrative access

.. code:: bash

    ./manage.py createsuperuser


**NOTE:** When you are executing ``manage.py ...`` commands make sure the vertualenv is active.


Starting the development server
--------------------------------

Django comes with an inbuilt server which can be used during development.
You shouldn't be using this server on production sites.

To start the development server go to your project root directory run

.. code:: bash

    ./manage.py runserver


Now you will be able to access a site locally via http://127.0.0.1:8000


Customizing CSS
---------------

The project is using Sass for pre-processing CSS.
To customize projects stylesheet don't edit CSS directly but edit the Sass files are located in scss directory
the compile the your chnges to CSS using your favourite Sass compiler.

Example;

.. code:: bash

    sass --watch scss/main.scss:static/css/main.css


Deployment
==========

Since this is a typical Django project any standard Django deployment stack can be used.
For more information on Django deployment please look for available resources on the
Internet including https://docs.djangoproject.com/en/2.1/howto/deployment/

Most Django deployments usually include a frontend web/proxy server like Nginx,
a WSGI application server  like Gunicorn or uWSGI.

In production usually you won't want Django or your application server to serve static
files directly instead you may use Nginx or another server optimized for serving
static content.

You may also want to use a process manager like "supervisor" to manage your application daemon.
