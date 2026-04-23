from enum import StrEnum

from pydantic import BaseModel


class Gender(StrEnum):
    MALE = "male"
    FEMALE = "female"


class AgeGroup(StrEnum):
    CHILD = "child"
    TEENAGER = "teenager"
    ADULT = "adult"
    SENIOR = "senior"

class ProfileCreate(BaseModel):
    name: str
    gender: Gender
    gender_probability: float
    age: int
    age_group: AgeGroup
    country_id: str
    country_name: str
    country_probability: float

class ProfileUpdate(BaseModel):
    name: str | None = None
    gender: Gender | None = None
    gender_probability: float | None = None
    age: int | None = None
    age_group: AgeGroup | None = None
    country_id: str | None = None
    country_name: str | None = None
    country_probability: float | None = None