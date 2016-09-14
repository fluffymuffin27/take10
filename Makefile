init:
	python -m pip install -r requirements.txt

tests:
	python -m unittest discover tests/

docs:
	sphinx-apidoc . -o docs && $(MAKE) -C docs/ html

.PHONY: init tests docs
