#!/usr/bin/python3

import random
import time

#random string initializer
domainName = ["gmail.com","yahoo.com", "yandex.ru", "outlook.com", "hotmail.com", "live.com"]
usernameFile = open("usernames.txt", "r")
username = usernameFile.readlines()

#generate random credential
def randomCred():
    #random choice
    userSel = random.choice(username).strip('\n')
    domainSel = random.choice(domainName)
    randomInt = random.randint(10,9999)

    #generate email
    emailGen = userSel + str(randomInt) + "@" + domainSel

    #generate pw
    pwGen = userSel + str(random.randint(1000,999999))

    return emailGen, pwGen

