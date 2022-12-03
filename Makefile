APP = FLASK-API

compose:
	@docker-compose build
	@docker-compose up

test:
	@pytest -v --disable-warnings
