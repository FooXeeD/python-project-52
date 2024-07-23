install:
	poetry lock
	poetry install

dev:
	python3 manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

shell:
	python3 manage.py shell

makemig:
	poetry run python3 manage.py makemigrations

mig:
	poetry run python3 manage.py migrate

lint:
	poetry run flake8 task_manager

setup:
	poetry install
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi
