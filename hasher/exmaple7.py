import hashlib
import os
from platform import system
from turtledemo.chaos import h

''' clear method to clear every thing on the screan'''
def clear():
    if system() == 'linux':       # if the system is linux we use clear command
        os.system('clear')
    if system() == 'windows':     # if the system is windows we use the command cls
        os.system('cls')
clear()   # here we call the function clear
banner ='''    ___
    /  \      /   \
    |  |      |   |
    |  |______|   |                 
    |  |______|   |
    |  |      |   |
    |  |      |   |
    |  |      |   |
    |  |      |   |
    \__|      \___|

'''
print(banner)

# function to ask the user if he wont to contiune or not
def ext():
    ex = input("continue/exit c/e ->")
    if ex[0].upper() == 'E':      # if the user enter the letter e we exit
        print('exiting')
        exit()
    else:                      # if the user enter any thing but e
        clear()                 # clear any thing
        print(banner)         # print the banner
        menu()               # call the menu method
        chocie()            # call the choice method

''' function to print the menu information'''
def menu():
    print('''
    1 >> md5 encode
    2 >> sha1 encode
    3 >> sha256 encode
    4 >> sha520 encode
    5 >> Exit
    ''')
menu()


''' function to ask the user to enter choice '''
def chocie():
    co =input("please enter your choice ->")
    if co == '1':            # if the choice is 1 run the md5 method
        md5()
    elif co == '2':          # if the choice is 2 run the sha1 method
        sha1()
    elif co == '3':         # if the choice is 3 run the method sha256
        sha256()
    elif co == '4':         # if the choice is 4 run the method sha512
        sha512()
    elif co == '5':         # if the choice is 5 print something and run exit function
        print("Exiting")
        exit()

''' method to generate md5 hash'''
def md5():
    clear()
    hs = input("please enter text to encode ->")
    h =hashlib.md5(hs.encode())
    print(h.hexdigest())    # retur the hashed text in hex formate
    ext()

'''method to genarete hash in sha1'''
def sha1():
    clear()
    hs =input("please enter the text to encode ->")
    h =hashlib.sha1(hs.encode())
    print(h.hexdigest())
    ext()

''' function to generate sha256 hash'''
def sha256():
    clear()
    hs =input("please enter the text to encode ->")
    h =hashlib.sha256(hs.encode())
    print(h.hexdigest())
    ext()

''' function to generate  sha 512 hash'''
def sha512():
    clear()
    hs =input("please enter text to encode  ->")
    h =hashlib.sha512(hs.encode())
    print(h.hexdigest())
    ext()
chocie()


1





















