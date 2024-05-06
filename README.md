# Jellybeans

This web app was written as part of a technical challenge for a job.
It is a simple CRUD app written in Python Django.
Leverages AWS S3 and RDS in order to store images and other database items.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed the latest version of Python.
- You have a `<Windows/Linux/Mac>` machine. (Specify any platform dependencies.)

## Installing Jellybeans

To install Jellybeans, follow these steps:

### Clone the repository
git clone https://github.com/JacksonSchow/jellybeans
cd hbll-jellybeans

### Set up a virtual environment
python -m venv venv
source venv/bin/activate 
# On Windows use venv\Scripts\activate

### Install the dependencies
pip install -r requirements.txt

## Configuring the Environment

Create a .env file in the project directory to store environment variables. The .gitignore file already ignores this file.

*******************************************************************************
### If you would like to run this app, you need these variables from me. I would be happy to provide them for prospective employers.
*******************************************************************************

DJANGO_SECRET_KEY
POSTGRES_HOST
POSTGRES_DATABASE_PASSWORD
AWS_SECRET_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_BUCKET_NAME

## Running Jellybeans

To run Jellybeans, execute the following commands while in your virtual environment:

python manage.py runserver

Navigate to `http://127.0.0.1:8000` in your web browser to view the app.

## Using Jellybeans

It's really a simple app. Feel free to add, edit, and delete jellybeans.
