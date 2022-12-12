module = geoambiental

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

.PHONY: \
    check \
    clean \
    coverage \
    format \
    init \
    install \
    linter \
    mutants \
    tests

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests

clean:
	rm --force --recursive ${module}.egg-info
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive .*_cache
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache
	rm --force NAMESPACE
	rm --force coverage.xml

coverage: install
	pytest --cov=${module} --cov-report=term-missing --verbose

format:
	black --line-length 100 ${module}
	black --line-length 100 tests

mutants: install
	mutmut run --paths-to-mutate ${module}

init: install tests

install: clean
	pip install --editable .

tests:
	pytest --verbose