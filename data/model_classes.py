class School:
    name: str
    district: str
    school_level: str
    school_id:int

    def __init__(self, name: str, district: str, school_level: str, school_id: int) -> None:
        self.name = name
        self.district = district
        self.school_level = school_level
        self.school_id = school_id

    def __str__(self) -> str:
        return f"*school* ID:{self.school_id} [{self.name}] {self.school_level} ({self.district})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, School) and self.school_id == other.school_id

    def __hash__(self) -> int:
        return self.school_id.__hash__()

    def __lt__(self, other):
        if not isinstance(other, School):
            return NotImplemented
        return self.school_id < other.school_id

class Passport:
    passport_number: str
    validity: str
    valid_from: str

    def __init__(self, passport_number: str ,validity: str ,valid_from: str) -> None:
        self.passport_number = passport_number
        self.validity = validity
        self.valid_from = valid_from

    def __str__(self) -> str:
        return f"*passport* ID:{self.passport_number}: Validity: {self.valid_from} - {self.validity}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Passport) and self.passport_number == other.passport_number

    def __hash__(self) -> int:
        return hash(self.passport_number)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Passport):
            return NotImplemented
        return self.passport_number < other.passport_number

class Person:
    id_number: str
    name: str
    birth_date: str
    school_number: int

    def __init__(self,id_number: str ,name: str ,birth_date: str ,school_number: int ) -> None:
        self.id_number = id_number
        self.name = name
        self.birth_date = birth_date
        self.school_number = school_number

    def __str__(self) -> str:
        return f"*person* ID:{self.id_number} : {self.name} [{self.birth_date}] School_ID: {self.school_number}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.name < other.name

if __name__ == '__main__':
    sc = School(
        name="SZUAI",
        school_level="alt isk",
        school_id=2343,#int
        district="Szobi ut"
    )
    passp = Passport(
        passport_number="123123123",
        validity="2020-12-12",
        valid_from="2010-12-12"
    )

    pers = Person(
        id_number=passp.passport_number,
        name ="Kiss Zoltán",
        birth_date="2002-03-15",
        school_number=sc.school_id
    )

    print(sc)
    print(passp)
    print(pers)