from abc import ABC, abstractmethod


class IPayment(ABC):

    @abstractmethod
    def process_payment(self, amount): ...
