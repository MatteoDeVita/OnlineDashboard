#Dashboard 

Vuejs + nginx + Flask + MySQL

### Important Infos

backend folder = Flask
frontend folder = Vuejs
db infos located in docker-compose.yml

UI on port 8080
phpmyadmin on port 3000

Build and run :: `docker-compose up --build`
Stop instances :: docker-compose down
Stop and Delete all containers :: `docker container stop $(docker container ls -aq) && docker container rm $(docker container ls -aq)
