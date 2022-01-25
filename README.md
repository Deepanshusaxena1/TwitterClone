Virtual Environment:
`virtualenv venv`

Activate Environment:
`source venv/bin/activate`

Install requirements:
* `pip3 install -r requirements.txt`

Make migrations server using following command:
* Migrations for accounts app
  * `python3 manage.py makemigrations accounts`
  * `python3 manage.py migrate accounts`


* Migrations for feed app
  * `python3 manage.py makemigrations feed`
  * `python3 manage.py migrate feed`


* Migrations for default apps
  * `python3 manage.py makemigrations`
  * `python3 manage.py migrate`

Run server using following commands:

* `python3 manage.py runserver`

Server will be running on 8000 after above commands.


Front end:

Open the frontend folder in vscode:
* Install live server extension
* On bottom right corner 
* Go to 127.0.0.1:5500/