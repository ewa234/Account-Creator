def generateUsername(fullName, startYear):
    #this subroutine will generate the username 
    #based on the students' first name, last name 
    #and their starting year
    #turn Ronald smith and 2022 into 22SmithR
    firstName = (input("enter your first name "))
    lastName = str(input("enter your last name "))
    startYear = str(input("enter your starting year"))
    print(startYear[2:4]+lastName+firstName[0]) 
    username = "#######"
    return username

def calculateYearGroup(username):
    #this subroutine will calculate the year group
    startYear= int(input("enter your starting year "))
    currentYear = int(input("enter the current year"))
    yearGroup = (currentYear - startYear )
    print("you've spent ",yearGroup ,"years")
    if yearGroup <= 1:
        print(" you are in year 7")
    elif yearGroup <= 2 :
        print(" you are in year 8")
    elif yearGroup <= 3 :
          print(" you are in year 9")
    elif yearGroup <= 4:
        print(" you are in year 10")
    elif yearGroup <= 5:
        print (" you are in year 11")
    elif yearGroup <= 6:
        print(" you are in year 12")
    elif yearGroup <= 7 :
        print(" you are in year13")
    else:
        print("you are not in a year group")
    
    #that the student is in based on their username
    yearGroup = "Year #"
    return yearGroup

def getPassword():
    #this subroutine will ask the user to enter a password 
    #and pass it to the isPasswordSecure subroutine to 
    #check if it is secure
    password = input("enter a password: ")
    while isPasswordSecure(password) == False:
        password = input("password was not secure, please try again: ")
    return password

def isPasswordSecure(password):
    #this password will return True if the password meets
    #all the required conditions and False if it does not
    return True

def menu():
    fullName = print("welcome ")
    startYear = print("you would be prompted some question please answer correctly")
    username = generateUsername(fullName, startYear)
    yearGroup = calculateYearGroup(username)
    password = getPassword()
    
menu()