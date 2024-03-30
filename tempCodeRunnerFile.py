requested_toppings = ['mashroom', 'meat', 'chicken']
for requested_topping in requested_toppings:
    if requested_topping == 'meat':
         print(f"We are out of {requested_topping}.")
    else:
        print(f'{requested_topping} will be added')   
print('Your oder will be ready in 5 minutes.')