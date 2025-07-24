run:
	docker-compose up --build

test:
	docker-compose exec app pytest --cov=src

lint:
	flake8 src tests

coverage:
	docker-compose exec app pytest --cov=src --cov-report=html
