from datetime import date

from pydantic import BaseModel, Field, field_validator, EmailStr, computed_field
from typing import Any, Generic, TypeVar, Optional


class Order(BaseModel):
    # id: int
    # user_id: int
    # items: list[int]
    # status: str
    ...


# !
# def func(i, arg1:list=None):   ###!!!важливо, скидувати стан дефолт аргумент
#     # --неможна ставити arg1:list=[] ,буде аппендити неверно
#     if arg1 is None:
#         arg1 = []
#     arg1.append(i)
#     print(arg1)
#
# func(1)
# func(2)

class Book(BaseModel):
    id: int
    title: Optional[str]
    author: str | None = Field(default=None, min_length=3, max_length=30)
    year: int
    birth_day: date
    # age: int = Field(default=0, ge=0, lt=100)
    email: EmailStr
    price: float
    items: list[int] = Field(default_factory=list)
    orders: dict[str, Order] | None  # or Any for values in dict orders

    @field_validator("author", mode="before")
    @classmethod
    def validator(cls, value):
        # return value.upper()
        if isinstance(value, str):
            return value
        elif isinstance(value, list):
            return " ".join(value)
        else:
            raise ValueError("Author must be a string or a list of strings")

    @computed_field(return_type=int | str)
    @property
    def age(self):
        return (date.today() - self.birth_day).days // 365

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False

        return (self.title == other.title and
                self.author == other.author and
                self.year == other.year and
                self.price == other.price and
                self.age == other.age and
                self.email == other.email and
                self.items == other.items and
                self.orders == other.orders and
                self.id == other.id and
                self.birth_day == other.birth_day
                )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.title, self.author, self.year, self.price))


# b=Book(id=1, title="Python", author=['Mike', 'Ava'], year=2020,price=17, age=11, email='email@aaa.com', items=[3,1,7,16], orders=None)
b = Book(id=1, title="Python", author=['Mike', 'Ava'], year=2020, birth_day='2000-12-25', price=17,
         email='email@aaa.com', items=[3, 1, 7, 16], orders=None)
print(b)
print(b.items)

book_dumped = b.model_dump()
print(book_dumped)

book_json = b.model_dump_json()
print(book_json)
# print(b.model_dump_json(by_alias=True, exclude={"id", "orders"}))


foreigner = Book.model_validate(book_dumped)
foreigner_json = foreigner.model_validate_json(book_json)
print(foreigner)
print(type(foreigner))
print(foreigner_json)
print(foreigner_json.items)
print(foreigner_json.email)
print(foreigner_json.age)
