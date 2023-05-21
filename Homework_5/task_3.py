# 3
with open('text.txt', 'r') as file:
    data = file.read()

results = set()
for el in data.lower():
    if el.isalpha():
        results.update({f'Count of "{el}" is --> {data.count(el)}'})

for el in results:
    print(el)
