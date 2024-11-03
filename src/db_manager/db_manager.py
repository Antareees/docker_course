from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.schemas.models import *


class DBManager:
    def __init__(self, user, password, host, port) -> None:
        '''создание базы данных postgres_db если ее нет'''
        self.user = user
        self.__password = password
        self.host = host
        self.port = port
        self.engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/postgres")
        self.session = Session(bind=self.engine)


    def get_programs(self) -> list:
        '''метод выдает записи компаний с количеством их вакансий'''

        session = self.session
        select_result = None
        select_result = session.query(Programs).all()
        return select_result
