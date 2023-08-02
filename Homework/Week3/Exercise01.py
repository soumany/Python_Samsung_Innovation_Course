print('#' * 50)
print('This is Many fruit shop')
print('1: Apple (Price: 5000 won)')
print('2: Grape (Price: 6000 won)')
print('3: Melon (Price: 8000 won)')
print('4: Orange (Price: 2000 won)')
print('#' * 50)

total_price = 0

while True:
    order = input('Enter item number (between 1~4) >> ')
    
    if not order.isdigit():
        print('Invalid input. Please enter a number.')
        continue
    
    order = int(order)
    
    if order < 1 or order > 4:
        print('Invalid input. Please enter a number between 1 and 4.')
        continue
    
    break

while True:
    count = input('Enter number of items (between 1~10) >> ')
    
    if not count.isdigit():
        print('Invalid input. Please enter a number.')
        continue
    
    count = int(count)
    
    if count < 1 or count > 10:
        print('Invalid input. Please enter a number between 1 and 10.')
        continue
    
    break

if order == 1 :
    fruit = 'Apple'
    price = 5000
elif order == 2:
    fruit = 'Grape'
    price = 6000
elif order == 3:
    fruit = 'Melon'
    price = 8000
elif order == 4:
    fruit = 'Orange'
    price = 2000

print('Fruit selected:', fruit)
print('Price:', price)
print('Quantity:', count)
print('Total price is', price * count, 'won')

while True:
    money = input('Insert money please (ex: 15000) >>> ')
    
    if not money.isdigit():
        print('Invalid input. Please enter a number.')
        continue
    
    money = int(money)
    
    if money < price * count:
        print('Not Enough Money.')
        continue
    
    break

change = money - price * count
print(money, 'won received. Your change is', change, 'won')

num_200_won = change // 200
num_100_won = (change % 200) // 100

print('Number of 200 won notes:', num_200_won)
print('Number of 100 won notes:', num_100_won)
