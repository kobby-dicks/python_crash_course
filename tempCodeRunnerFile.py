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