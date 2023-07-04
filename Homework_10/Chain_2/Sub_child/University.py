from Homework_10.Chain_2.Child.Afterschool_education import *


class University (AfterSchool):
    """This is a class which heirs characteristics from classes Educational establishment and after school."""

    def __init__(self,
                 headmaster: str,
                 year_of_establishment: int,
                 accreditation_level: int,
                 type_of_institution: str,
                 university_type: str,
                 major: str,
                 name: str):
        super().__init__(headmaster, year_of_establishment, accreditation_level, type_of_institution)
        self.university_type = university_type
        self.major = major
        self.name = name

    def educate_students(self):
        print(f'Students are educated in {self.type_of_institution}: {self.name}')

    def graduate_students(self):
        print(f'Students are graduated from {self.type_of_institution} ({self.name}) in major {self.major}')

    def enroll_students(self):
        print(f'Students are enrolled to university {self.name}')

    def dismiss_students(self):
        print(f'Students are dismissed from university {self.name}')

    def go_to_holidays(self):
        print(f'Our {self.university_type} {self.name} is on holidays from 01.06.2023 till 01.09.2023')

    def start_educational_year(self):
        print(f'We are happy to welcome you in the new year of study at our {self.university_type} {self.name}')
