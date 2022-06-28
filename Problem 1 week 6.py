x = [ [5,2,3], [10,8,9] ]
heros = [{'real_name':  'Bruce Wayne', 'hero_name' : 'Batman'}, {'real_name' : 'Tony Stark', 'hero_name' : 'Ironman'}]
franchise = {
    'dc' : ['Batman', 'Aquaman', 'Wonder Woman', 'Superman'],
    'marvel' : ['Hulk', 'Thor', 'Black Widow']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]=15
print(x)

heros[0]['hero_name']="Dark Knight"
print(heros)


for x in franchise['dc']:
  if x=='Aquaman':
      franchise['dc'] = ['Batman', 'Daredevil', 'Wonder Woman', 'Superman']
print(franchise['dc'])

# 4.) For z, how would you change the value 20 to 30?

z[0]['y'] = 30
print(z)