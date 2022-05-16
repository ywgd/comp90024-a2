#!/bin/bash

echo "build the docker image"
sudo docker build -t a2:group .
echo "Deploying the update container"
sudo docker run -it -d -v $PWD/var/www/html -p 80:80 --name group36 a2:group
echo "Delpoying the container"

