import pytest
from creepin import db
from creepin import crud
from creepin.wiring import wire
from dataclasses import dataclass
from sqlalchemy import Boolean, Column, Integer, String, JSON
from sqlalchemy import text


wire()

with db.engine.connect() as con:
    con.execute(text("CREATE TABLE examplemodel (id INT NOT NULL, text VARCHAR(100))"))


@dataclass
class ExampleModel(crud.ModelBase, crud.DataModel):

    __tablename__ = "examplemodel"

    id:int = Column(Integer, primary_key=True)
    text:str = Column(String)


class TestExampleModel:

    def test_invalid_save(self):
        model = ExampleModel()
        with pytest.raises(ExampleModel.InvalidState):
            model.save()

    def test_valid_save(self):
        model = ExampleModel()
        model.id = 1
        model.save()

    def test_resave(self):
        model = ExampleModel()
        model.id = 2
        model.save()
        model.save()

    def test_dict(self):
        model = ExampleModel(text="testing")
        d = { "id": None, "text": "testing" }
        assert model.dict() == d
