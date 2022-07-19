print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
# initialize empty meal dictionary
menu = {
    'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
    'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A literal Garden': 0},
    'Desserts': {'Ice Cream': 0, 'Cake': 0, 'Pie': 0},
    'Drinks': {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0},
}
# start  loop here until user enters quit
answer = input().lower().capitalize()

while answer != 'Quit':

    for key in menu.keys():

     if answer in menu[key].keys():

    menu[key][answer]+= 1

    if menu[key][answer] ==1:
        print(f'** {menu[key][answer]} order of {answer} has been added to your meal **')
        break
    else:
        print(f'** {menu[key][answer]} orders of {answer} have been added to your meal **')
        break
else:
 print('** Item is unavailable, please order another item from our menu **')

answer = input().lower().capitalize()



