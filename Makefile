# Default target
.PHONY: all
all: install lint test run

# Install Python dependencies
.PHONY: install
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# Lint Python files
.PHONY: lint
lint:
	pip install flake8
	flake8 src

# Run tests
.PHONY: test
test:
	python -m unittest discover src/tests

# Run the application
.PHONY: run
run:
	python src/app.py
