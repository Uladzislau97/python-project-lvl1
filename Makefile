install:
	@poetry install

build: clear
	@poetry build

publish: build
	twine upload --repository testpypi dist/* --config-file .pypirc

GAME = games

run:
	@poetry run brain-$(GAME)

clear:
	if [ -d "dist" ]; then rm -r dist; fi

lint:
	@poetry run flake8 brain_games