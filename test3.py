persons = [
    {'name':'Roger', 'age': 28, 'hobbies': ['futbol', 'musica', 'juegos']},
    {'name':'Rudy', 'age': 30, 'hobbies': ['metidar', 'trading', 'musica']},
    {'name':'Gledys', 'age': 55, 'hobbies': ['caminar', 'juegos', 'leer']}
]

# LIST COMPREHENSION FOR GETTING A NEW LIST WITH ONLY PERSONS NAMES
persons_names = [person['name'] for person in persons]

# CHECK IF ALL AGES ARE GREATER THAN 20
def check_age(age):
    return all([person["age"] > age for person in persons])

if check_age(20):
    print("All ages are greater than 20")
else:
    print("One ore more ages are lower than 20")

# COPYING CORRECTLY TO UPDATE NAME OF THE FIRST PERSON WITHOUT AFFECTING THE ORIGINAL PERSONS LIST
copied_persons = [person.copy() for person in persons]
copied_persons[0]["name"] = "Alexa"
print(persons)
print(copied_persons)

# UNPACKING THE ORIGINAL PERSONS LIST IN VARIABLES
person1, person2, person3 = persons
print("First person " + str(person1), "second person " + str(person2), "Third person " + str(person3))