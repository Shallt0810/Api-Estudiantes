from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

# Database location: SQLite file will be created in the current directory
DATABASE_URL = "sqlite:///./database.db"

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SessionLocal class will be used to create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for our models (Student) to inherit from
# This allows SQLAlchemy to map our Python classes to database tables
Base = declarative_base()
