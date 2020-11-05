yum list docker-ce
yum insatll docker-ce  --nobest
docker info
docker pull [image_name]:[version]
docker images #all the images available
docker ps # all running os
docker ps  -a # all the os in running or stop condition
docker run -it [image_name]:[version] # Launching the container

docker start [name_of_os]
docker attach [name_of_os]
# to delete  the os forcefully
docker rm -f name_of_os
#to delete the image forcefully
docker rmi -f [image]:[version]

# All the containers id
docker  ps -a -q

# To terminate all the containers  existing in the os
docker rm  `docker  ps -a -q`


