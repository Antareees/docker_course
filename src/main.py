from fastapi import FastAPI
from src.db_manager.db_manager import DBManager



app = FastAPI()
db_manager = DBManager("postgres", "postgres", "db", '5432')

@app.get("/programs")
def get_programs():
    programs = db_manager.get_programs()
    programs_name_and_rating = []
    for program in programs:
        print(program)
        programs_name_and_rating.append({'name': program.program_name, 'ratings': program.program_ratings})
    return {"все программы": programs_name_and_rating}


@app.get("/")
def get_init():
    return {"все программы": "/programs"}