# FROM ubuntu uncomment if you want to use ubuntu

# Install pip and git
# RUN apt-get update && apt-get install --assume-yes --fix-missing python-pip git

# Clone repository to /app folder in the container image
# RUN git clone https://github.com/amirziai/sklearnflask.git /app

#####################################################################################################################
FROM python:3.6.6-slim

# Mount current directory to /app in the container image
VOLUME ./:app/

# Copy local directory to /app in container
COPY * /app/

# Change WORKDIR
WORKDIR /app

# Install dependencies
# use --proxy http://<proxy host>:port if you have proxy
RUN pip install -r requirements.txt

# Expose port and run the application when the container is started
EXPOSE 9999
ENTRYPOINT python main.py 9999
# CMD ["main.py"]


# docker build
# docker build -t <app name> .

# docker run
# docker run ml_app -p 9999 # to make the port externally avaiable for browsers

# show all running containers
# docker ps

# Kill and remove running container
# docker rm <containerid> -f

# open bash in a running docker container
# docker exec -ti <containerid> bash

# docker compose
# run and interact between multiple docker containers