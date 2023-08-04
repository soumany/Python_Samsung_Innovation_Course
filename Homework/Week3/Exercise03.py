print('Welcome to Yummy Restaurant. Here is the menu.')
print('- Burger (enter b)')
print ('- Chicken (enter c)')
print ('- Pizza (enter p)')

menu = {
    'b': 'Burger',
    'c': 'Chicken',
    'p': 'Pizza'
}

while True:
    choose = input('Choose a menu (enter b, c, or p): ')
    if choose in menu:
        print('You chose', menu[choose])
        break
    else:
        print('Invalid choice. Enter the menu again.')

