favorite_movies = {
    'John wick' : '2017',
    'Killer Bean' : '2014',
    'The Avengers' : '2012',
    'Most wanted' : '2011'
}
Top_two_favorites = ['John wick' , 'Most wanted']
year = ['2017', '2011']
for title in favorite_movies.keys():
    print(f'\n{title}')
if title in Top_two_favorites:
    x = favorite_movies[title]
    print(f'\n{title} was released in {x}') 
for year_released in favorite_movies.values():
    print(f'\n{year_released}')
if year_released in year:
    y = year 
    print(f'\n my favorite movies were released in \n{y}')