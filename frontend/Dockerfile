FROM node:alpine

RUN npm install -g @angular/cli

WORKDIR /usr/src/app
# install and cache app dependencies
COPY package.json /usr/src/app/package.json
RUN npm install
COPY . /usr/src/app/
