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
        return "{name} ({district}, {school_level} : {school_id})".format(
            name=self.name,
            district=self.district,
            school_level=self.school_level,
            school_id=self.school_id
        )

    def __eq__(self, other: object) -> bool:
        return isinstance(other, school_id) and self.plate == o.plate

    def __hash__(self) -> int:
        return self.plate.__hash__()

    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.plate < other.plate

class Passport:
    passport_number: str
    validity: str
    valid_from: str

    def __init__(self, name: str, industry: str) -> None:
        self.name = name
        self.industry = industry

    def __str__(self) -> str:
        return f"{self.name} ({self.industry})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Company) and self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Company):
            return NotImplemented
        return self.name < other.name

class Person:
    id_number: str
    name: str
    birth_date: str

    def __init__(self, name: str, industry: str) -> None:
        self.name = name
        self.industry = industry

    def __str__(self) -> str:
        return f"{self.name} ({self.industry})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Company) and self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Company):
            return NotImplemented
        return self.name < other.name
