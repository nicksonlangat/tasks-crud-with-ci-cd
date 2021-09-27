## PROJECT SET UP
#### Getting started
These instructions will get you a copy of the project up and running in your local machine for development and testing purposes.

## Prerequisites
- [Git](https://git-scm.com/download/)
- [Python 3.6 and above](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)


## Installing
### Setting up the database
- Start your database server and create your database

### Setting up and Activating a Virtual Environment
- Create a working space in your local machine
- Clone this [repository](https://github.com/nicksonlangat/tasks-crud-with-ci-cd.git ) `git clone https://github.com/nicksonlangat/tasks-crud-with-ci-cd.git `
- Navigate to the project directory
- Create a virtual environment `virtualenv name_of_your_virtual_environment` and activate `source name_of_your_virtual_environment/bin/activate`
- Create a .env in the same location as `settings.py` file and put these key=values in it:
```
SECRET_KEY=YOUR SECRET KEY
DATABASE_NAME=db_name
DATABASE_USER=db_username
DATABASE_PASS=db_password

```

- Install dependencies to your virtual environment `pip install -r requirements.txt`
- Migrate changes to the newly created database `python manage.py migrate`

## Starting the server
- Ensure you are in the project directory on the same level with `manage.py` and the virtual environment is activated
- Run the server `python manage.py runserver`

## PROJECT FEATURES
#### EMAIL NOTIFICATIONS
#### VUE JS FRONTEND
#### ANDROID/IOS APP
