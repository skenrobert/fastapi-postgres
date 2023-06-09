
###################call conect database in main ####################
from db.database import Base, engine
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import user



################# create table in postgres
def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()