import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
#from dependency_injector import containers, providers


#from . import crud
#DEFAULT_MODULES = [crud]

class InvalidDatabaseConfiguration(Exception):
    """Configuration error in client."""



class DB():

    def __init__(self, db_uri, verbose=False):
        self.db_uri = db_uri
        self.verbose = verbose
        self.connection_count = 0
        self.engine = create_engine(
            db_uri,
            echo=verbose,
            future=True,  # SQLAlchemy 2.0 compatibility
            pool_pre_ping=True,
        )
        self.Session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine, expire_on_commit=False
        )
        event.listen(self.engine, "checkin", self.receive_checkin)
        event.listen(self.engine, "checkout", self.receive_checkout)

    #def wire(self, modules=None):
    #    if modules is None:
    #        modules = DEFAULT_MODULES
    #    Container.db = providers.Factory(self.Session)
    #    Container.closed_db = providers.Resource(self.get_closed_db)

    def receive_checkin(self, dbapi_connection, connection_record):
        self.connection_count -= 1

    def receive_checkout(self, dbapi_connection, connection_record, connection_proxy):
        self.connection_count += 1

    def get_closed_db(self) -> Generator:
        """Yield a db session that is closed when the function is exited. Note, to work
        properly with dependency injection, this must be provided as a Resource (not a
        Factory), and must be injected with the Closing operator. E.g:

        ```
        from dependency_injector.wiring import Closing, Provide
        def myfunc(db:Session=Closing[Provide[Container.closed_db]])...
        ```

        WARNING: The yielded session object cannot be error-handled in this scope.  Thus,
        rollback and connection close will not occur as a result of exceptions in target
        functions.

        This service **should only be used with thread-local scope** and with the Closing
        dependency injection directive. Requires expire_on_commit=False so that objects
        returned from the orm layer are still usable after the session is closed. There does
        not seem to be any performance penalty for committing sessions that do not really
        need to be committed. Thus, a no-commit option is not provided.
        """
        db = self.Session()
        yield db
        db.commit()
        db.close()

    #def container(self):
    #    class Container(containers.DeclarativeContainer):
    #        config = providers.Configuration()

    #        # Do not use this with the Closing directive
    #        db = providers.Factory(SessionLocal)

    #        # For use with Closing.
    #        # Use only with scoped_session thread-local scope.
    #        closed_db = providers.Resource(get_closed_db)
    #    return Container

    #@event.listens_for(engine, "checkin")
    #def receive_checkin(dbapi_connection, connection_record):
    #    self.connection_count -= 1


    #@event.listens_for(engine, "checkout")
    #def receive_checkout(dbapi_connection, connection_record, connection_proxy):
    #    global connection_count
    #    connection_count += 1



#SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///test.db"
#SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///:memory:"
#try:
#    SQLALCHEMY_DATABASE_URI = os.environ["CREEPIN_SQLALCHEMY_DATABASE_URI"]
#KeyError:
#    raise InvalidDatabaseConfiguration("CREEPIN_SQLALCHEMY_DATABASE_URI environment variable must be provided")
#LOG_SQL = os.environ.get("CREEPIN_LOG_SQL", True)
#
#engine = None
#SessionLocal = None
#
#def _create_engine(db_url, verbose=False):
#    global engine
#    engine = create_engine(
#        SQLALCHEMY_DATABASE_URI,
#        echo=LOG_SQL,
#        future=True,  # SQLAlchemy 2.0 compatibility
#        pool_pre_ping=True,
#    )

#SessionLocal = sessionmaker(
#    autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
#)

"""
SQLAlchemy connection count provided for testing and debugging purposes.
"""
#connection_count = 0

#@event.listens_for(engine, "checkin")
#def receive_checkin(dbapi_connection, connection_record):
#    global connection_count
#    connection_count -= 1


#@event.listens_for(engine, "checkout")
#def receive_checkout(dbapi_connection, connection_record, connection_proxy):
#    global connection_count
#    connection_count += 1


#def get_closed_db() -> Generator:
#    """Yield a db session that is closed when the function is exited. Note, to work
#    properly with dependency injection, this must be provided as a Resource (not a
#    Factory), and must be injected with the Closing operator. E.g:
#
#    ```
#    from dependency_injector.wiring import Closing, Provide
#    def myfunc(db:Session=Closing[Provide[Container.closed_db]])...
#    ```
#
#    WARNING: The yielded session object cannot be error-handled in this scope.  Thus,
#    rollback and connection close will not occur as a result of exceptions in target
#    functions.
#
#    This service **should only be used with thread-local scope** and with the Closing
#    dependency injection directive. Requires expire_on_commit=False so that objects
#    returned from the orm layer are still usable after the session is closed. There does
#    not seem to be any performance penalty for committing sessions that do not really
#    need to be committed. Thus, a no-commit option is not provided.
#    """
#    db = SessionLocal()
#    yield db
#    db.commit()
#    db.close()


#class Container(containers.DeclarativeContainer):
#    config = providers.Configuration()
#
#    # Do not use this with the Closing directive
#    db = providers.Factory(SessionLocal)
#
#    # For use with Closing.
#    # Use only with scoped_session thread-local scope.
#    closed_db = providers.Resource(get_closed_db)
