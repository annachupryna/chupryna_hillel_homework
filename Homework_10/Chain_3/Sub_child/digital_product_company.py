from Homework_10.Chain_3.Child.product_company import *


class DigitalProductCompany(ProductCompany):
    """This is a class which heirs characteristics from classes Company and ProductCompany."""

    def __init__(self, ceo, cto, interest_rate, product_name, product_version, domain, workers):
        super().__init__(ceo, cto, interest_rate, product_name)
        self.product_version = product_version
        self.domain = domain
        self.workers = workers

    def do_work(self):
        print(f'We are developing {self.product_name}.')

    def dismiss_worker(self, worker):
        self.workers.remove(worker)
        print(f'Worker {worker} is dismissed from company {self.product_name}.')

    def promote_worker(self, worker):
        print(f'Worker {worker} from company {self.product_name} is promoted by {self.ceo}.')

    def release_new_version(self):
        self.product_version += 1
        print(f'Current product version is: {self.product_version}')

    def test_before_release(self):
        print(f'Product {self.product_name} is being tested by QA team.')

    def collect_user_reviews(self):
        print(f'User reviews have been collected by {self.workers}')
