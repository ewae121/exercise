all: install

install:
	pip install -r requirements.txt

format:
	black -l 80 src
	black -l 80 tests

test:
	pytest tests
