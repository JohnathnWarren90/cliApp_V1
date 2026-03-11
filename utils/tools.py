import os

def clear_screen():
    # Windows uses 'cls', Unix/Mac uses 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')