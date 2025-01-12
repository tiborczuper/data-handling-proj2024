from faker import Faker
from faker_vehicle import VehicleProvider
from model_classes import Car, Company
import random

def generate_cars(n: int, lang: str = "hu_HU", min_year: int = 1990, max_year: int = 2025) -> list[Car]:

    fake_vehicle = Faker(lang)
    fake_vehicle.add_provider(VehicleProvider)



    cars = []
    for i in range(n):
        automatic = random.choice([True,False])
        car = Car(

            plate=fake_vehicle.license_plate(),
            type=fake_vehicle.vehicle_make(),
            year=random.randint(min_year, max_year),
            automatic=automatic
        )


        cars.append(car)
    return cars

def generate_companies(n: int, lang: str = "hu_HU") -> list[Company]:
    fake_company = Faker(lang)
    companies = []

    for i in range(n):
        company = Company(
            name=fake_company.company(),
            industry=fake_company.job(),
        )
        companies.append(company)
    return companies

if __name__ == '__main__':
    cars = generate_cars(5)
    company = generate_companies(5)
    for v in cars:
        print(v)
    print()
    for v in company:
        print(v)


