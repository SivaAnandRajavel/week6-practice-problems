	#Problem 3
#Create a function that given a list of dictionaries and a key name,
#it outputs the value stored in that key for each dictionary.
#For example, iterateDictionary2('real_name', superheros) should output

#Steve Rogers
#Barry Allan
#Bruce Banner
#Diana Prince

superheros = [
    {'real_name': 'Steve Rogers', 'hero_name': 'Captain America'},
    {'real_name': 'Barry Allan', 'hero_name': 'The Flash'},
    {'real_name': 'Bruce Banner', 'hero_name': 'The Incredible Hulk'},
    {'real_name': 'Diana Prince', 'hero_name': 'Wonder Woman'}
]
def first(d):
    for key in d:
        if key == 'real_name':
            print(d[key])

        #print(key +"-"+d[key])

superheros = [
    {'real_name': 'Steve Rogers', 'hero_name': 'Captain America'},
    {'real_name': 'Barry Allan', 'hero_name': 'The Flash'},
    {'real_name': 'Bruce Banner', 'hero_name': 'The Incredible Hulk'},
    {'real_name': 'Diana Prince', 'hero_name': 'Wonder Woman'}
]
for i in superheros:
    first(i)
