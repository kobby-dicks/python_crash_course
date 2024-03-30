requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}')
    print('Your pizza will be ready in 3 minutes.')
else:
    print('Are you sure you want a plain pizza?')