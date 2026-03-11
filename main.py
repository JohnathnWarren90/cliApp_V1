from model.user import User
from logic.fileRounting import create_file, list_user_dir, create_dir, remove_dir, delete_file
from utils.tools import clear_screen

def main():
    user = User()
    
    while True:
        print("\n1. Signup\n2. Login\n3. Exit")
        choice = input("> ")

        if choice == "1":
            if user.signupUser():
                user_session(user)
        elif choice == "2":
            if user.loginUser():
                user_session(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


def user_session(user):
    clear_screen()
    
    while True:
        print("Commands: Create_File: mkfl, Create_Directory: mkdir, List: li, Remove_File: rmfl, Remove_Directory: rmdir, Exit: q")
        cmd = input(f"{user.username}@UserFiles:{user.home} >> ").lower()
    
        if cmd == "mkfl":
            fileName = input("Name File: ")
            path = create_file(user.home, fileName)
            print(f"File: {fileName} created at: {path}")
        elif cmd == "mkdir":
            folder = input("Enter Directroy Name: ")
            path = create_dir(user.home, folder)
            print(f"Folder: {folder} created at: {path}")
        elif cmd == "rmfl":
            file = input("Which File: ")
            success = delete_file(user.home, file)
            if success:
                print(f"File: {file} Successfully Deleted")
            else:
                print(f"File: {file} not found...")
        elif cmd == "rmdir":
            folder = input("Enter Directory Name: ")
            success = remove_dir(user.home, folder)
            if success:
                print(f"Directory: {folder} Successfully Deleted")
            else:
                print(f"Directory: {folder} not found...")            
        elif cmd == "li":
            files =list_user_dir(user.home)
            if not files:
                print("Directory is empty")
            else:
                print("Files: ")
                for f in files:
                    print(f"- {f}")
                    
        elif cmd == "q":
            print("Logging out...")
            return
        else:
            print("Unknown Command")
    
if __name__ == "__main__":
    main()