#4
anna = {'name': 'Anna', 'vegetarian': True, 'omnivore': True}
oleh = {'name': 'Oleh', 'vegetarian': True, 'omnivore': True}
olena = {'name': 'Olena', 'vegetarian': True, 'omnivore': False}
oksana = {'name': 'Oksana', 'vegetarian': True, 'omnivore': False}
people = [olena, oksana, anna, oleh]
guests_herbs_vegetables = set()
for person in people:
    for key, value in person.items():
        if person.get('vegetarian'):
            guests_herbs_vegetables.add(person.get('name'))

print(guests_herbs_vegetables)
