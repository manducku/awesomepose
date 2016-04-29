clean:
	find . -name "*.pyc" -exec rm -rf {} \;

migrate:
	python awesomepose/manage.py makemigrations users users tags django_summernote mptt categories posts
	python awesomepose/manage.py migrate 

test:
	python blogram/manage.py users 
