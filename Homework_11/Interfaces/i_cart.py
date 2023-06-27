from abc import ABC, abstractmethod


class ICart(ABC):

    @abstractmethod
    def add_item(self, item): ...

    @abstractmethod
    def remove_item(self, item): ...

    @abstractmethod
    def calculate_total(self): ...

    @abstractmethod
    def checkout(self): ...
