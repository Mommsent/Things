def order_shirt():
    print('Hello! You can choose what shitr do you wont to order.', '\nYou can order standart shirt or castom',
          '\nWrite 1 if you wont to choose standart shirt or 2 if castom')
    user_choose = int(input())
    if user_choose == 1:
        generate_shirt()
        print('Your order: Size - "L", Color - "Green", Text - "I love Python"')
    elif user_choose == 2:
        make_shirt()

def generate_shirt():
    print('You choose standart tshirt.')
    order = 'User_order.txt'
    with open(order, 'w') as file_object:
        file_object.write('Size - "L", Color - "Green", Text - "I love Python"')

def make_shirt():
    print('Choose which one tshirt size you want.', 'Exemple: "L", "M", "XL"')
    user_size = input()
    if user_size == 'L':
        print('You choose size "L".')
    elif user_size == "M":
        print('You choose size "M".')
    elif user_size == "XL":
        print('You choose size "XL"')
    else:
        print('You write wrong incorrect value? pleas try again!')
    print('\nNow we choose a color. We have Green, Pink, Red, Blue. ')
    user_color = input()
    if user_color == 'Green':
        print('You choose green color.')
    elif user_color == "Pink":
        print('You choose pink color.')
    elif user_color == "Red":
        print('You choose red color.')
    elif user_color == 'Blue':
        print('You choose blue color.')
    else:
        print('You write wrong incorrect value? pleas try again!')
    print('What do you want to write on a shirt?')
    user_text = input()
    print('You write ' + user_text)
    print('Order is confirmed and issued')
    order = 'User_order.txt'
    with open(order, 'w') as file_object:
        file_object.write('Size - ' + user_size + ', color - ' + user_color + ', text - ' + user_text)
    print('Size - ' + user_size + ', color - ' + user_color + ', text - ' + user_text)


order_shirt()