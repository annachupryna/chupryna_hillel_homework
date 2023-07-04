from abc import ABC, abstractmethod


class Phone(ABC):
    """This is an abstract class which describes a phone."""

    def __init__(self, brand, year_of_issue, model):
        self.brand = brand
        self.year_of_issue = year_of_issue
        self.model = model

    @abstractmethod
    def charge(self): ...

    @abstractmethod
    def call(self): ...
