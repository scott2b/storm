import os
import pytest
from creepin import db
from creepin import wiring
from sqlalchemy import text
from dependency_injector import containers, providers

DB_URI = "sqlite+pysqlite:///:memory:"

_db = db.DB(DB_URI, verbose=True)
with _db.engine.connect() as con:
    con.execute(text("CREATE TABLE examplemodel (id INT NOT NULL, text VARCHAR(100))"))



#class Container(containers.DeclarativeContainer):
#    config = providers.Configuration()
#    # Do not use this with the Closing directive
#    db = providers.Factory(_db.Session)
#
#    # For use with Closing.
#    # Use only with scoped_session thread-local scope.
#    closed_db = providers.Resource(_db.get_closed_db)

#Container = containers.DynamicContainer()
#Container.db = providers.Factory(_db.Session)
#Container.closed_db = providers.Resource(_db.get_closed_db)
wiring.wire(_db)
wiring.Container.wire(modules=["creepin.crud", ".models"])
from . import models

#wiring.Container = Container

#container = Container()
#container.wire(modules=["creepin.crud", ".models"])
#Container.wire(modules=["creepin.crud", ".models"])


class TestExampleModel:

    def test_invalid_save(self):
        model = models.ExampleModel()
        with pytest.raises(models.ExampleModel.InvalidState):
            model.save()

    def test_valid_save(self):
        model = models.ExampleModel()
        model.id = 1
        model.save()

    def test_resave(self):
        model = models.ExampleModel()
        model.id = 2
        model.save()
        model.save()

    def test_dict(self):
        model = models.ExampleModel(text="testing")
        d = { "id": None, "text": "testing" }
        assert model.dict() == d


if __name__=="__main__":
    t = TestExampleModel()
    t.test_valid_save()
