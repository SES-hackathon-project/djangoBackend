# BACKEND: how to set up, API documentation

## How to set up
Before you start, make sure you have python/pip installed on your system.

1. (in command line) clone repository, cd into repository, then create virtualenv
```
git clone https://github.com/SES-hackathon-project/djangoBackend.git
```
```
cd djangoBackend
```
```
python -m venv venv
```
2. activate virtualenv
```
#if you are using windows:
venv\Scripts\activate
```
```
#if you are using mac:
source venv\bin\activate
```
3. install requirements
```
pip -r requirements.txt
```
4. migrate to set up SQLite database tables
```
python manage.py makemigrations
```
```
python manage.py migrate
```
5. Run the backend server
```
python manage.py runserver
```
6. for reference on API endpoints, see the "API documentation" section below.

## API documentation

for the userInput API: https://github.com/SES-hackathon-project/djangoBackend/tree/master/userInput

