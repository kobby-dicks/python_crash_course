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