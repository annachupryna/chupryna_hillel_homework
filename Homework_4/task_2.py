import re

# 2
variable_names = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_names = []

for name in variable_names:
    snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    snake_case_names.append(snake_case_name)

print(snake_case_names)
