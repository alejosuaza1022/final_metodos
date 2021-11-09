FROM node:14-alpine
WORKDIR /app_react
ENV PATH /app_react/node_modules/.bin:$PATH
COPY package.json ./
COPY package-lock.json ./
COPY . ./
RUN npm i
RUN npm audit fix
RUN npm run build
RUN npm install -g serve
ENV NODE_ENV=production
CMD ["npm","run", "deploy"]