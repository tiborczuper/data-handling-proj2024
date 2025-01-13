import csv
from typing import List
from generator import generate_schools, generate_passport, generate_person
from model_dataclasses import School, Passport, Person

#writing
def write_school_csv(filename: str, schools: List['School']):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        #headers
        writer.writerow(['SCHOOL_ID', 'SCHOOL_NAME', 'DISTRICT', 'SCHOOL_LEVEL', 'NUM_OF_STUDENTS'])

        for school in schools:
            writer.writerow([school.school_id, school.name, school.district, school.school_level, school.students])

def write_passport_csv(filename: str, passports: List['Passport']):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        #headers
        writer.writerow(['PASSPORT_NUMBER','VALIDITY','VALID_FROM'])

        for passport in passports:
            writer.writerow([passport.passport_number, passport.validity, passport.valid_from])

def write_person_csv(filename: str, persons: List['Person']):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        #headers
        writer.writerow(['ID_NUMBER', 'NAME', 'BIRTH_DATE', 'SCHOOL_NUMBER'])

        for person in persons:
            writer.writerow([person.id_number, person.name, person.birth_date, person.school_number])


#reading
def read_school_csv(filename: str):
    schools = []

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for sor in reader:
            schools.append(School(school_id=int(sor[0]),
                                  name=sor[1],
                                  district=sor[2],
                                  school_level=sor[3],
                                  students=int(sor[4])))

    return schools

def read_passport_csv(filename: str):
    passports = []

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for sor in reader:
            passports.append(Passport(passport_number=sor[0],
                                      validity=sor[1],
                                      valid_from=sor[2]))
    return passports

def read_person_csv(filename: str):
    persons = []

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for sor in reader:
            persons.append(Person(id_number=sor[0],
                                  name=sor[1],
                                  birth_date=sor[2],
                                  school_number=int(sor[3])))

    return persons

if __name__ == '__main__':

    schools = generate_schools(3)
    w_schools = write_school_csv('schools.csv', schools)
    r_schools = read_school_csv('schools.csv')
    for v in r_schools:
        print(v)

    print()

    passports = generate_passport(3)
    w_passports = write_passport_csv('passports.csv', passports)
    r_passports = read_passport_csv('passports.csv')
    for v in r_passports:
        print(v)

    print()

    persons = generate_person(3,schools=schools, passports=passports)
    w_persons = write_person_csv('persons.csv', persons)
    r_persons = read_person_csv('persons.csv')
    for v in r_persons:
        print(v)