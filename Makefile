APP = flask-api

compose:
	@docker compose build
	@docker compose up

restart:
	@docker-compose down
	@docker-compose up

test:
	@black .
	@flake8 --statistics
	@bandit -r . -x '*/tests/*'
	@pytest -v --disable-warnings


heroku:
	@heroku container:login
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web