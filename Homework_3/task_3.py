# 3
list_of_friends = ["John", "Marta", "James"]
list_of_enemies = ["John", "Johnatan", "Artur"]

for friend in list_of_friends:
    if friend in list_of_enemies:
        print(f"{friend} we are not friends anymore")
    elif friend == "James":
        continue
    else:
        print(f"{friend} we are the best friends")