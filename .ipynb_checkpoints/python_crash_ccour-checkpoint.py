# doing for loops
names = [
    "samuel oklu" , "prince asare" ,"jeremiah adjetey"
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


manus = ('rice', 'banku')
for manu in manus:
    print(manus)

# OR
Dimensions = (100,200)
#print(Dimensions[0]) this could be done in another way using a loop
#print(Dimensions[1])
for Dimension in Dimensions:
    print(Dimension)

# modifying the original tuple by assigning a new values
Dimensions = (500,200)
#print(Dimensions[0]) this could be done in another way using a loop
#print(Dimensions[1])
for Dimension in Dimensions:
    print(f'the modified dimensions: {Dimension}')


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

# using if statements with lists
requested_toppings = ['mushroom', 'meat', 'chicken']
for requested_topping in requested_toppings:
    if requested_topping == 'meat':
         print(f"We are out of {requested_topping}.")
    else:
        print(f'{requested_topping} will be added')   
print('Your oder will be ready in 5 minutes.')

# checking that a requested list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}')
    print('Your pizza will be ready in 3 minutes.')
else:
    print('Are you sure you want a plain pizza?')
    
# Dictionaries. these helps to build any form of model that you cal=n use 
# to create anything you want.

aliens_0 = {'color': 'Yellow', 'Points' : '10'}
# This is a simple Dictionary that models an alien in a game.
# Dictionaries are wrapped in curly brackets.

# accessing values in a dictionary using print function.
print(aliens_0['color'])
print(aliens_0['Points'])

# adding new value pairs to a dictionary.
# this code adds more key-value pairs to the dictionary.
aliens_0['speed'] = '120'
aliens_0['x-position'] = '0'
aliens_0['y-position'] = '25'
print(aliens_0)

# you can also start with an empty dictionary and build it up
aliens_0 = {}
aliens_0['color'] = 'Yellow'
aliens_0['Points'] = '0'
aliens_0['speed'] = '120'
aliens_0['x-position'] = '0'
aliens_0['y-position'] = '25'
print(aliens_0)

# modifying and assigning new values to items in a dictionary
aliens_0 = {'x-position' : '0' , 'y-position' : '25', 'speed' : 'fast'}
print(aliens_0)

# try to modify the key-value (speed) a little bit using if-elif-else
if aliens_0['speed'] == 'slow':
    speed_increment = '1'
elif aliens_0['speed'] == 'medium':
    speed_increment = '2'
else:
    speed_increment = '3'

# assign the modified data to the (speed) to the x-position
aliens_0['x-position'] = aliens_0['x-position'] + speed_increment
print(f'new position: {aliens_0["x-position"]}')

# deleting an item from a dictionary
aliens_0 = {'color': 'Yellow', 'Points' : '10'}
del aliens_0['color']
print(aliens_0)


# A dictionary of similar objects
# a dictionary involving multiple lines could be written like this.
favorite_movies = {
    'John Wick' : '2017',
    'Killer Bean' : '2014'
}
print(favorite_movies['John Wick'])

# using get() method to access values in a dictionary 
aliens_0 = {'color': 'Yellow', 'Points' : '10'}
speed = aliens_0.get('speed', 'Maximum speed reached.') # there is no key value
# python will return None.
print(speed)

# looping through a dictionary
# looping through all keys-value pairs in a dictionary

favorite_movies = {
    'John Wick' : '2017',
    'Killer Bean' : '2014',
    'The Avengers' : '2012',
    'Most wanted' : '2011'
}
for movie, year_released in favorite_movies.items():
    print(f'\n{movie} was released in {year_released}')

# another try of the looping through all key-value pairs in a dictionary
Manu = {
    'Mondays' : 'Rice and vegetable stew',
    'Tuesdays' : 'Chicken and vegetable stew',
    'Wednesdays' : 'Chicken and vegetable stew',
    'Thursdays' : 'Chicken and vegetable stew',
    'Fridays' : 'Chicken and vegetable stew',
    'Saturdays' : 'Chicken and vegetable stew',
    'Sundays' : 'Chicken and vegetable stew'
}
for Day, Dish in Manu.items():
    print(f'\n This is the manu for {Day}: {Dish}')

#looping through keys in a dictionary
favorite_movies = {
    'John wick' : '2017',
    'Killer Bean' : '2014',
    'The Avengers' : '2012',
    'Most wanted' : '2011'
}
Top_two_favorites = ['John wick' , 'Most wanted']
year = ['2014', '2012']
for title in favorite_movies.keys():
    print(f'\n{title}')
    if title in Top_two_favorites:
        x = favorite_movies[title]
        print(f'\n{title} was released in {x}')

for year_released in favorite_movies.values():
    print(f'\n{year_released}')
    if year_released in year:
        y = favorite_movies[title]
        print(f'\n {title} for the remaining \n{y}')

# another example 
favorite_languages = {
    'John' : 'python',
    'Christian' : 'PHP',
    'Joseph' : 'Java',
    'Seth' : 'C++'
}
friends = ['John', 'Seth']
for name in favorite_languages:
    print(f'\n Hi {name.title()}')
    if name in friends:
        language = favorite_languages[name]
        print(f'\n {name.title()} likes {language.title()}')

# nesting. this is a list containing dictionaries of identical nature 
aliens_0 = {'color' : 'green' , 'Points' : '5' , 'speed' : 'slow'}
aliens_1 = {'color' : 'yellow' , 'Points' : '10' , 'speed' : 'medium'}
aliens_2 = {'color' : 'red' , 'Points' : '15' , 'speed' : 'fast'}
aliens = [aliens_0, aliens_1, aliens_2]
print(aliens)

# another way to do this is to use range() method to print a number of aliens
# and modify how each of them behaves
aliens = []
for total_alien in range(20):
    new_alien = {'color' : 'green', 'points' : '5', 'speed' : 'slow'}
    aliens.append(new_alien)
#print(f'{len(aliens)}') #to check the length of of the alien list
# or 
#print({aliens}) # to print the elements in the alien list

# modify the first 3 aliens to look yellow
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = '15'
        alien['speed'] = 'fast'
print(aliens)

# using the sorted method to sort the output of the loop in specific manner
aliens_0 = {'color' : 'brown', 'point' : '20', 'speed' : 'medium',
                'position' : 'centre'}
for alien in sorted(aliens_0.values()):
    print(alien)

# a dictionary in another dictionary
users = {
    'Kaywa' : {
        'Firstname' : 'Kwesi',
        'Last Name' : 'Kaywa',
        'Location' : 'Accra',
        'Studio Name' : 'Kaywa Sounds',
    },

    'Hammer' : {
        'Firstname' : 'Alfred',
        'Last Name' : 'Hamilton',
        'Location' : 'Kumasi',
        'Studio Name' : 'The Last 2',
    }
}

for username, user_info in users.items():
    print(f'\nusername: {username}')
    fullname = f"{user_info['Firstname']} {user_info['Last Name']}"
    location = user_info['Location']
    studio_name = user_info['Studio Name']
    print(f'full name: {fullname}')
    print(f'location: {location}')
    print(f'studio name: {studio_name}')

# inputs() method
message = input('Input your FullName:' )
print(f'Welcome {message}')

# defining a variable and assigning the variable to the input message.
prompt = 'Enter your E-mail.'
prompt += f'\nWe only accept gmail accounts.'
email = input(prompt)
print(f'You are signed in as \n{email}')

# using the int() function to convert a user's input which was a string 
# to a number. 
prompt = 'How old are you?.'
prompt += f'\nWe do not accept minors on this platform.'
Age = input(prompt)
age = int(Age)
if age >= 18: # making a comparison with user input.
    print(f'\nyou qualify to join this page.')
else:
    print(f'\nyou are too young to join this page.')
#print(f'did you sa{age}?')

# modulus % operator. this returns the remainder after a division.
# it always returns the value 0 if the number is even.
User_number = input('Input your number:')
user_input = int(User_number)
if user_input % 2 == 0:
    print(f'\nyou entered an even number.')
else:
    print(f'\nyou entered an odd number.')

# using the while loop
# the while loop keeps a code running until the user decides to quit.
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

# another scenario 
prompt = 'How old are you?.'
prompt += f"\nminors are not allowed."
Age = input(prompt)
age = int(Age)
if age >= 18:
    print(f'\nyou qualify to join this page.')
elif age <= 18:
    print(f'\nyou are too young to join this page.')
    print('\nType Exit to end the session.')
message = ""
while message != 'Exit':
    message = input(prompt)
print('Your session has ended.')

# using flags. flags determine whether the program should continue to run 
# while certain conditions defined in the flag are true

prompt = 'How old are you?.'
prompt += f"\nminors are not allowed."
active = True 
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        break
    else: 
        print(message)

# using continue statement to loop back to the beginning of the code
# this code is to print out the odd numbers or numbers NOT divisible by 2
current_number = 0
while current_number <= 21:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)   
      
