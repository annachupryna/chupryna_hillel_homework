from Homework_10.Chain_1.Parent.phone import *


class ButtonPhone(Phone):
    """This class is an heir from Phone and describes the characteristics of a button phone."""
    def __init__(self, brand, year_of_issue, model, supported_connection, amount_of_dynamics):
        super().__init__(brand, year_of_issue, model)
        self.supported_connection = supported_connection
        self.amount_of_dynamics = amount_of_dynamics

    def charge(self):
        super().charge()
        print('Button phone is charging')

    def call(self):
        super().call()
        print(f'Button phone {self.brand} {self.model} is calling.')

    def play_radio(self):
        print(f'Button phone {self.brand} {self.model} is playing radio.')

    def turn_flashlight(self):
        print(f'Button phone {self.brand} {self.model} has the flashlight on.')
