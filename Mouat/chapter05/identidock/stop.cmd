docker stop $(docker ps -lq)
docker rm $(docker ps -lq)
docker run -d -p 5000:5000 -v "$(pwd)"/app:/app identidock
