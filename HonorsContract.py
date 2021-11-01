################################################
#Honors Contract
#Name: Craig Spencer
#Lecture: T, Th 4:30
#Description: This program uses a binary search tree to store
# peoples names and emails. It also gives each file a
# randomly generated number to be accessed by.
################################################

import random

#Defines what is contained in each persons data file
#Each data file will act as a node in the binary search tree
class dataFile:
    def __init__(self, userId = None, name = None, email = None):
        self.userId = userId
        self.name = name
        self.email = email
        self.left = None
        self.right = None

#Defines a function that will allow the user to add data files to the tree
def addFiles(headFile):

    userName = input("Name of file: ")
    userEmail = input("Enter an email: ")

    userId = 50
    while (findFile(headFile, userId) != None):
        userId = random.randint(1,100)
    
    print("This users id is", userId)

    temp = dataFile(userId, userName, userEmail)
    placeInTree(headFile, temp)
    
    #Asks the user if they would like to input another file
    userInput = ""
    while (userInput != "n"):
        userInput = input("Add another file? (y/n)  ")
        print ("")
        
        if (userInput == "y"):
            addFiles(headFile)
            break
        elif (userInput != "n"):
            print("Invalid choice")

#Defines how to add a file into the binary tree
#Used by the addFiles function
def placeInTree(headFile, newFile):
    pointer = headFile

    loop = True
    while (loop):
        if (newFile.userId < pointer.userId):
            if (pointer.left == None):
                pointer.left = newFile
                loop = False
            else:
                pointer = pointer.left   
        else:
            if (pointer.right == None):
                pointer.right = newFile
                loop = False
            else:
                pointer = pointer.right

#Searches for a file given an id and returns the file it finds
def findFile(headFile, key):
    pointer = headFile

    loop = True
    while (loop):
        if (key == pointer.userId):
            return pointer
        
        if (key < pointer.userId):
            if (pointer.left == None):
                loop = False
                return None
            else:
                pointer = pointer.left   
        else:
            if (pointer.right == None):
                loop = False
                return None
            else:
                pointer = pointer.right


#Uses the findFile method to display a File given a key
def searchFile(headFile):
    inputKey = int(input("Enter a key value to search for: "))
    keyFile = findFile(head, inputKey)

    if (keyFile == None or inputKey == 50):
        print("No File Found")
    else:
        print("File", inputKey, "Found")
        print("Name:", keyFile.name)
        print("Email:", keyFile.email, "\n")

    #Asks the user if they would like to search for another file
    userInput = ""
    while (userInput != "n"):
        userInput = input("Search for another file? (y/n)  ")
        print ("")
        
        if (userInput == "y"):
            searchFile(headFile)
            break
        elif (userInput != "n"):
            print ("Invalid choice")

    
    

#Searches for a file given an id and deletes said file
def removeFiles(headFile):
    pointer = headFile

    inputKey = int(input("Enter the key of the file you wish to delete: "))
    keyFile = findFile(head, inputKey)

    if (keyFile == None or inputKey == 50):
        print("No File Found")
    else:
        #Calls recursive function that deletes the node
        delete(keyFile)

    #Asks the user if they would like to delete another file
    userInput = ""
    while (userInput != "n"):
        userInput = input("Delete another file? (y/n)  ")
        print ("")
        
        if (userInput == "y"):
            removeFiles(headFile)
            break
        elif (userInput != "n"):
            print ("Invalid choice")

        
#Helper function to removeFiles()
def delete(file):
    if (file.right != None):
        file.userId = file.right.userId
        file.name = file.right.name
        file.email = file.right.email
        delete(file.right)
    elif (file.left != None):
        file.userId = file.left.userId
        file.name = file.left.name
        file.email = file.left.email
        delete(file.left)
    else:
        free(head, file)

#Helper function to delete
def free(headFile, fileToFree):
    pointer = headFile

    loop = True
    while (loop):
        if (pointer == None):
            loop = False

        else:
            #Free node if found
            if (pointer.right != None):
                if (pointer.right.userId == fileToFree.userId):
                    if (pointer.right.right == None and pointer.right.left == None):
                        pointer.right = None
                    else:
                        pointer.right.right = None
                        pointer.right.left = None
                    loop = False
            elif (pointer.left != None):
                    if (pointer.left.right == None and pointer.left.left == None):
                        pointer.left = None
                    else:
                        pointer.left.right = None
                        pointer.left.left = None
                    loop = False
                    
            #Traverse tree
            if (fileToFree.userId < pointer.userId):
                if (pointer.left == None):
                    loop = False
                    return None
                else:
                    pointer = pointer.left   
            else:
                if (pointer.right == None):
                    loop = False
                    return None
                else:
                    pointer = pointer.right


#main

#Creates a data File that will act as the starting point for the binary search tree
head = dataFile(50, "No Name", "No Email")

option = '?'
while (option != 'D'):

    print("\nOptions: Enter the letter to perform the action")
    option = input("A - Add Files \nB - Search Files \nC - Delete Files \nD - Quit\n").upper()
    print ("")

    if (option == 'A'):
        addFiles(head)
        print ("Files added\n")
    elif (option == 'B'):
        searchFile(head)
    elif (option == 'C'):
        removeFiles(head)
        print ("File(s) deleted")    
    elif (option != 'D'):
        print ("Invalid action")
        

print("done")
