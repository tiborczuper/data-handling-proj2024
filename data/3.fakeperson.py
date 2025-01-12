from faker import Faker

fake = Faker("hu-HU")

print("passport id")
print(fake.name())
birthdate = fake.date_of_birth(minimum_age=18,maximum_age=25)
school number

print(birthdate)
