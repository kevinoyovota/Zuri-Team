from time import ctime
from random import choice

customers = [
                {'username': 'Seyi', 'password': 'passwordSeyi', 'accountNo': '0061056218', 'balance': 750000.00},
                {'username': 'Mike', 'password': 'passwordMike', 'accountNo': '7460223510', 'balance': 124500.00},
                {'username': 'Love', 'password': 'passwordLove', 'accountNo': '2312891005', 'balance': 36400.00}
           ]

def register():
    #Choosing a username
    usernameNotAccepted = True
    print("==========================================================\n")
    while(usernameNotAccepted):
        username = input("Please choose a username of at least 4 characters: ")
        for user in customers: # CHeck if the usernname has alreaddy been taken
            if username.lower() == (user["username"]).lower():
                print("'%s' has already been chosen. Try again.\n" % username)
                break
        else:
            if(len(username) >= 4):
                usernameNotAccepted = False


    #Choosing a password
    password = input("\nPlease choose a password of at least 8 characters: ")
    while(len(password) < 8):
        print("Password is less than 8 charaacters.")
        password = input("\nPlease choose a password of at least 8 characters: ")

    confirmPassword = input("\nConfirm your password: ")
    while(confirmPassword != password):
        confirmPassword = input("Passwords don't match. Try again: ")


    #Creating the account number
    accountNumber = ''
    for i in range(10):
        accountNumber += choice('0123456789')

    #Opening deposit
    openingBalance = -1
    while(openingBalance < 0):
        try:
            openingBalance = float(input("\nHow much do you want to deposit in this account? "))
            if(openingBalance < 0):
                print("Your deposit must be greater than zero.")
        except:
            print("Invalid input. Try again.")

    #Create the new account
    customers.append({'username': username, 'password': password, 'accountNo': accountNumber, 'balance': openingBalance})

    #Display new account details
    print("\nNew account created successfully!\n")
    print("Username:\t%s" % username)
    print("Password:\t%s" % password)
    print("Account number:\t%s" % accountNumber)
    print("Balance:\t%.2f Naira" % openingBalance)

    prompt = input("\nDo you want to perform another operation? (y/n) ")
    if(prompt.lower() == 'y'):
        main()
    else:
        return

def login():
    currentTime = ctime()

    #Validating username
    usernameCorrect = False
    print("==========================================================\n")
    while(not usernameCorrect):
        username = input("Enter username: ")
        for user in customers:
            if(username ==  user['username']):
                usernameCorrect = True
                accountIndex = customers.index(user)
                break
        else:
            print("Invalid username. Try again.\n")

    #Validating password
    passwordCorrect = False
    if(usernameCorrect):
        userAccount = customers[accountIndex]
        while(not passwordCorrect):
            password = input("\nEnter password: ")
            if(password == userAccount['password']):
                passwordCorrect = True

            if(passwordCorrect):
                print("\nWelcome %s! It is %s." % (username, currentTime))
                print("Your account balance is %.2f Naira." % userAccount['balance'])
                transaction(userAccount, accountIndex)
            else:
                print("Incorrect password.")
                

def transaction(userAccount, accountIndex):
    print("==========================================================\n")
    print("These are your available options:")
    print("1. Withdrawal")
    print("2. Cash deposit")
    print("3. Complaint")
    print()
    validChoice = False
    while(not validChoice):
        try:
            selectedOption = int(input("Please select an option: "))
            if(selectedOption in [1, 2, 3]):
                validChoice = True
            else:
                print("Invalid selection.\n")
        except:
            print("Invalid selection.\n")

    if(selectedOption == 1): #withdrawal
        print("You selected %d" % (selectedOption))
        withdrawal = int(input("\nHow much would you like to withdraw? "))

        if(userAccount['balance'] >= withdrawal):
            userAccount['balance'] -= withdrawal
            customers[accountIndex] = userAccount
            print("Take your cash.")
        else:
            print("You have insufficient funds in your account.")
            prompt = input("\nDo you want to perform another operation? (y/n) ")
            if(prompt.lower() == 'y'):
                transaction(userAccount, accountIndex)
            else:
                print()
                main()
            
    elif (selectedOption == 2): #Deposit
        print("You selected %d" % (selectedOption))
        print()
        deposit = int(input("How much would you like to deposit? "))
        userAccount['balance'] += deposit
        customers[accountIndex] = userAccount
        print("Your current account balance is %.2f Naira" % userAccount['balance'])
    elif (selectedOption == 3): #Complaint
        print("You selected %d" % (selectedOption))
        complaint = input("\nWhat issue would you like to report?\n")
        print()
        print("Thank you for contacting us!")
    
    prompt = input("\nDo you want to perform another operation? (y/n) ")
    if(prompt.lower() == 'y'):
        transaction(userAccount, accountIndex)
    else:
        print()
        main()
        
    return
    

def main():
    print("==========================================================\n")
    print("Welcome to New Dawn Bank! Select an option.")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    try:
        option = int(input())
    except:
        option = 0

    while option not in [1, 2, 3]:
        try:
            option = int(input("\nInvalid option. Try again: "))
        except:
            option = 0

    if(option == 1):
        register()
    elif(option == 2):
        login()
    elif(option == 3):
        return

main()
print("==========================================================\n")
print("Thank you for banking with us!")

