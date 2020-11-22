# DOCKER - WEBSERVER, DATABASE

### OS
* Amazon aws EC2 ubuntu 18.04
* Same as OS X

### Software
* Docker v19.03.6
* docker-compose v1.25.0-rc2

### Installation
#### Docker
```
1. $ sudo apt update -y
2. $ sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
3. $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
4. $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
5. $ sudo apt update -y
6. $ sudo apt install -y docker-ce
7. $ sudo systemctl start docker
8. $ sudo systemctl status docker
9. $ docker version
```
#### docker-compose
* you can choose the version(https://github.com/docker/compose/releases)
```
1. $ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
2. $ sudo chmod +x /usr/local/bin/docker-compose
3. $ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
4. $ docker-compose -version 
```

### Execution
* In the SERVER Directory
```
$ docker-compose up
```

### TroubleShooting
* pymongo.errors(pymongo.errors.ServerSelectionTimeoutError: mongodb:27017: [Errno -2] Name does not resolve)
  * change services name in docker-compose.yml
  * (https://stackoverflow.com/questions/64855098/docker-compose-with-django-mongodb-using-djongo-error-pymongo-errors-serverse)
  ```
  'mongo' -> 'mongodb'
  ```
  * docker-compose up error("ERROR: Version in "./docker-compose.yml" is unsupported")
  ```
  $ sudo apt-get remove docker-compose
  $ sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  $ sudo chmod +x /usr/local/bin/docker-compose
  $ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
  ```
* mongo/home/mongodb volume error
  ```
  $ chown -R 999:999 ./home/mongodb
  ```
  * https://github.com/docker-library/mongo/issues/323 
  
### [Development Log](https://github.com/SeongNamYouthTeamE/RaspiCam/blob/main/SERVER/webserver/README.md) 
