from dataclasses import dataclass, field

@dataclass(unsafe_hash=True)
class School:
    school_id: int = field(hash=True)
    name: str = field(compare=False)
    district: str = field(compare=True)
    school_level: str = field(compare=True)
    students: int = field(compare=True)

@dataclass(unsafe_hash=True)
class Passport:
    passport_number: str = field(hash=True)
    validity: str = field(compare=True)
    valid_from: str

@dataclass(unsafe_hash=True)
class Person:
    id_number: str = field(hash=True)
    name: str
    birth_date: str = field(compare=True)
    school_number: int