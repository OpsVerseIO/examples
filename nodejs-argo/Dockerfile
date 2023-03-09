FROM node:18-alpine
ENV PORT 3000

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

RUN npm install

EXPOSE 3000

CMD "npm" "run" "start"
