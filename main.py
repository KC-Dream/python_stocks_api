#import requests

import sys
import gui

#pip3 install package_name --user

#Get User Input
def check_input():
    print("checking input...")

    #If user has not quit yet
    while True:

        user_input = input("Enter \"q\" or \"quit\" to exit the program. Enter the Stock Symbol you would like to search for: ")
        print(f"You entered: {user_input.upper()}")

        if user_input == "q" or user_input == "quit":
            print("Exitting program...")
            sys.exit()
        else:
            print("Running the program...")
            #getdata.get_data(user_input)
            gui.run_gui(user_input)



check_input()




