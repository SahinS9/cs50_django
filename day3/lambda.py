people = [
    {'name':'Harry','house':'Gryffindor'},
    {'name': 'Cho','house':'Ravenclaw'},
    {'name':'Draco', 'house':'Slytherin'}
]

#sort can not just sort the dictionary, so we will create function to help sorting

# f is for decoraters
def f(person):
    return person["name"]


people.sort(key = lambda person: person['name'])

people.sort(key = f)

print(people)




