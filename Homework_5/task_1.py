import os
import random
import pickle

# 1
list_of_tuples = []
for number in range(1, 101):
    list_of_tuples.append((random.randint(1, 100), random.randint(1, 100), random.randint(1, 3)))

os.makedirs('./Homework_5.1')
os.chdir('./Homework_5.1')
with open('data.txt', 'w+b') as file:
    data = pickle.dumps(list_of_tuples)
    file.write(data)
