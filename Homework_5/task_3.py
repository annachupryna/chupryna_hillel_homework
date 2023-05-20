# 3
with open('text.txt', 'r') as file:
    data = file.read()

results = []
for el in data.lower():
    if el.isalpha():
        results.append(f'count of "{el}" is --> {data.count(el)}')

for el in set(results):
    print(el)
