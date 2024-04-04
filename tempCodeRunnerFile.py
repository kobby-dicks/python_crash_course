prompt = 'How old are you?.'
prompt += f"\nminors are not allowed. \nEnter 'quit' to end the program."
Age = input(prompt)
age = int(Age)
if age >= 18:
    print(f'\nyou qualify to join this page.')
message = ""
while message != 'quit':
    message = input(prompt)
print('Your session has ended.')