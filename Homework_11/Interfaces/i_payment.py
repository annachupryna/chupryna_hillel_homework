from abc import ABC, abstractmethod


class IPayment(ABC):

    @abstractmethod
    def _process_payment(self, amount): ...
