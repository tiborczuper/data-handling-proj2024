from dataclasses import dataclass, field

@dataclass(unsafe_hash=True)
class School:
    school_id: int = field(hash=True)
    name: str = field(hash=True)
    district: str
    school_level: str
    students: int = field(compare=True)

@dataclass(unsafe_hash=True)
class Passport:
    passport_number: str = field(hash=True)
    validity: str
    valid_from: str

@dataclass(unsafe_hash=True)
class Person:
    id_number: str = field(hash=True)
    name: str
    birth_date: str
    school_number: int = field(compare=True)