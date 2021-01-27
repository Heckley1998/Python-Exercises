pin = 1234

print("Welcome to the bank of Mitchell.")
choice = int(input("Enter your pin: "))

print()

if choice == pin:
    print("Your pin has been accepted")
else:
    print("Incorrect pin")
