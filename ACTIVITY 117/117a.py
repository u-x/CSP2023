animals_list = ['dog', 'cat', 'fish', 'bird', 'turtle']

print(animals_list)
print(type(animals_list))

animals_list.append('snake')
print(animals_list)
animals_list.pop()

for animal in animals_list:
    print(animal)

print(animals_list[2])

animals_list[2] = "mouse"
print(animals_list)