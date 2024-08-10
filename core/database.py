"""Module for setting up of connecting and closing of the DB"""

from decouple import config
import sqlalchemy as sql
from sqlalchemy.orm import declarative_base


DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT", default=5432)


DATABASE_URI = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = sql.create_engine(DATABASE_URI, echo=True)
Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    _id = sql.Column(sql.Integer, sql.Sequence("_id"), primary_key=True)
