import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error


class DBManager:
    def __init__(self, user, password, host, port) -> None:
        '''создание базы данных postgres_db если ее нет'''
        self.user = user
        self.__password = password
        self.host = host
        self.port = port
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user=user,
                                      # пароль, который указали при установке PostgreSQL
                                      password=password,
                                      host=host,
                                      port=port)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # получаем курсор, который позволяет выполнять SQL команды
        cursor = connection.cursor()
        sql_create_database = 'create database postgres;'
        try:
            cursor.execute(sql_create_database)
        except Error:
            pass
        finally:
            if connection:
                cursor.close()
                connection.close()

    def get_programs(self) -> list:
        '''метод выдает записи компаний с количеством их вакансий'''
        connection = psycopg2.connect(user=self.user,
                                      # пароль, который указали при установке PostgreSQL
                                      password=self.__password,
                                      host=self.host,
                                      port=self.port,
                                      database="postgres")
        cursor = connection.cursor()
        select_result = None
        try:
            select_query = '''SELECT * from programs;'''
            cursor.execute(select_query)
            select_result = cursor.fetchall()
        except Error:
            pass
        finally:
            if connection:
                cursor.close()
                connection.close()
        return select_result