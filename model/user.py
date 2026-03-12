from logic.fileRouting import Create_Home_Dir
import json
import os

# i want the user to have the abilty to make files/dir with the file sys

class User:
    
    def __init__(self, username: str ="", password: str ="") -> None:
        self.username = None
        self.password = None
        
    def loginUser(self):
        if not os.path.exists("Data/data.json"):
            print("File not found...")
            return False
        
        with open("Data/data.json")as f:
            user_list = json.load(f)
        
        for attempt in range(3):
            self.username = input("Enter Username: ").lower()
            self.password = input("Enter Password: ").lower()
        
            for user in user_list:
                if self.username == user["Username"] and self.password == user["Password"]:
                    print("Login Succesfully")
                    return True
                    
            print("User not found...")
            
        print("Too many failed attempts...")
        return False
            
    
    def signupUser(self):
        try:
            with open("Data/data.json", "r") as f:
                user_list = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            user_list =[]
            
        while True:
            firstName = input("Enter First Name: ").lower()
            lastName = input("Enter Last Name: ").lower()
            username = input("Create Username: ").lower()
            password = input("Create Password: ").lower()
        
            if len(username) > 8 and len(password) > 8:
                print("Username and Password can't be longer that 8 characters")
                return
            elif len(username) > 8:
                print("Username can't be longer than 8 characters")
                continue
            elif len(password) > 8:
                print("Password can't be longer than 8 characters")
                continue
            
            if any(user["Username"] == username for user in user_list):
                print("Username already exist")
                continue
                
            confirm_password: str = input("Comfirm Password: ").lower()
            if password != confirm_password:
                print("Password does not match...")
                continue
        
            userDict = {
                "FirstName": firstName,
                "LastName": lastName,
                "Username": username,
                "Password": password,
            }
        
            user_list.append(userDict)
        
            with open("Data/data.json", "w") as f:
                json.dump(user_list, f, indent=4)
                
            self.home = Create_Home_Dir(username)
            self.username = username
            self.password = password
            
            print("User Created Successfully...")
            return True