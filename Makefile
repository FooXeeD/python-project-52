install:
	poetry lock
	poetry install

dev:
	python3 manage.py runserver

test:
	poetry run python3 manage.py test

PORT ?= 8000
start:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi --timeout 90

shell:
	python3 manage.py shell

mig:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

lint:
	poetry run flake8 task_manager

mes:
	python3 manage.py makemessages -l ru

mes_c:
	python3 manage.py compilemessages -l ru

setup:
	poetry install
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

create_user:
	python3 manage.py createsuperuser
