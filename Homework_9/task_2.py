class Worker:
    """This class describes default characteristics of any worker."""

    def __init__(self, name, age, position, salary, company, experience):
        self.__experience = experience
        self.__company = company
        self.__salary = salary
        self.__position = position
        self.__age = age
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) < 20:
            self.__name = new_name
        else:
            raise TypeError(f'Name should be a string less than 20 letters.')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age <= 0:
            raise ValueError(f'Age should be a positive number.')
        else:
            self.__age = new_age

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if isinstance(new_position, str) and len(new_position) < 40:
            self.__position = new_position
        else:
            raise TypeError(f'Name should be a string less than 20 letters.')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError(f'Salary should be a positive number more than 0.')
        else:
            self.__salary = new_salary

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, new_company):
        if isinstance(new_company, str) and len(new_company) < 40:
            self.__company = new_company
        else:
            raise TypeError(f'Name should be a string less than 20 letters.')

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, new_experience):
        if new_experience <= 0:
            raise ValueError(f'Experience should be a positive number.')
        else:
            self.__experience = new_experience

    def is_promotion_allowed(self, experience):
        """This method checks if worker can be promoted."""

        if experience > 2:
            return f'Promotion for worker {self.__name} is allowed.'
        else:
            return f'Not enough years to promote worker {self.__name}.'

    @staticmethod
    def calculate_yearly_income(salary):
        """This method calculates worker's yearly income."""

        return salary * 12

    def calculated_taxes(self):
        """This method calculates worker's monthly taxes."""

        taxes = self.__salary * 0.3
        return f'Taxes for worker {self.__name} are {taxes}'

    def do_work(self):
        return f'Worker {self.__name} is working'

    @classmethod
    def assign_director(cls):
        director_worker = Worker('Tom Henks', 34, 'director', 4000, 'BMW', 5, )
        return f'This worker is director: {director_worker.__name}'


if __name__ == '__main__':
    worker_1 = Worker("Anna", 25, "Designer", 1500, "Apple", 4)
    print(worker_1.do_work())
    worker_2 = Worker.assign_director()
    print(worker_2)
