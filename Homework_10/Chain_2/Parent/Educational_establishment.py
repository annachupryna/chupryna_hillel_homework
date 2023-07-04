from abc import ABC, abstractmethod


class EducationalEstablishment(ABC):
    """This is an abstract class which describes an educational establishment."""

    def __init__(self, headmaster, year_of_establishment):
        self.headmaster = headmaster
        self.year_of_establishment = year_of_establishment

    @abstractmethod
    def educate_students(self): ...

    @abstractmethod
    def graduate_students(self): ...
