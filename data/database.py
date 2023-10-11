"""
	TODO: postgres=# CREATE DATABASE question_quiz;
"""
from sqlalchemy import create_engine
from models.model import Base

from config.db_config import user, password, host, port, db_name
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
Base.metadata.create_all(engine)