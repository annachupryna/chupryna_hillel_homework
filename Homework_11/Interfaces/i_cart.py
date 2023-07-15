from abc import ABC, abstractmethod


class ICart(ABC):

    @abstractmethod
    def _add_item(self, item): ...

    @abstractmethod
    def _remove_item(self, item): ...

    @abstractmethod
    def _calculate_total(self): ...

    @abstractmethod
    def _checkout(self): ...
