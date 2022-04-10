from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



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
