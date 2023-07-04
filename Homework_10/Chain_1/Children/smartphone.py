from Homework_10.Chain_1.Parent.phone import *


class Smartphone(Phone):
    """This class is an heir from Phone and describes the characteristics of a smartphone."""

    def __init__(self, brand, year_of_issue, model, screen_diagonal, screen_resolution, lenses):
        super().__init__(brand, year_of_issue, model)
        self.screen_diagonal = screen_diagonal
        self.screen_resolution = screen_resolution
        self.lenses = lenses

    def charge(self):
        super().charge()
        print('Smartphone is charging')

    def call(self):
        super().call()
        print(f'Smartphone {self.brand} {self.model} is calling')

    def take_photo(self):
        print(f'Smartphone {self.brand} {self.model} is taking photo.')

    def connect_to_internet(self):
        print(f'Smartphone {self.brand} {self.model}  is connected to the Internet')
