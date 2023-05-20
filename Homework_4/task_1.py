# 1
str_1 = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
str_2 = str_1.strip().replace("=", "&").replace("&&", "&")
values = str_2.split("&")
values.remove('sssss')

dict_of_values = {}
for element in range(0, len(values), 2):
    key = values[element]
    value = values[element + 1]
    dict_of_values[key] = value

print(dict_of_values)
