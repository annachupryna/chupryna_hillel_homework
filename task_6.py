#6
names = ["Tyler Craig", "Nicola Suarez", "Tyler Craig", "Claire Chang", "Suzanne Mejia", "Claire Chang", "Tyler Craig"]
unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)