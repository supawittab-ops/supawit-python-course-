print("Enter prices of 6 items:")
pricee = []
for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    pricee.append(price)

print()

budget = int(input("Enter total budget: "))
print()

current_total = 0
bought_items = []

for i in range(6):
    item_price = pricee[i]
    
    if current_total + item_price <= budget:
        print(f"Item {i+1} = {item_price} -> buy")
        current_total += item_price       
        bought_items.append(item_price)   
    else:
        
        print(f"Item {i+1} = {item_price} -> cannot buy")
    
    print(f"Current total = {current_total}")
    print() 

print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {budget - current_total}")