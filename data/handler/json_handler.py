import json
from typing import List
from model_dataclasses import School, Passport, Person
from generator import generate_schools, generate_passport, generate_person


def write_json(filename: str, schools: List['School'], passports: List['Passport'], persons: List['Person']):
    data = {
        "schools": [school.__dict__ for school in schools],
        "passports": [passport.__dict__ for passport in passports],
        "persons": [person.__dict__ for person in persons]
    }

    with open(filename, mode='w') as file:
        json.dump(data, file, indent=3)


def read_json(filename: str):
    with open(filename, mode='r') as file:
        data = json.load(file)

    schools = [School(**school) for school in data['schools']]
    passports = [Passport(**passport) for passport in data['passports']]
    persons = [Person(**person) for person in data['persons']]

    return schools, passports, persons

if __name__ == '__main__':
    n = 3
    schools = generate_schools(n)
    passports = generate_passport(n)
    person = generate_person(n,passports=passports,schools=schools)
    w_json = write_json('json.json', schools=schools,passports=passports,persons=person)

    r_json = read_json('json.json')

    for v in r_json:
        print(v)