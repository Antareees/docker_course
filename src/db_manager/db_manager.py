from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from schemas.models import *


class DBManager:
    def __init__(self, user, password) -> None:
        '''создание базы данных postgres_db если ее нет'''
        self.user = user
        self.__password = password
        self.engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres:5432/postgres")
        self.session = Session(bind=self.engine)

    def get_programs(self) -> list:
        '''метод выдает записи компаний с количеством их вакансий'''

        session = self.session
        select_result = None
        select_result = session.query(Programs).all()
        return select_result
