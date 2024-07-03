install:
	pip install -r requirements.txt

lint:
	pylint your_python_module.py

test:
	python3 -m unittest discover

run:
	python3 your_script.py

