FROM node:12-alpine
COPY about.js babel.config.js package.json yarn.lock .browserslistrc .editorconfig .eslintrc.js /home/
COPY src /home/src
COPY public /home/public
WORKDIR /home
RUN npm install
RUN npm install -g @vue/cli@3.7.0
RUN npm i @vue/cli-service
RUN npm install chokidar
EXPOSE 8080
ENTRYPOINT npm run serve
