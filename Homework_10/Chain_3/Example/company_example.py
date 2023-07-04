from Homework_10.Chain_3.Sub_child.digital_product_company import *

company = DigitalProductCompany('Vadim Nekhai', 'Dmytro Ivanov', 2, 'Canva', 3.0, 'Commercial businesses',
                                ['Mary', 'Anton', 'Serhii', 'Olena', 'Svitlana'])
print(company.workers)
company.dismiss_worker('Mary')
print(company.workers)
