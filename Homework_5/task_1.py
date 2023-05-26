import os
import random
import pickle

# 1
list_of_tuples = []
for _ in range(1, 101):
    list_of_tuples.append((random.randint(1, 100), random.randint(1, 100), random.randint(1, 3)))

os.makedirs('./test/data')
with open('./test/data/data.txt', 'w+b') as file:
    data = pickle.dumps(list_of_tuples)
    file.write(data)
