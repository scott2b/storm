from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from dependency_injector import containers, providers


SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///test.db"
LOG_SQL = True


engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=LOG_SQL,
    future=True, # SQLAlchemy 2.0 compatibility
    pool_pre_ping=True
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

"""
SQLAlchemy connection count provided for testing and debugging purposes.
"""
connection_count = 0


@event.listens_for(engine, 'checkin')
def receive_checkin(dbapi_connection, connection_record):
    global connection_count
    connection_count -= 1


@event.listens_for(engine, 'checkout')
def receive_checkout(dbapi_connection, connection_record, connection_proxy):
    global connection_count
    connection_count += 1


def get_closed_db() -> Generator:
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
    db = SessionLocal()
    yield db
    db.commit()
    db.close()


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Do not use this with the Closing directive
    db = providers.Factory( SessionLocal )

    # For use with Closing.
    # Use only with scoped_session thread-local scope.
    closed_db = providers.Resource( get_closed_db )
