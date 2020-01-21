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
<<<<<<< HEAD
	pip install - r requirements-dev.txt
=======
	pip install -r requirements-dev.txt
>>>>>>> 684ca86b607f7571c49f17534cb5651beab0b7b5

superuser:
	python manage.py createsuperuser

migrate_db:
	python manage.py migrate

runserver:
	python manage.py runserver
