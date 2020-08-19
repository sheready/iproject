## IProject

Application to post projects to be rated by other users.


## Description

* This is an app that allows users to post reviews on other peoples projects.

## Features

* User can log in to application and view other peoples posts.
* A user can upload posts and edit their profile.
* Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.

## Behavior Driven Development

* When the user loads the page,he/she sees the uploaded sites
* If the user wants to upload a site, he/she should first register
* Then click on the upload site and fill in the form.
* Then, the user should click on the logout to log out from the page.

## Setup/Installation requirements

* Clone or download and unzip the repository from github.

* Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

* Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

* Create the Database

* psql
* CREATE DATABASE "Database Name";
* Create .env file and paste the following filling where appropriate:
1.SECRET_KEY = '<Secret_key>' 2.DBNAME = 3.USER = '' 4.PASSWORD = '' 5.DEBUG = True

* Run initial Migration -python3.6 manage.py makemigrations -python3.6 manage.py migrate

* Run the app -python3.6 manage.py runserver

* Open terminal on localhost:8000

## Technologies Used

* PYTHON 3.6
* DJANGO FRAMEWORK
* BOOTSTRAP
* POSTGRES

## Prerequisite

* PYTHON 3.6
* DJANGO FRAMEWORK
* PYTHON VIRTULENV
* POSTGRES


## License
The project is underMIT license Copyright © 2019.All rigths reserved