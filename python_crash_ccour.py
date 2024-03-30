# doing for loops
names = [
    "samuel oklu" , "prince asare" ,"jeremiaj adjetey"
]
for name in names:
    print(f'How are you {name.title()}')
    print("what are you doing today?\n")
print("Alright good night buddies!!")

# using range function under for loops
for values in range(1,8):
    print(values)

# using range to write a list 
scores = list(range(11,21))
#print(scores)
scores.append(21)
print(scores)

Data = []
for value in range(2,11):
    square = value**2 # squares of the numbers in data
    Data.append(square)
print(Data)
#another way to write it is 
Data = []
for value in range(5,21):
    Data.append(value**2)
print(Data)

# finding the min or max of numbers in a list
#List Comprehensions. this helps to build 
#in one single line of code
Data = [value**2 for value in range(2,8)]
print(Data)

Data = [value for value in range(0,250)] #doing just a normal list
print(Data)

# slicing lists 
Data = [value for value in range(1,29)]
print(Data[1:10])

#slicing
names = ['kwame' , 'kojo', 'yaw']
print(f'Has anyone set eyes on {names[-1].title()}?')

# making a copy of a list
names = ['kwame', 'kojo', 'yaw']
attendance = names[:]
print('the list of members who were present')
attendance.append('ama')
print(attendance)

# tuples. these are immutable list. thus the content of a tuple cannot be 
#changed
fixed_manu = ('rice', 'joloff', 'banku')
fixed_manu[0] = 'yam' # if we try to change rice to yam, it is not possible 
#in this case
print(fixed_manu[0].title())

# tuple containing numbers 
numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])


manues = ('rice', 'banku')
for manu in manues:
    print(manues)

# OR
Dimenssions = (100,200)
#print(Dimenssions[0]) this could be done in another way using a loop
#print(Dimenssions[1])
for Dimenssion in Dimenssions:
    print(Dimenssion)

# modifying the original tuple by assigning a new values
Dimenssions = (500,200)
#print(Dimenssions[0]) this could be done in another way using a loop
#print(Dimenssions[1])
for Dimenssion in Dimenssions:
    print(f'the modified dimenssions: {Dimenssion}')


# if statements. looping with if statements 
cars = ['benz' , 'toyota' , 'suzuki', 'bmw']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# conditional tests
# if-else syntax works for two conditions.
banned_users = ['Killman' 'swatman' 'byran']
for banned_user in banned_users:
    if banned_user == 'Killman':
        print(f'{banned_user.title()}, Please add your comment')
    else:
        print('your account has been banned!!')

# using if-else statements
age = 19
if age >= 18:
    print('You are eligible to register') #this works if the test is true
    print('Fill out the form below')
else:
    print('sorry, you are not eligible to register.') #this works if age is less
    print('Try another time.')

# the if-elif-else syntax. it is used to test more than one conditions. 
age = 54
if age < 4:
    print('Your admission cost is $0')
elif age < 18:
    print('Your admission cost is $25')
else:
    print('Your admission cost is £40.')

# still on if-elif-else syntax
weight = 30
if weight < 50:
    print('you have a healthy weight.')
elif weight < 100:
    print('Do a lot more exercise!')
elif weight >= 100:
    print('You are overweight')
else:
    print('You have gained a lot of weight this month.')

#another way to write this is
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

