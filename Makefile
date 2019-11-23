install:
	poetry install

build: clear
	poetry build

publish: build
	twine upload --repository testpypi dist/* --config-file .pypirc

run:
	poetry run brain-games

clear:
	if [ -d "dist" ]; then rm -r dist; fi

lint:
	poetry run flake8 brain_games