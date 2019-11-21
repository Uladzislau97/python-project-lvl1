install:
	poetry install

build:
	poetry build

publish:
	twine upload --repository testpypi dist/* --config-file .pypirc

run:
	poetry run brain-games