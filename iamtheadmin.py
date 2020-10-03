import requests
from termcolor import colored
import time
string = "This Tool is for Educational Purpose Only "
for char in string:
    print(char, end='')
    time.sleep(.25)
    print("")
val = input("Enter website url in https://website.com/ format :")
print(colored("I see you've entered " + val,"green"))
print(colored("Testing......","green"))
response = requests.get(val)
if (response.status_code == 200):
  print("Hmm.. The site is working, Scanning for admin site.....")
  response = requests.get(val + "admin")
  
  if(response.status_code ==200):
     print(colored("Yay! Admin site found:" + val + "admin","red"))
  else:
      print("Enumerating ...")

  response = requests.get(val + "administrator")
    
  if(response.status_code==200):
    
      print(colored("Yay! Admin site found:" + val + "administrator","red"))
      
      
  else:
    print("Enumerating .....")
    
        
         
  response = requests.get(val + "wp-admin")
  if(response.status_code==200):
    print(colored("Yay! Admin site found:" + val + "wp-admin","red"))
  else:
   print("Thats all I can do.")
else:
  print("Sorry the target isnt working")
      

