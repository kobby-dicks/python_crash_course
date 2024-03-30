weight = 19
if weight < 4:
    metal_to_lift = 0
elif weight <= 18:
    metal_to_lift = 25
elif weight <= 25:
    metal_to_lift = 40
else:
    metal_to_lift= 100
print(f'You can try the {metal_to_lift}kg')