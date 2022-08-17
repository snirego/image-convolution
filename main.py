# ------------------------------------------------------------
# Files we should create:
#  -| main.py
#  ---| sign_up.py
#  ---| sign_in.py
#  ---| create_password.py
#  ---| game.py
# ------------------------------------------------------------
# import files
from curses import def_prog_mode
from distutils import ccompiler
from distutils.errors import DistutilsFileError
from fcntl import F_FULLFSYNC
from genericpath import exists
from multiprocessing.resource_tracker import getfd
from multiprocessing.util import DEFAULT_LOGGING_FORMAT

if exists("sign_up.py"):
    from sign_up import *

if exists("sign_in.py"):
    from sign_in import *

if exists("create_password.py"):
    from create_password import *

if exists("game.py"):
    from game import *
# ------------------------------------------------------------
# main function
def main():
    print("Welcome to the game!")
    print("Please choose an option:")
    print("1. Sign up")
    print("2. Sign in")
    print("3. Create password")
    print("4. Play game")
    print("5. Exit")
    option = int(input("Please enter your option: "))
    if option == 1:
        sign_up()
    elif option == 2:
        sign_in()
    elif option == 3:
        create_password()
    elif option == 4:
        game()
    elif option == 5:
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid option!")
        main()