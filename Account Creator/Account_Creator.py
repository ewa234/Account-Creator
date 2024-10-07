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
    startYear= int(input("enter your starting year i.e *2022"))
    currentYear = int(input("enter the current year"))
    yearGroup = (currentYear - startYear )
    print("you've spent ",yearGroup ,"years")
    if yearGroup is 1:
        print("year 7")
    elif yearGroup is 2 :
        print("year 8")
    elif yearGroup is 3 :
          print("year 9")
    elif yearGroup is 4:
        print("year 10")
    elif yearGroup is 5
    
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