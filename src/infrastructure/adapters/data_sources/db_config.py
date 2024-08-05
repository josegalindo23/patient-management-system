import os
# import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

host = os.getenv("HOST_NAME")
port = os.getenv("PORT")
database = os.getenv("DB_NAME")
user = os.getenv("USER_NAME")
schema = os.getenv("SCHEMA")
password = os.getenv("PASSWORD")

database_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(database_url, connect_args={'options': f'-csearch_path={schema}'})


Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()