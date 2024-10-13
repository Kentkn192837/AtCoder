build-py:
	docker-compose -f docker-compose.python.yml up -d --build

build-java:
	docker-compose -f docker-compose.java.yml up -d --build

up-py:
	docker-compose -f docker-compose.python.yml up -d

up-java:
	docker-compose -f docker-compose.java.yml up -d
