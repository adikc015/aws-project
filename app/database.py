from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = "appuser"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "aws_project"

# First connect without DB
server_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD.replace('@','%40')}@{DB_HOST}:{DB_PORT}"

engine = create_engine(server_url)

with engine.connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))

# Now connect to database
DATABASE_URL = f"{server_url}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
