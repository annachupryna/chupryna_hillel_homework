from Homework_10.Chain_2.Parent.Educational_establishment import *


class AfterSchool(EducationalEstablishment, ABC):
    """This is an abstract class, heir from class Educational establishment which describes after school."""

    def __init__(self, headmaster, year_of_establishment, accreditation_level, type_of_institution):
        super().__init__(headmaster, year_of_establishment)
        self.accreditation_level = accreditation_level
        self.type_of_institution = type_of_institution

    @abstractmethod
    def enroll_students(self): ...

    @abstractmethod
    def dismiss_students(self): ...
