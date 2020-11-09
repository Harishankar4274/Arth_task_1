import os
import getpass



os.system("tput setaf 3")
print("\t\t\tWelcome To My Menu ")
os.system("tput setaf 7")
print("\t\t\t----------------")




r  = input("where to want to run this menu ? (local / remote):")
print(r)

while True:
      os.system("clear")
      os.system("cd /etc/hadoop  ")
      os.system("") 
      os.system("")
      os.system("")
      print("""
      \n
      Press 1 : Configure Master node core-site.xml 
      Press 2 : Configure Master node hdf-site.xml
      Press 3 : Start Cluster     
      Press 4 : Configure Data node core-site.xml                               
      Press 5 : Configure Data node hdfs-site.xml                             
      Press 6 : Start Data node                       
      Press 7 : Configure Client Node Setup
      Press 8 : Report Of Cluster 
      Press 9 : Files In Cluster 
      Press 10 : To Upload File In Cluster
      Press 11 : To Remove File From The Cluster 
      Press 12 : To Read File From The Cluster
      Press 13 : To Upload The File With Blocksize
      Press 14 : To LEave Safe Mode 
      


                                    
      """)
      ch = input("Enter Your Choice:")
      print(ch)                
      if r == "local":                       
               if int(ch) == 1:
                  os.system(" vim /etc/hadoop/core-site.xml ")
               elif int(ch) == 2:
                    os.system("vim /etc/hadoop/hadf-site.xml ")       
               elif int(ch) == 3:
                    os.system("hadoop-daemon start namenode")                             
               elif int(ch) == 4:
                    os.system("vim /etc/hadoop/core-                         site.xml")                           
               elif int(ch) == 5:
                    os.system("vim etc/hadoop/hadfs-site.xml")                                                  
               elif int(ch) == 6:
                    os.system("hadoop-daemon start datanode")                               
               elif int(ch) == 7:
                    os.system("vim /etc/hadoop/core-site.xml") 
               elif int(ch) == 8:
                    os.system("hadoop dfsadmin -report")
               elif int(ch) == 9:
                    os.system("hadoop fs -ls/")                                
               elif int(ch) == 10:
                    os.system("hadoop fs -put f.txt/")                                  
               elif int(ch) == 11:
                    os.system("hadoop fs -rm /f.txt")                       
               elif int(ch) == 12:
                    os.system("hadoop fs -cat /f.txt")
               elif int(ch) == 13:
                    os.system("hadoop fs -ls/")
               elif int(ch) == 14:
                    os.system("hadoop dfsadmin -safemode leave")               
               else:   
                    print("Not Supported")                
      elif r== "remote":
           ip = input("Enter remote ip")
           print(ip)       
           if int(ch)== 1:
                 os.system("sh {vim /etc/hadoop/core-site.xml} ".format(ip))       
           elif int(ch) == 2:
                 os.system("sh {vim /etc/hadooop/hdfs-site.xml}".format(ip))                     
           elif int(ch)== 3:
                 os.system("sh {hadoop-daemon.sh start namenode} ".format(ip))            
           elif int(ch)== 4:
                 os.system("sh {vim /etc/hadoop/core-site.xml} ".format(ip))             
           elif int(ch)== 5:
                 os.system("sh {vim /etc/hadoop/hdfs-site.xml}".format(ip))          
           elif int(ch)== 6:
                 os.system("sh {hadoop-daemon.sh start datanode} ".format(ip))             
           elif int(ch)== 7:
                 os.system("sh {vim /etc/hadoop/core-site.xml}".format(ip))   
           elif int(ch)== 8:
                 os.system("sh {hadoop dfsadmin -report} ".format(ip))  
           elif int(ch)== 9:
                 os.system("sh {hadoop fs-ls/} ".format(ip))     
           elif int(ch)== 10:
                 os.system("sh {hadoop fs -put filename/ } ".format(ip))  
           elif int(ch)== 11:
                 os.system("sh {hadoop fs -rm /filename} ".format(ip))  
           elif int(ch)== 12:
                 os.system("sh {hadoop fs -cat /filename} ".format(ip))  
           elif int(ch)== 13:
                 os.system("sh {hadoop fs -ls/} ".format(ip))    
           elif int(ch)== 14:
                 os.systeem("sh {hadoop dfsadmin -safeadmin leave}".format(ip)) 
           else:
                print("Not Supported")
            
      else:
           print("Not Supported Login.....") 
         
























