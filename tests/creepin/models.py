from creepin import crud
from dataclasses import dataclass
from sqlalchemy import Boolean, Column, Integer, String, JSON


@dataclass
class A(crud.ModelBase, crud.DataModel):
    """Standard model with inherited autoincrement id field."""

    __tablename__ = "a"

    text:str = Column(String)


class AManager(crud.CRUDManager[A]):
    pass

a_objs = AManager(A)
A.objects = a_objs

###

@dataclass
class B(crud.ModelBase, crud.DataModel):
    """A model with a different concept of an ID from the base autoincrement ID."""

    __tablename__ = "b"

    id:str = Column(String, primary_key=True)
    text:str = Column(String)


class BManager(crud.CRUDManager[B]):
    pass

b_objs = BManager(B)
B.objects = b_objs
