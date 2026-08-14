def convert_currency(amount, unit):
    """
    Converts currency between THB and USD.
    Exchange rate: 1 USD = 32 THB
    """
    rate = 32

    if unit == "THB":
        
        converted = amount / rate
        print(f"{amount} THB = {converted:.2f} USD")
        return converted
    elif unit == "USD":
       
        converted = amount * rate
        print(f"{amount} USD = {converted:.2f} THB")
        return converted
    else:
        print("Error: unit must be 'THB' or 'USD'")
        return None

convert_currency(100, "THB")   
convert_currency(100, "USD")   
convert_currency(3.13, "USD")  