import random
import datetime
import sqlite3

conn = sqlite3.connect('test.db') # this line creates db or opens one if exists

""" This line creates table. It only needs to be run once. """

print("Opened database successfully")

# conn.execute('''Create Table Results
#          (ID INT PRIMARY KEY NOT NULL,
#          result TEXT NOT NULL);''')
# conn.close()

x = datetime.datetime.now() # this line gets current date and 
                            # stores it in variable x

num = random.randint(1, 100) # this line creates random num 
tries = 1
result = 0
# print(num)
print("Welcome back, your previous score was:")
#f = open("guess.txt", "r")
#print(f.read())
print("Guess the number between 1 and 100!")

db_value = ''

guess = int(input("Your guess: "))
if guess < 1 or guess > 100:
    print("Invalid guess. Range from 1 - 100")
    tries - 1

while guess != num:
    print("That is incorrect, guess again!")
    if guess  > num:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    guess = int(input("Your guess: "))
    if guess < 1 or guess > 100:
        print("Invalid guess. Range 1 - 100") 
        tries - 1
    if guess == num:
        print("You Got it!")
        print(x.strftime("%x"))
        db_value = ('You got it', x)
        result = 1
    tries +=1
    if tries == 3:
        print("You suck")
        print(x.strftime("%x"))
        db_value = ('You suck', x)
        result = 0 
        break


conn.execute("INSERT INTO Results (ID, result) VALUES ('1', 'Radek')")

conn.commit()
print("Records created successfully")
conn.close()

""" save to txt file code """
f = open("guess.txt", "a")
if result == 1:
    f.write("You guessed it")
    f.write(x.strftime("%x"))
else:
     f.write("You Suck")
     f.write(x.strftime("%x"))
