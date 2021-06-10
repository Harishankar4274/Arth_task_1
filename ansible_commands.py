import os
os.system("tput setaf 1")
print("\t\t\tWelcome to the ansible menu")
os.system("tput setaf 7")
while True:
	print("""
	Press 1 to install  ansible 
	Press 2 to check the ansible version
	Press 3 to see the list of hosts
	Press 4 to check the connectivity b/w the target node and controller node
	Press 5 to exit
	""") 

	ch = input("Enter your choice:")
	ch=int(ch)
	if ch==1:
		os.system("pip3 install ansible")
	elif ch==2:
		os.system("ansible --version")
	#list of all the hosts/target node
	elif ch==3:
		os.system("ansible all --list-hosts")
	#ping to all the target nodes
	elif ch==4:
		os.system("ansible all -m ping")
	elif ch==5:
		exit()
