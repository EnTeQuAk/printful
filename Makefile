.PHONY: tests coverage coverage-html devinstall tox docs clean-build
APP=src/
COV=printful
OPTS=

help:
	@echo "tests - run all non-selenium tests"
	@echo "coverage - run all non-selenium tests with coverage enabled"
	@echo "coverage-html - run all non-selenium tests with coverage html export enabled"
	@echo "devinstall - install all packages required for development"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "clean-build - Clean build related files"


tests:
	py.test ${OPTS} ${APP}


coverage:
	py.test --cov=${COV} --cov-report=term-missing ${OPTS} ${APP}


coverage-html:
	py.test --cov=${COV} --cov-report=html ${OPTS} ${APP}


devinstall:
	pip install -e .
	pip install -e .[docs]
	pip install -e .[tests]


tox:
	tox -c tox.ini


docs: clean-build
	sphinx-apidoc --force -o docs/modules/ src/printful
	$(MAKE) -C docs clean
	$(MAKE) -C docs html


clean-build:
	rm -fr build/ src/build
	rm -fr dist/ src/dist
	rm -fr *.egg-info src/*.egg-info
	rm -fr htmlcov/
	$(MAKE) -C docs clean
