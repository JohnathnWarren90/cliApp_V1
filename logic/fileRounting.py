import os
import shutil
import sys

BASE_PATH = "UserFiles"

def Create_Home_Dir(username):
    path = os.path.join(BASE_PATH, username)
    
    os.makedirs(path, exist_ok=True)
    return path

def create_dir(user_home, dirName):
    path = os.path.join(user_home, dirName)
    os.makedirs(path, exist_ok=True)
    
    return path

def create_file(user_home, filename):
    os.makedirs(user_home, exist_ok=True)
    path = os.path.join(user_home, filename)
    with open(path, "w") as f:
        f.write("")
        
    return path

def list_user_dir(user_home):
    return os.listdir(user_home)

def delete_file(user_home, filename):
    path = os.path.join(user_home, filename)
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
        return True
    return False

def remove_dir(user_home, dir_name):
    path = os.path.join(user_home, dir_name)

    if not os.path.exists(path) or not os.path.isdir(path):
        print(f"Directory '{dir_name}' does not exist.")
        return False

    contents = os.listdir(path)
    if contents:
        print(f"Directory '{dir_name}' is not empty. It contains:")
        for item in contents:
            print(f" - {item}")

    confirm = input(f"Are you sure you want to delete '{dir_name}' and all its contents? (y/n): ").lower()
    if confirm == "y":
        shutil.rmtree(path)
        print(f"Directory '{dir_name}' has been deleted.")
        return True
    else:
        print("Deletion canceled.")
        return False
    