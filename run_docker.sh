# build docker
docker build -t myapi .

# run the app on docker
docker run -d -p 8080:80 myapi

# compose docker so it reloads 
docker-compose up --build 