# using while loop with list and dictionaries
unverified_users = ['kwesi' , 'yaw', 'mandela']
verified_users = []
while unverified_users:
    user = unverified_users.pop()
    if user in verified_users:
        continue
    verified_users.append(user)
    print(f'\n{user} has been verified.')

# another example is 
unverified_users = ['kwesi' , 'yaw', 'mandela']
verified_users = []
while unverified_users:
    user = unverified_users.pop()
    print(f'verifying user: {user.title()}')
    verified_users.append(user)
print(f'\nthe following users have been verified:')
for user in verified_users:
    print(f'\n{user.title()}')

# removing all instances of a specific value in a list
pets = ['cat', 'dog', 'rabbit', 'cat', 'dog', 'cat']
#print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# chapter 8. Functions
"""A function allows you to define how program should operate in a particular 
way and it is fixed to that function only. def is used to define the function
and it followed rightly by name of the function and information about the 
function is held in the parenthesis."""
def greetings():
    """A simple greetings to the wold."""
    print('Hello!')
greetings()

# adding information about the function in its parenthesis.
def greetings(username):
    """A simple greetings to the wold."""
    print(f'Hello ! {username.title()}')
greetings('Gamba')  
greetings('Seth')


# parameters and arguments. 
def user_age(age): # age in this case is a parameter
    """A function to calculate the age of a user."""
    print(f'You are {age} years old.')
