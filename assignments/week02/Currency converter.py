EXCHANGE_RATE = 35.5  # 1 USD = 35.5 THB

def main():
    print("Currency Converter")
 
    while True:
        print("\n1. THB to USD")
        print("2. USD to THB")
        print("3. Exit")
 
        choice = input("Choose conversion direction (1, 2, or 3): ")
 
        if choice == "3":
            print("Goodbye!")
            break
 
        if choice not in ("1", "2"):
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
 
        amount = float(input("Enter the amount to convert: "))
 
        if choice == "1":
            result = amount / EXCHANGE_RATE
            print(f"\nFormula: USD = THB / {EXCHANGE_RATE}")
            print(f"{amount:.2f} THB = {result:.2f} USD")
        else:
            result = amount * EXCHANGE_RATE
            print(f"\nFormula: THB = USD * {EXCHANGE_RATE}")
            print(f"{amount:.2f} USD = {result:.2f} THB")
 
 
if __name__ == "__main__":
    main()
