import pickle

# 2
with open('./test/data/data.txt', 'r+b') as file:
    byte_text = file.read()
tuples_list = pickle.loads(byte_text)

results = []
for element in tuples_list:
    if element[2] == 1:
        results.append(element[0] + element[1])
    elif element[2] == 2:
        results.append(element[0] - element[1])
    else:
        results.append(element[0] * element[1])
print(results)
