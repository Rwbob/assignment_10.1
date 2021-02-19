# A program that validates a user-specified directory then writes a file to that directory and reads the file back for verification.
# Robert Sivadon
# 02-21-2021


import os, csv

# Welcome message
print("\nWelcome to Python file reader and writer.")

def use_user_dir(directory):
# Asks user if validated directory is to be used to save file, if yes sends directory to user_file_name()
    while True:
        print("Would you like to use this directory to save your file?")
        selection=input("Type 'y' to use directory, or 'n' to choose another: ").lower()
        if selection == 'y' or selection == "yes":
            user_file_name(directory)
            break
        elif selection == 'n' or selection == 'no':
            print()
            main()
        else:
            print("\nSorry, that is not a valid input try again!\n")

def user_file_name(directory):
# prompts user for file name, stores directory and file name into one variable to be passed in write_to_file()
    file_name=input("\nFile name:  ")
    full_path= directory + file_name
    print(f"\n-----Writting '{file_name}'------\n" + full_path)
    write_to_file(full_path)

def write_to_file(full_path):
# prompts user for name, address, and phone number, then writes to file
    with open(full_path,'w') as f:
        u_name= input("\nPlease provide your name: ")
        u_address=input("Please provide your address: ")
        u_phone=input("Please provide your phone number: ")
        x=csv.writer(f,delimiter=',')
        x.writerow([u_name,u_address,u_phone])
        f.close()
        read_file(full_path)

def read_file(full_path):
# prints file for user validation
    with open (full_path, 'r') as f:
        print()
        for line in f.readlines():
            print(line.strip())
    validate_info(full_path)

def validate_info(full_path):
# User input for validation, if correct program ends, if not, write_to_file() runs
    while True:
        v_info=input("Is the above information correct?\n"
        "type 'y' for yes or 'n' to correct: ").lower()
        if v_info == "y" or v_info == 'yes':
            print("\nYour file has been written, thank you and good bye!")
            exit()
        if v_info == 'n' or v_info == 'no':
            write_to_file(full_path)
        else:
            print("\nSorry, that is not a valid input try again!")

def main():
# Beginning of program
# Validate a directory exsits. If not, stays active until user finds a working directory
    while True:
        directory=input("Please enter the directory where the saved file will be located\n"
        "(Please end path with '/' to avoid storing file in wrong directory): ")
        validate_dir=os.path.isdir(directory)
        if validate_dir == True:
            print("\nDirectory Found!\n")
            use_user_dir(directory)
        if validate_dir == False:
            print('\nDirectory not found, please try again\n')
main()