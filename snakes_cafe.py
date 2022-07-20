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
Food_items = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A literal Garden': 0,
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0,
}

# customer order prompt
order = input('> ')


# start  loop here until user enters quit
while order != 'quit':

    if order not in Food_items:
        print('Please order from items available on menu')
        order = input('> ')
        continue
    if Food_items[order] == 0:
        Food_items[order] = 1
        report = f'** {1} order of {order} has been added to your meal **'
        print(report)

    else:
        Food_items[order] += 1
        report = f'** {Food_items[order]} order of {order} has been added to your meal **'
        print(report)

    order = input('> ')







