import os

def all_docker_local(ch):
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
		ch=input("Are you sure? press yes to continue or q to quit")
		if ch=="yes":
			os.system("docker rm  `docker  ps -a -q`")
		elif ch=="q":
			exit()
def all_docker_ssh(ch):
	ip=input("Enter the hosts ip address: ")
	if ch==1:
		os.system("ssh tty".format(ip)) # terminal you are using
	elif ch==2:	
		os.system("ssh root@{} yum list docker-ce".format(ip))
	elif ch==3:
		os.system("ssh root@{} yum insatll docker-ce  --nobest".format(ip))
	elif ch==4:
		os.system("ssh root@{} docker info".format(ip))
	elif ch==5:
		os.system("ssh root@{} docker pull {}:{}".format(ip,image_name,version))
	elif ch==6:
		os.system("ssh root@{} docker images".format(ip))
	elif ch==7:	
		os.system("ssh root@{} docker ps".format(ip)) # all running os
	elif ch==8:	
		os.system("ssh root@{} docker ps  -a".format(ip)) # all the os in running or stop condition
	elif ch==9:	
		os.system("ssh root@{} docker run -it {}:{}".format(ip,image_name,version)) # Launching the 	container
	elif ch==10:
		os.system("ssh root@{} docker start {}".foramt(ip,name_of_os))
	elif ch==11:
		os.system("ssh root@{} docker attach {}".format(ip,name_of_os))
	elif ch==12:	
		os.system("ssh root@{} docker stop {}".format(ip,name_of_os))
	elif ch==13:
			# to delete  the os forcefully
		os.system("ssh root@{} docker rm -f {}".format(ip,name_of_os))
	elif ch==14:	
			#to delete the image forcefully
		os.system("ssh root@{} docker rmi -f {}:{}".format(ip,image_name,version))
	elif ch==15:
			# All the containers id
		os.system("ssh root@{} docker  ps -a -q".format(ip))
	elif ch==16:
			# To terminate all the containers  existing in the os
		print("Warning:All the container will be deleted")
		ch=input("Are you sure? press yes to continue or q to quit")
		if ch=="yes":
			os.system("ssh root@{} docker rm  `docker  ps -a -q`".format(ip))
		elif ch=="q":
			exit()

login=input("Press r for remote login and l for local login")				

while True:
	print("""
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
	Press 17 to exit
	""")
	choice = input("Enter the choice")
	choice = int(choice)
	if choice==17:
		exit
	if login=="l":
		all_docker_local(choice)

	elif login=="r":
		all_docker_ssh(choice)
			
