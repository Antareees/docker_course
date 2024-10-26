from fastapi import FastAPI
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
from db_manager.db_manager import DBManager



app = FastAPI()
db_manager = DBManager("postgres", "postgres", "db", '5432')

@app.get("/programs")
def get_programs():
    programs = db_manager.get_programs()
    programs_name_and_rating = []
    for program in programs:
        programs_name_and_rating.append({'name': program[1], 'ratings': program[3]})
    return {"все программы": programs_name_and_rating}


@app.get("/")
def get_init():
    return {"все программы": "/programs"}