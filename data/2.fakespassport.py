from faker import Faker
import random
from dateutil.relativedelta import relativedelta


fake = Faker("hu-HU")


print(fake.passport_number())
valid = (fake.date_between(start_date='today', end_date='+10y')) #lejarat
valid_minus_10_years = valid - relativedelta(years=10) #mikor csinaltak

print(valid)
print(valid_minus_10_years)