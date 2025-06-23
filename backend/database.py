from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .models import Base
import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
db_session = scoped_session(sessionmaker(bind=engine))

def init_db():
    Base.metadata.create_all(bind=engine)
