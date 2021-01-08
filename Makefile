build:
	docker-compose -p "marvel_favs" -f "./docker/docker-compose.yml" build api

run:
	docker-compose -p "marvel_favs" -f "./docker/docker-compose.yml" up -d api

stop:
	docker-compose -p "marvel_favs" -f "./docker/docker-compose.yml" stop api

deploy: stop run