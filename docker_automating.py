import os

def all_docker(ch):
	if ch==1:
		os.system("tty") # terminal you are using
	if ch==2:	
		os.system("yum list docker-ce")
	if ch==3:
		os.system("yum insatll docker-ce  --nobest")
	if ch==4:
		os.system("docker info")
	if ch==5:
		os.system("docker pull {}:{}".format(image_name,version))
	if ch==6:
		os.system("docker images #all the images available")
	if ch==7:	
		os.system("docker ps") # all running os
	if ch==8:	
		os.system("docker ps  -a") # all the os in running or stop condition
	if ch==9:	
		os.system("docker run -it {}:{}".format(image_name,version)) # Launching the container
	if ch==10:
		os.system("docker start {}".foramt(name_of_os))
	if ch==11:
		os.system("docker attach {}".format(name_of_os))
	if ch==12:	
		os.system("docker stop {}".format(name_of_os))
	if ch==13:
		# to delete  the os forcefully
		os.system("docker rm -f {}".format(name_of_os))
	if ch==14:	
		#to delete the image forcefully
		os.system("docker rmi -f {}:{}".format(image_name,version))
	if ch==15:
		# All the containers id
		os.system("docker  ps -a -q")
	if ch==16:
		# To terminate all the containers  existing in the os
		print("Warning:All the container will be deleted")
		ch=input("Are you sure? press yes to continue")
		if ch=="yes"
			os.system("docker rm  `docker  ps -a -q`")
def all_docker_ssh(ch):  ####  in ssh  i am still working it is not completed
	if ch==1:
		os.system("tty") # terminal you are using
	if ch==2:	
		os.system("yum list docker-ce")
	if ch==3:
		os.system("yum insatll docker-ce  --nobest")
	if ch==4:
		os.system("docker info")
	if ch==5:
		os.system("docker pull {}:{}".format(image_name,version))
	if ch==6:
		os.system("docker images #all the images available")
	if ch==7:	
		os.system("docker ps") # all running os
	if ch==8:	
		os.system("docker ps  -a") # all the os in running or stop condition
	if ch==9:	
		os.system("docker run -it {}:{}".format(image_name,version)) # Launching the container
	if ch==10:
		os.system("docker start {}".foramt(name_of_os))
	if ch==11:
		os.system("docker attach {}".format(name_of_os))
	if ch==12:	
		os.system("docker stop {}".format(name_of_os))
	if ch==13:
		# to delete  the os forcefully
		os.system("docker rm -f {}".format(name_of_os))
	if ch==14:	
		#to delete the image forcefully
		os.system("docker rmi -f {}:{}".format(image_name,version))
	if ch==15:
		# All the containers id
		os.system("docker  ps -a -q")
	if ch==16:
		# To terminate all the containers  existing in the os
		print("Warning:All the container will be deleted")
		ch=input("Are you sure? press yes to continue")
		if ch=="yes"
			os.system("docker rm  `docker  ps -a -q`")

while True:
	input("""
	Press 1 to know the terminal.
	Press 2 to check that docker is available in the repos.
	Press 3 to install docker community edition.
	Press 4 to check that docker is working properly.
	Press 5 to download images from docker hub.
	Press 6 to check all the images available.
	Press 7 to see all the running containers.
	Press 8 to see all the existing containers.
	Press 9 to Launch the conatiner.
	Press 10 to Start the container.
	Press 11 to attach the container.
	Press 12 to stop the container.
	Press 13 to delete the container forcefully.
	Press 14 to delete the image forcefully.
	Press 15 to see all the containers id.
	Press 16 to delete all the existing containers.
	""")
	ch = input("Enter your choice")
	all_docker(int(ch))
