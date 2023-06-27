from abc import ABC, abstractmethod


class Company(ABC):
    """This is an abstract class which describes a company."""

    def __init__(self, ceo, cto):
        self.ceo = ceo
        self.cto = cto

    @abstractmethod
    def do_work(self): ...

    @abstractmethod
    def dismiss_worker(self, worker): ...
