'''
Chris Everhart
January 21, 2026
ITMD 413
'''

bankBalance = 0.0
intRate = 0.0
pin = "1234"
secured = False
attempts = 0

while not secured and attempts < 3:
        userPin = input("Enter your PIN: ")
        if userPin == pin:
            
            secured = True
            bankBalance = float(input("Enter your starting bank balance: "))
            initial_balance = bankBalance
            intRate = float(input("Enter your annual interest rate as a decimal: "))
            for index in range (1, 13):
                bankBalance += bankBalance * (intRate / 12)
                print(f"Month {index}:\t ${bankBalance:.2f}")

            bankBalance = initial_balance
            print("\nSummary statement:")
            print("Month #\t Interest Amt\t Balance")
            for i in range(1, 13):
                interest = bankBalance * (intRate / 12)
                bankBalance += interest
                print(f"{i}\t ${interest:.2f}\t\t${bankBalance:.2f}")
        else:
            print("Incorrect PIN. Please try again.")
            attempts += 1
            print(f"You have {3 - attempts} attempts left.")

