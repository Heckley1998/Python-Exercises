""" Library """

import os
import time

# login screen

# login validation

# logout

# class book

# class CD

# class user


books = [{'title': 'Harry Potter', 'author': 'J.K.Rawling', 'date': 2004 }, {'title': 'Bible', 'author': 'J.Christ', 'date': 32}, {'title': 'PhD for Dummies', 'author': 'Andrew Dockerty', 'date': '2015'}]

cd  = [{'title': 'The Joshua Tree', 'author': 'U2', 'date': 1987 } , {'title': 'Greatest Hits', 'author': 'Now', 'date': 2010 }, {'title': 'Physical Graffiti', 'author': 'Led Zeppelin', 'date': 1975 }]

choice = 'Harry Potter'
for i in books:
    title = i.get('title')
    if title == choice:
        print("Is this your book?", i )
    

def login_screen():

    os.system('clear||cls')

    print("\t=================")
    print("\tNewcastle Library")
    print("\t=================\n")
    
    username = input("\tWhat is your username? ")
    password = input("\tWhat is your password? ")
    

    details = [username, password]
    login_validation(details)

def login_validation(details):
    username = details[0]
    password = details[1]

    try:
       f = open("database.txt", "r")
       logins = f.read()
       logins = logins.split('\n')

       if username in logins:
        
           os.system('clear||cls')
           # add logout here
           print()
           print("\n\t1. Rent a book")
           print("\t2. Rent a CD")
           print("\t3. Return a book")
           print("\t4. Return a CD")

           option = input(">")

           if option == '1':
               # book input
               title = input("What is the book title? ")

            #    author = input("Who is the author of the book? ")
            #    date = input("What date was this book released?")

               for i in books:
                   if title in i:
                       print("I found your book")
                   else:
                       print("Didn't find it.")
                   
            
            #    if title in books[]: 
            #        print("Is this the book: ")
            #    title
           elif option == '2':
               # cd input
               title = input("What is the CD title? ")
               author = input("Who is the author or this CD? ")
               date = input("What date was this book released?")
               cd = CD()
               cd.title(user_input())
               cd.date(user_input())
               cd.author(user_input())
           elif option == '3':
               title = input("What is the book title? ")
               # return book input
               book = Book()
               book.title(user_input())
           elif option == '4':
               # return cd input
               title= input("What is the title of the CD?")
               book = Book()
               book.title(user_input())
           else: 
                print("Input Error")
       else:
           f = open("database.txt", "a")
           f.write(username + "\n")
           f.write(password + "\n")
           f.close()

           print("\tDatabase updated. New user created!")
           print("\t\tPlease Login")

           username = input("\tWhat is your username? ")
           password = input("\tWhat is your password? ")

           os.system('clear||cls') 
           print("Please provide extra details.")
           name = input("\n\tYour name: ")
           age = input("\tYour age: ")
           address = input("\tYour address: ")

           user1 = User(username, password, name, age, address)
           time.sleep(2)
           login_screen()
            

    except FileNotFoundError:
       pass 


def logout():
    question = input("Would you like to logout? (y,n): ")
    if question == 'y':
        pass
    else:
            # something else
        pass

def user_input():
    user_input = input()

class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def rent_item():
        pass

    def return_item():
        pass

class Book(object):
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date

class CD:
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date

# if __name__ == "__main__":
#     login_screen()
