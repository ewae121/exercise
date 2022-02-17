all: install

install:
	pip install -r requirements.txt

format:
	black src
	black tests

test:
	pytest tests
