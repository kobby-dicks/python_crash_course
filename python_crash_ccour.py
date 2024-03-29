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

# tuples. these are immutable list. thus the content of a tuple cannot be changed
fixed_manu = ('rice', 'joloff', 'banku')
fixed_manu[0] = 'yam' # if we try to change rice to yam, it is not possible in this case
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
    