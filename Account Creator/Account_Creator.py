def generateUsername(fullName, startYear):
    #this subroutine will generate the username 
    #based on the students' first name, last name 
    #and their starting year
    username = "#######"
    return username

def calculateYearGroup(username):
    #this subroutine will calculate the year group
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
    fullName = input("enter your full name (first and last name separated by a space): ")
    startYear = input("enter your starting year (e.g. 2024):")
    username = generateUsername(fullName, startYear)
    yearGroup = calculateYearGroup(username)
    password = getPassword()
    
#menu()