#!/usr/bin/python3

import requests
import sys
import CredentialGenerator as gen

#phisher capturing credential endpoint
phisherURL = "http://192.168.169.204/signin"

while True:
    try:
        #generate fake credential 
        email, pw = gen.randomCred()

        #POST Data (this one need to be change according to the situation)
        data = {
            "login_email" : email,
            "login_password" : pw
        }

        print("[*] Flooding credential => " + email + ":" + pw)
        requests.post(phisherURL, data=data)
    except KeyboardInterrupt:   #when user input "CTRL+C"        
        print('[*] Exiting...')
        sys.exit(0)
    except:
        continue    #prevent script stop