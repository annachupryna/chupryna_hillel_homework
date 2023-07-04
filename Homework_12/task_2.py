"""
2. Describe the Train object. The class must contain fields and a method for adding wagons (it is necessary
to add objects, and instances of the wagon class). Describe the class Wagon together with the train.
The Wagon must contain a list of passengers and allow adding passengers. In the Wagon can be 10 passengers for example.
When using the len function on a Wagon, I want to see the number of passengers. When using len on a train,
I want to see a list of Wagons without a locomotive. Each wagon must have a number. When printing a wagon
to the console, I want to see the following "[n]" where n is the number of the wagon.
"""


class Wagon:
    def __init__(self, list_of_passengers: list, number_of_passengers: int, wagon_number: int):
        self.__list_of_passengers = list_of_passengers
        self.__number_of_passengers = number_of_passengers
        self.__wagon_number = wagon_number

    def add_passenger(self, passenger):
        if len(self.__list_of_passengers) < 10:
            self.__list_of_passengers.append(passenger)
            self.__number_of_passengers += 1
            return self.__list_of_passengers
        else:
            raise ValueError(f'Wagon contains maximum 10 people. '
                             f'Currently wagon {self.__wagon_number} has {self.__number_of_passengers} passengers.')

    def __str__(self):
        return f"[{self.__wagon_number}]"

    def __len__(self):
        output = len(self.__list_of_passengers)
        print(f'There are {output} passengers in wagon {self.__wagon_number}.')
        return output


class Train:

    def __init__(self, departure: str, destination: str):
        self.__departure = departure
        self.__destination = destination
        self.number_of_wagons = 0
        self._wagons = []
        self.locomotive = '<=HEAD'

    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, depart):
        if isinstance(depart, str):
            self.__departure = depart
        else:
            raise TypeError(f'Departure should be a string.')

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination_1):
        if isinstance(destination_1, str):
            self.__destination = destination_1
        else:
            raise TypeError(f'Destination should be a string.')

    @property
    def wagons(self):
        return self._wagons

    @wagons.setter
    def wagons(self, wagon):
        self._wagons = self._wagons.append(wagon)

    def add_wagon(self, wagon):
        self.number_of_wagons += 1
        self._wagons.append(wagon)
        return f'Wagon has been added to train.'

    def __len__(self):
        output = len(self._wagons)
        return output

    def __str__(self):
        wagon_list = "-".join(str(new_wagon) for new_wagon in self._wagons)
        return f"{self.locomotive}-{wagon_list}"


if __name__ == '__main__':
    wagon_1 = Wagon(['Pass1', 'Pass2', 'Pass3', 'q', 'q', 'Pass1', 'Pass2', 'Pass3', 'q'], 9, 1)
    wagon_2 = Wagon(['Pass1', 'Pass2', 'Pass3, Pass4'], 4, 2)
    wagon_3 = Wagon(['Pass1', 'Pass2', 'Pass3', 'q', 'q', 'Pass1', 'Pass2', 'Pass3', 'q'], 9, 3)
    train = Train('Kyiv', 'Lviv')
    train.add_wagon(wagon_1)
    train.add_wagon(wagon_2)
    train.add_wagon(wagon_3)
    print(train.__str__())
    print(train.number_of_wagons)
