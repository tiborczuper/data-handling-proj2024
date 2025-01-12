from faker import Faker
from faker_education import SchoolProvider
from model_classes import School, Passport, Person
import random
from dateutil.relativedelta import relativedelta


def generate_schools(n: int) -> list[School]:

    fake = Faker()
    fake.add_provider(SchoolProvider)

    schools = []
    for i in range(n):
        school = School(
            school_id= i+1,
            name = fake.school_name(),
            district = fake.school_district(),
            school_level= fake.school_level()
        )
        schools.append(school)
    return schools

def generate_passport(n: int,ervenyes: int = 5):
    fake = Faker()

    passports = []
    for i in range(n):
        validity = fake.date_between(start_date='today', end_date='+10y')
        valid_from= validity - relativedelta(years=ervenyes)
        pp = Passport(
            passport_number= fake.passport_number(),
            validity= str(validity),
            valid_from= str(valid_from)
        )
        passports.append(pp)
    return passports

def generate_person(n: int, passports: list[Passport],schools: list[School], lang = "hu_HU"):
    fake = Faker(lang)

    persons = []
    for i in range(n):

        school_numb = random.choice(schools).school_id
        bday = fake.date_of_birth(minimum_age=18,maximum_age=25)
        id = passports[i].passport_number

        person = Person(
            id_number = id,
            name = fake.name(),
            birth_date = str(bday),
            school_number = school_numb
        )
        persons.append(person)
    return persons

if __name__ == '__main__':
    n = 5
    sc = generate_schools(n)
    passp = generate_passport(n)
    pers = generate_person(n,passp,sc)


    for i in range(n):
        print(sc[i])
    print()
    for i in range(n):
        print(passp[i])
        print(pers[i])
        print()
