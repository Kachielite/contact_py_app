from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL
SQLALCHEMY_DATABASE_URL = 'sqlite:///./contact.db'

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Session
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Database Object
Base = declarative_base()
