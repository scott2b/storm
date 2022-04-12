import os
import pytest
import sqlalchemy
from creepin import wiring
from creepin.db import AlchemyDB
from sqlalchemy import text
from dependency_injector import containers, providers


import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

DB_URI = "sqlite+pysqlite:///:memory:"


# Important!!! Database must be registered and wired before importing any
# modules which require injection wiring
_db = AlchemyDB(DB_URI, verbose=True)
_db.register()
_db.container.wire(modules=["creepin.crud", ".models"])

from . import models


@pytest.fixture()
def db_a():
    """For tests of model "A" with a standard inherited autoincrement ID."""
    models.A.__table__.create(_db.engine)
    yield _db
    models.A.__table__.drop(_db.engine)


class TestModelA:

    def test_auto_id(self, db_a):
        model = models.A()
        model.save()
        assert model.id == 1

    def test_valid_save(self, db_a):
        model = models.A(id=1)
        model.save()

    def test_save_duplicate(self, db_a):
        model = models.A(id=1)
        model.save()
        model = models.A(id=1)
        with pytest.raises(sqlalchemy.exc.IntegrityError):
            model.save()

    def test_update_save(self, db_a):
        model = models.A(id=1)
        model.save()
        model.text = "test"
        model.save()
        model_test2 = models.A.objects.get(1)
        assert model_test2.text == "test"

    def test_dict(self):
        model = models.A(text="testing")
        d = { "id": None, "text": "testing" }
        assert model.dict() == d
        model = models.A(id=1, text="testing")
        d = { "id": 1, "text": "testing" }
        assert model.dict() == d


@pytest.fixture()
def db_b():
    """For tests of model "B" with ID override of a string-based ID."""
    models.B.__table__.create(_db.engine)
    yield _db
    models.B.__table__.drop(_db.engine)


class TestModelB:

    def test_alt_id(self, db_b):
        model = models.B(id="test")
        model.save()

    def test_alt_id_duplicate(self, db_b):
        model = models.B(id="test")
        model.save()
        model = models.B(id="test")
        with pytest.raises(sqlalchemy.exc.IntegrityError):
            model.save()

    def test_alt_id_missing_id(self, db_b):
        model = models.B()
        with pytest.warns(sqlalchemy.exc.SAWarning):
            with pytest.raises(sqlalchemy.exc.IntegrityError):
                model.save()
