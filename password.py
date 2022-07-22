
import random
import string
import csv

accounts = []
usernames = []
passwords = []


def main():

    print('Password Generator')

   
    option = 0
    # menu to get information from user
    while option !=4:
        print("\n---------------------------------------------\n"
        "Please select one of the following:\n"
        "1. Generate a random password\n"
        "2. List all passwords created\n"
        "3. Save your passwords in a file\n"
        "4. Quit\n")

        option = input('Please enter an action: ')
        # generate a random password
        # store accounts and usernames from input
        if option.isnumeric() == True:
            option_number = int(option)
            if option_number == 1:
                account = input("\nTo what account do you want a password? ")
                accounts.append(account)
                username = input("What's your username for that account? ")
                usernames.append(username)
                
                pass_length = check_pass_length()
                password = ""
                characters = get_choice(password)
        
                get_password(password, characters, pass_length)
            # print a list with account, username and password    
            elif option_number == 2:
                print_lists(accounts, usernames, passwords)
            # save the list in a csv file     
            elif option_number == 3:
                save_passwords(accounts, usernames, passwords)
            # end application       
            elif option_number == 4:
                print('Thank you. Goodbye.') 
                break
        # certify if the user is typing a valid number   
        else:
            print("Please enter a valid number.")      

       

def check_pass_length():
    # check if the length of the password is a valid number and convert input to interger
    # parameters: none
    # return: the number of the password length choice 
    while True:
        pass_length = input("How many characters do you want for this password? ")
        if pass_length.isdigit() == False or int(pass_length) <= 0:
            print("Please type a valid number")
        else:
            pass_length = int(pass_length)
            break
    return pass_length

def get_choice(password):
    # get the user's choice if the password will have lowercase, uppercase, numbers or symbols, 
    # start the creation of the password to secure at least one character of each choice
    # parameters: the initial variable password = ""
    # return: variable with the string method for each one of the choices 
    choice_input1 = input(f"Do you want lowercase letters (Yes/No)? ")
    if choice_input1.lower() == "yes":
        string1 = string.ascii_lowercase
        password += random.choice(string.ascii_lowercase)
    else:
        string1 = ""

    choice_input2 = input(f"Do you want uppercase letters (Yes/No)? ")
    if choice_input2.lower() == "yes":
        string2 = string.ascii_uppercase
        password += random.choice(string.ascii_uppercase)
    else:
        string2 = ""

    choice_input3 = input(f"Do you want numbers (Yes/No)? ")
    if choice_input3.lower() == "yes":
        string3 = string.digits
        password += random.choice(string.digits)
    else:
        string3 = ""

    choice_input4 = input(f"Do you want symbols (Yes/No)? ")
    if choice_input4.lower() == "yes":
        string4 = string.punctuation
        password += random.choice(string.punctuation)
    else:
        string4 = ""

    characters_source = string1 + string2 + string3 + string4
    return characters_source


def get_password(password, characters_source, pass_length):
    # finish the creation of the password according the length chosed
    # storer password created in passwords list
    # parameters: 
    #  "password" - result from get_choice function
    #  "characters_source - result from get_choice function
    #  "pass_lenght" - result from the check_pass_length function
    # return: password 
    for i in range(pass_length - len(password)):
        password += random.choice(characters_source) 

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    passwords.append(password)
    print("\n Your random password is:", password)
    return password

def print_lists(accounts, usernames, passwords):
    # create a list with the accounts, usernames and passwords stored
    # print the list
    # parameters: 
    #  accounts, usernames and passwords
    # return: nothing 
    rows = list(zip(accounts, usernames, passwords))
    for i, j, k in rows:
        print(f"Account: {i}, Username: {j}, Password: {k}")

def save_passwords(accounts, usernames, passwords):
    # create a csv file with Account, Username and Password as fields
    # return: nothing 
    rows = list(zip(accounts, usernames, passwords))
    with open('passwords.csv', 'w') as f:
        fields = ["Account", "Username", "Password"]
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(rows)
    print("Your passwords were saved on the passwords.csv file")

if __name__ == "__main__":
    main()
