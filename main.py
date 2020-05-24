import requests
import os
import random
import string
import json


chars = string.ascii_letters + string.digits
random.seed = (os.urandom(1024))
url = "https://koblizek.club/page/invite-request.php"
filename = json.loads(open("names.json").read())
for names in filename:
    name_extra = "".join(random.choice(string.digits))  
    name = names
    steam = "https://steamcommunity.com/id/" + names.lower()
    email = names.lower() + name_extra + "@gmail.com"
    password = "".join(random.choice(chars) for i in range(8))
    discord = names.lower() + name_extra + "#1234"
    requests.post(url, allow_redirects=False, data={
        "Name" : name,
        "Password" : password,
        "Steam" : steam,
        "Email" : email,
        "Discord" : discord
    } 
    )
    print("Going with " + name + " " + password + " " + email + " " + discord + " "  + steam)