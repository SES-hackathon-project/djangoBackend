# Django backend set up instructions
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
``
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
5. For documentation on the APIs, refer to the github readme's within the userInput and recPlaces folders.

