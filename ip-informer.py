import argparse
import requests, json
import sys
from sys import argv
import os

parser = argparse.ArgumentParser()

parser.add_argument("-v", help="target/host IP address", type=str, dest='target', required=True)

args = parser.parse_args()

red = '\033[31m'
yt = '\033[0m'
rt = '\033[96m'
a = yt+rt+"[$]"
b = red+yt+rt
print(b, """                                                     
                                   ,dPYb,            
                                   IP'`Yb            
  gg              gg               I8  8I            
  ""              ""               I8  8'            
  gg  gg,gggg,    gg   ,ggg,,ggg,  I8 dP   ,ggggg,   
  88  I8P"  "Yb   88  ,8" "8P" "8, I8dP   dP"  "Y8ggg
  88  I8'    ,8i  88  I8   8I   8I I8P   i8'    ,8I  
_,88,,I8 _  ,d8'_,88,,dP   8I   Yb,d8b,_,d8,   ,d8'  
8P""YPI8 YY888888P""Y8P'   8I   `YPI8"88P"Y8888P"    
      I8                           I8 `8,            
      I8                           I8  `8,           
      I8                           I8   8I           
      I8                           I8   8I           
      I8                           I8, ,8'           
      I8                            "Y8P' [ version 1.0]
                                          [ by white_hacker.official ] 

# Ip-Informer
# Version     : 1.0
# Description : this tool gives the ip adress information.
# Author      : white_devil & Rani Joshi
# instagram   : https://www.instagram.com/white_hacker.official/
# language    : python
# Country     : IN           

   ! WELCOME !

""")

ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = yt+rt+"[$]"
        print (a, "[Victim]:", data['query'])
        print(red+"<============================================================>"+red)
        print (a, "[Attack]:", data['status'])
        print(red+"<============================================================>"+red)
        print (a, "[Country]:", data['country'])
        print(red+"<============================================================>"+red)
        print (a, "[countryCode]:", data['countryCode'])
        print(red+"<============================================================>"+red)
        print (a, "[regionName]:", data['regionName'])
        print(red+"<============================================================>"+red)
        print (a, "[Network]:", data['as'])
        print(red+"<============================================================>"+red)
        print (a, "[ISP]:", data['isp'])
        print(red+"<============================================================>"+red)
        print (a, "[Organisation]:", data['org'])
        print(red+"<============================================================>"+red)
        print (a, "[City]:", data['city'])
        print(red+"<============================================================>"+red)
        print (a, "[Region]:", data['region'])
        print(red+"<============================================================>"+red)
        print (a, "[Longitude]:", data['lon'])
        print(red+"<============================================================>"+red)
        print (a, "[Latitude]:", data['lat'])
        print(red+"<============================================================>"+red)
        print (a, "[Time zone]:", data['timezone'])
        print(red+"<============================================================>"+red)
        print (a, "[Zip code]:", data['zip'])
        print(red+"<============================================================>"+red)

except KeyboardInterrupt:

        print ('Terminating, Bye'+lgreen)

        sys.exit(0)

except requests.exceptions.ConnectionError as e:

        print (red+"[~]"+" check your internet connection!"+clear)

sys.exit(1)