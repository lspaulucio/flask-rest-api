APP = flask-api

compose:
	@docker-compose build
	@docker-compose up

restart:
	@docker-compose down
	@docker-compose up

test:
	@pytest -v --disable-warnings

heroku:
	@heroku container:login
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web