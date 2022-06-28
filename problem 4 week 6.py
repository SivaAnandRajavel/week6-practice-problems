# Problem 4
# Create a function that prints the name of each disney and pixar movie and also how many movies each category currently has.
# Note the output formatting
movie_collection = {
    'disney': ['Cinderella', 'Encanto', 'Little Mermaid', 'Tangled', 'Beauty & The Beast', 'Lion King',
               '101 Dalmations'],
    'pixar': ['Toy Story', 'Monsters, Inc.', 'Up', 'Finding Nemo', 'Coco', 'Wall-E', 'The Incredibles', 'Inside Out']
}

for key, value in movie_collection.items():
    j = 0
    print(key)
    for i in value:
        j = j + 1
        print(i)
    print(j)
