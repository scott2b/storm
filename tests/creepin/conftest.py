#import pytest
#from creepin import crud
#from creepin import db
#from creepin import wiring
#
#
#DB_URI = "sqlite+pysqlite:///:memory:"
#
#
#@pytest.fixture
#def database():
#    return db.DB(DB_URI, verbose=True)


#@pytest.fixture
#def models(db):
#    from . import models as _models
#    wiring.wire(db, modules=["tests.creepin.models"])
#    return _models


#@pytest.fixture
#def container():
#    container = wiring.Container
#    #container.wire(modules=["yourapp.module1", "yourapp.module2"])
#    wiring.wire(modu
#    yield container
#    container.unwire()

#from dependency_injector import containers, providers
#
#@pytest.fixture
#def container(database):
#    #class Container(containers.DeclarativeContainer):
#    #    config = providers.Configuration()
#    #    db = providers.Factory(database.Session)
#    #    closed_db = providers.Resource(database.get_closed_db)
#
#    _container = wiring.Container
#    #_container = Container()
#    #_container.init_resources()
#    #container.wire(modules=[".models"])
#    #from . import models
#    #wiring.wire(database, modules=[crud, models])
#    wiring.wire(database, modules=["creepin"])
#    #Container.db = providers.Factory(db_obj.Session)
#    #Container.closed_db = providers.Resource(db_obj.get_closed_db)
#    yield _container
#    _container.unwire()
#
