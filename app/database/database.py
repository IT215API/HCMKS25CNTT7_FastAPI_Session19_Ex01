from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/logitics_db"

engine = create_engine(DATABASE_URL)

LocalSession = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass