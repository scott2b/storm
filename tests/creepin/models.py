from creepin import crud
from dataclasses import dataclass
from sqlalchemy import Boolean, Column, Integer, String, JSON


@dataclass
class ExampleModel(crud.ModelBase, crud.DataModel):

    __tablename__ = "examplemodel"

    id:int = Column(Integer, primary_key=True)
    text:str = Column(String)