user_age(20) # 20 in this case is an argument. 

# having more than one parameter
def user_age(age, weight):
    """A function to calculate the age of a user."""
    print(f'You are {age} years old.')
    print(f'Your weight is {weight} kg.')
user_age(age=20, weight='120') #fixed keyword argument.

# using default values. a default value can be set to a parameter so that 
# that become the output when an argument is not made.
def pets(name, animal_type='cat'):   # cat is set as default in this case.
    """A function of pets and their names."""
    print(f"my pet's name is {name}")
    print(f" It is a {animal_type}")
pets('Tom')

# if you want a specific argument as a second argument instead of a cat,
# specify the argument. 
def pets(name, animal_type='cat'):   # cat is set as default in this case.
    """A function of pets and their names."""
    print(f"my pet's name is {name}")
    print(f" It is a {animal_type}")
pets('Singi', animal_type='bird') # the argument bird in this case overrides 
# the default value of cat.

# using return value 
def get_formatted_name(first_name, last_name):
    """A function to get the formatted name."""
    first_name = input('Enter your first name:')
    last_name = input('Enter your last name:')
    fullname = f'{first_name.title()} {last_name.title()}'
    return fullname.title()
Owner = get_formatted_name('firstname', 'lastname',)
print(f' Welcome: {Owner}')

# making an optional parameter like middle_name in the previous code.
def get_formatted_name(first_name, last_name, middle_name=''):
    """A function to get the formatted name."""
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name:')
    if middle_name:
        middle_name = input('Enter your middle name: ')
        fullname = f'{first_name.title()} {middle_name.title()} {last_name.title()}'
    else:
        fullname = f'{first_name.title()} {last_name.title()}'
    return fullname.title()
Owner = get_formatted_name('firstname', 'lastname', 'middle_name')
print(f' Welcome: {Owner}')


# returning a dictionary 
def greeting_users(names):
    """A function to greet users."""
    for name in names:
        msg = f'hello {name.title()}'
        print(msg)
usernames = ['king', 'bross', 'koo', 'weter']
greeting_users(usernames)


# passing arguments into a function using *args and **kwargs
# this will help to pass a limitless number of arguments into a function othe 
# than the positional type.

def List_subjects(*subjects):
    print(subjects, type(subjects))

List_subjects('English', 'Maths', 'Financial Accounting', 'Business Management')

# another example
def add(*args):   # this will return a tuple
    total = 0
    for num in args:
        total += num
    return total

print(add(1,2,3,4,5)) # more numbers can be added in the next call
print(add(2,3,4,5,6,8,9,12,45,56,))


def team(*members, **features): # this returns a tuple and a dictionary
    for member in members:
        print(member)
    
    
    for key,value in features.items():
        print("{}: {}".format(key,value))

print(
    team
      ("Abena", "Marilyn","kwame", Name = "FemCode", Project = "Answers", 
     Number = "Two Members", gender = "male", school =  "aggrey",
     )
)

def Number_of_fruits(*args, **kwargs,):
    print(args, type(args))
    print(kwargs, type(kwargs))
    

Number_of_fruits('baskets', 'bowls', mangoes = 20, ornages = 15, passion_fruits = 45)
print(Number_of_fruits)

def add(x, *any_number):
    for num in any_number:
        x += num
        print(x)

add(2,3,4,5,1)


import args_kwargs
args_kwargs.Number_of_fruits('names of fruits in ghana')


# Classes. object oriented programming 
class Dog:
    """This is to model a dog that is able to sit and roll over"""
    def ___init___(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(f'{self.nama} is sitting.')

    def roll_over(self):
        print(f'{self.name} has rolled over.')
"""instantiating or instance"""
my_dog = Dog('Bingo', 6) 
print(f"my dog's name is {my_dog.name}")
print(f"he is {my_dog.age} years old.")



