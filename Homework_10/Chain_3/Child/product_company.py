from Homework_10.Chain_3.Parent.company import *


class ProductCompany(Company, ABC):
    """This is an abstract class, heir from class Company which describes product company."""

    def __init__(self, ceo, cto, interest_rate, product_name):
        super().__init__(ceo, cto)
        self.interest_rate = interest_rate
        self.product_name = product_name

    @abstractmethod
    def promote_worker(self, worker): ...

    @abstractmethod
    def release_new_version(self): ...
