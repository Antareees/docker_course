from fastapi import FastAPI
from db_manager.db_manager import DBManager
import asyncio
import logging
import uvicorn


app = FastAPI()
db_manager = DBManager("postgres", "postgres")


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


async def run() -> None:
    config = uvicorn.Config("main:app", host="0.0.0.0", port=8000, reload=False)
    server = uvicorn.Server(config=config)
    tasks = (
        asyncio.create_task(server.serve()),
    )

    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
