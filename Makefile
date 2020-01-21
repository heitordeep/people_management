SHELL=/bin/bash

help:
	@echo 'Makefile for Jobs			                                 '
	@echo '                                                              '
	@echo 'Usage:                                                        '
	@echo '    make requirements       Install required packages to Dev  '
	@echo '    make superuser          Create admin user on Django       '
	@echo '    make migrate_db         Apply the migrations to DB        '
	@echo '    make runserver          Run the application               '
	@echo '                                                              '


requirements:
	pip install - r requirements-dev.txt

superuser:
	python manage.py createsuperuser

migrate_db:
	python manage.py migrate

runserver:
	python manage.py runserver
