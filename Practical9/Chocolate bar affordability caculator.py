def calculate(total_money, price):
    numbers=total_money//price
    change=total_money%price
    return numbers, change

total_money=100
price=7
numbers, change = calculate(total_money, price)
print(numbers,change)