from Homework_10.Chain_1.Parent.phone import *


class DialPhone(Phone):
    """This class is an heir from Phone and describes the characteristics of a dial phone."""

    def __init__(self, brand, year_of_issue, model, amount_of_holes, dial_diameter):
        super().__init__(brand, year_of_issue, model)
        self.amount_of_holes = amount_of_holes
        self.dial_diameter = dial_diameter

    def charge(self):
        super().charge()
        print('Dial phone is charging')

    def call(self):
        super().call()
        print('Dial phone is calling')

    def dial_number(self):
        print('Number has been dialed.')

    def pick_up_handle(self):
        print('Handle has been picked up and connection created.')
