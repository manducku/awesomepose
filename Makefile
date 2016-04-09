clean:
	find . -name "*.pyc" -exec rm -rf {} \;

migrate:
	python awesomepose/manage.py makemigrations users posts tags django_summernote
	python awesomepose/manage.py migrate 

test:
	python blogram/manage.py users 
