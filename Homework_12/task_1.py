"""
Task 1
Describe any object of your choice in the class. I want the object to be printed to the console in the following format:
class_name: {
key: value
}
"""


class Worker:
    def __init__(self, name: str, age: int, company: str, department: str, position: str, salary: int):
        self.__name = name
        self.__age = age
        self.__company = company
        self.__department = department
        self.__position = position
        self.__salary = salary

    def __str__(self):
        output = f'{self.__class__.__name__}: \n{{\n\t"name": {self.__name}\n\t"age": {self.__age}' \
                 f'\n\t"company": {self.__company}\n\t"department": {self.__department}' \
                 f'\n\t"position": {self.__position}\n\t"salary": {self.__salary}\n}}'
        return output


if __name__ == '__main__':
    worker_1 = Worker('Alan', 45, 'Apple', 'Design', 'UX designer', 3000)
    print(worker_1)
