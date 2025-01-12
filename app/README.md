
## Build the docker compose (first time)
docker-compose up --build
## run docker-compose
docker-compose up
## run testd in docker container (unit test)
docker-compose exec web pytest

# Run flask api locally (using docker)
## build the docker image
docker buildx build -t person-api .

## API integration test
### install newman
npm install -g newman
### run the API integration tests using newman
newman run -e "postman\\[inst][local] Lab1.postman_environment.json" "postman\\[inst] Lab1.postman_collection.json"