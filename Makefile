run:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

create-req:
	pip freeze > requirements.txt

setup-req:
	pip install -r requirements.txt