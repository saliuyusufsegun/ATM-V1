import sys

balance="$1000"
pin=1234
attempts=0

while attempts<3:
    entered_pin=int(input("Enter your pin: "))
    if entered_pin==pin:
        print("Access granted!")
        break
    else:
        attempts+=1
        print(f"Try again. Attempt {attempts}/3")
else:
    print("Card blocked, contact customer care")
    sys.exit()
while True:
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    option=int(input("Enter option: "))
    if option==1:
        print(f"Your balance is {balance}")
    elif option==2:
        amount=int(input("Enter deposit amount: "))
        balance+=amount
        print(f"Your deposit of ${amount} was successful, and your new account balance is ${balance}")
    elif option==3:
        amount=int(input("Enter withdrawal amount: "))
        if amount<balance:
            balance-=amount
            print(f"Your withdrawal of ${amount} was successful and your new account balance is ${balance}")
        else:
            print("Insufficient funds")
    elif option==4:
        print("Thank you! Take your card.")
        break
    else:
        print("Invalid option")