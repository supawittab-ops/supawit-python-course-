# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print("Balance:" , balance, "บาท")

        elif choice == "2":
            withdraw = float(input("Amount: "))
            balance = balance - withdraw
        elif choice == "3":
            deposit = float(input("Amount: "))
            balance = balance = balance + deposit

        elif choice == "4":
            break      
        
else:
    print("Invalid PIN")
