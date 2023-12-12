# sicret Makefile
# Version: 0.1
# Language: Python
# Targets:
#	lint:      runs isort + black
#	test:      run project tests
#

PROJECT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
PYTHONPATH := $(PROJECT_DIR)

.PHONY: lint test format isort black clean

# Check code style
lint:
	poetry run flake8 sicret

# Run tests
test:
	poetry run pytest -v --cov=sicret

# Format code
format: isort black

# Sort imports
isort:
	poetry run isort sicret.py

# Format code with Black
black:
	poetry run black sicret.py

# Clean up files
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .pytest_cache
