# Define variables
VENV_DIR := venv
PYTHON := $(VENV_DIR)/bin/python

# Target to run main.py with PYTHONPATH set to include the necessary directory
.PHONY: run
run: $(VENV_DIR)/bin/activate
	PYTHONPATH="$(shell pwd)/../.." $(PYTHON) main.py

# Target to create the virtual environment and install dependencies
.PHONY: build
build:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r requirements.txt
	@echo "Environment setup complete with dependencies installed."

# Create venv if not present
$(VENV_DIR)/bin/activate:
	$(MAKE) build

# Default target to run
default: run

# Clean up the virtual environment
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)
	@echo "Virtual environment removed."
