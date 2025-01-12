from faker import Faker
from faker_education import SchoolProvider
import random

fake = Faker(SchoolProvider)

fake.add_provider(SchoolProvider)

print(random.randint(0,120)) #school id
print(fake.school_name())
print(fake.school_district())
print(fake.school_level())
