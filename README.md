# ABOUT PROJECT

The project demonstrates the ability to automatically deploy web-service using Docker.

# START

Install Docker on your computer (https://www.docker.com/).

Clone the repository and go to it on the command line:
```
git clone git@github.com:irinaexzellent/infra_sp2.git
```

# Description of commands for running an application in containers

Dockerfile — this is a file with instructions for creating an image.
'docker-compose.yaml' provides instructions for deploying a project to container.

Go to the directory where docker-compose.yml is saved and run:
```
docker compose up -d --build
```
You can view information about deployed containers using the command:
```
$ docker container ls
```

## Functionality check

API project:

* http://localhost:8004/docs#/default/predict_model_predict_post

After sending a POST request in string format, you will receive information about the presence or absence of an anomaly in the operation of the equipment.
Example string:
```
"2020-03-09 14:09:56,0.0278083,0.0399288,1.21178,0.054711,68.7436,24.7123,235.085,27.977"
```

## Author

* **Irina Ikonnikova** -  [[IrinaIkonnikova](https://github.com/irinaexzellent)]



