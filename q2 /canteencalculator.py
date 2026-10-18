def calculate_total(price, quantity):
    total = price * quantity
    return total


def calculate_change(payment, total):
    if payment >= total:
        return payment - total
    else:
        return total - payment


price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

total_cost = calculate_total(price, quantity)

amount = calculate_change(payment, total_cost)

print(f"Total Cost: PHP {total_cost:.2f}")

if payment >= total_cost:
    print(f"Change: PHP {amount:.2f}")
else:
    print(f"Additional amount needed: PHP {amount:.2f}")


#1:
# calculate_total() calculates the total purchase cost.
# calculate_change() calculates the change or shortage.

#2:
# Parameters are variable names in a function definition,
# such as price and quantity.
# Arguments are the actual values passed to a function,
# like as calculate_total(35, 3).

#3:
# The returned total is stored in total_cost.
# It is reused in calculate_change(payment, total_cost)
# and displayed as the total purchase cost.

#4:
# Separating the calculations makes the program easier to
# read, understand, test, and maintain.
