class Apple:
    """This class describes the Apple company characteristics."""

    def __init__(self):
        self.__name = 'Apple'
        self.__employees = 164000
        self.__establishment_year = 1976
        self.__headquarters = 'Cupertino, California, United States'
        self.__departments = {'Machine Learning and AI': 5000,
                              'Hardware': 6000,
                              'Software and Services': 4000,
                              'Design': 3000,
                              'Operations and Supply Chain': 5000,
                              'Marketing': 10000,
                              'Corporate Functions': 6000,
                              'Sales and Business Development': 10000}

    @property
    def name(self):
        return self.__name

    @property
    def employees(self):
        return self.__employees

    @property
    def establishment_year(self):
        return self.__establishment_year

    @property
    def headquarters(self):
        return self.__headquarters

    @property
    def departments(self):
        return self.__departments

    @staticmethod
    def is_official_store(country: str) -> str:
        """This method checks if the official store exists in a given country.
        List of countries can be extended if needed."""

        official_stores = ['United States', 'Japan', 'United Kingdom', 'Canada', 'Italy', 'Australia', 'Germany']
        if country in official_stores:
            return f'Official store in {country} exists.'
        else:
            return f'No official store in {country}.'

    @staticmethod
    def show_revenue(year: int) -> int | str:
        """This method returns revenue of Apple for the years between 2015-2022."""

        revenues = {2015: 5340000000,
                    2016: 5000000000,
                    2017: 4700000000,
                    2018: 5100000000,
                    2019: 4900000000,
                    2020: 5300000000,
                    2021: 5400000000,
                    2022: 6000000000}
        if revenues.get(year):
            return revenues.get(year)
        else:
            return f'Please type a year between 2015-2022'

    @staticmethod
    def show_bestseller(year: int) -> str:
        """This method returns the bestseller for the given year."""

        bestsellers = {2018: 'iPhone',
                       2019: 'iPad',
                       2020: 'MacBook',
                       2021: 'iPhone',
                       2022: 'iPhone'}
        if year in bestsellers.keys():
            return f'Bestseller in {year} is {bestsellers.get(year)}.'
        else:
            return f"Enter years in range 2018-2022"

    def check_department(self, department):
        """This method checks if department exists in the company"""

        if department in self.__departments.keys():
            return f'{department} exists in company.'
        else:
            return f'There is no such department as: {department}.'

    def show_department_employees(self, department: str) -> str:
        """This method returns department value according to the given department"""

        if department in self.__departments.keys():
            return f'Amount of employees in {department} is {self.__departments.get(department)}.'
        else:
            return f"There is no such department as: {department}"


if __name__ == '__main__':
    company = Apple()
    print(company.show_department_employees(",jkk"))
