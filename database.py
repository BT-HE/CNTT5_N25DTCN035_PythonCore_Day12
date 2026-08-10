from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "mysql+pymyslq://root:123456@localhost:3306/library_management"
engine = create_engine(DATABASE_URL, echo = True)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()



