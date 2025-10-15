# My Flask Dockerized App

## Build with Docker
# from project root
docker build -t my-flask-app .

## Run with Docker
docker run -d --name my-flask-app -p 5000:5000 my-flask-app

## Or with Docker Compose
docker-compose up --build -d

## Test the app
# root endpoint
curl http://localhost:5000/

# health
curl http://localhost:5000/health

## Stop & cleanup
docker stop my-flask-app
docker rm my-flask-app
docker rmi my-flask-app
docker-compose down

## View logs
docker logs -f my-flask-app

# my-flask-app-
