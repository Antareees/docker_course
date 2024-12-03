from fastapi import FastAPI, HTTPException, status
from db_manager.db_manager import DBManager
import asyncio
import logging
import uvicorn
from pydantic import BaseModel

app = FastAPI()
db_manager = DBManager("postgres", "postgres")


@app.get("/list_programs")
def get_all_programs():
    programs = db_manager.get_all_programs()
    programs_name_and_rating = []
    for program in programs:
        print(program)
        programs_name_and_rating.append({'name': program.program_name, 'ratings': program.program_ratings})
    return {"все программы": programs_name_and_rating}


@app.get("/get_program/{id}")
def get_program(id: int):
    program = db_manager.get_program_by_id(id)
    if program is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {'name': program.program_name, 'ratings': program.program_ratings, 'duration': program.duration}


class Program(BaseModel):
    program_name: str
    program_duration: str
    program_ratings: int


@app.post("/add_program")
def add_program(new_program: Program):
    db_manager.add_program(new_program.program_name, new_program.program_duration, new_program.program_ratings)
    return new_program


@app.put("/update_program/{id}")
def update_program(new_program: Program, id: int):
    db_manager.update_program(id, new_program.program_name, new_program.program_duration, new_program.program_ratings)
    return new_program


@app.delete("/delete_program/{id}")
def delete_program(id: int):
    db_manager.delete_program(id)


@app.get("/list_hosts")
def get_all_hosts():
    hosts = db_manager.get_all_hosts()
    res_hosts = []
    for host in hosts:
        res_hosts.append({'host_name': host.host_name, 'experience': host.experience, "age": host.age})
    return {"все ведущие": res_hosts}


@app.get("/get_host/{id}")
def get_host(id: int):
    host = db_manager.get_host_by_id(id)
    if host is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {'host_name': host.host_name, 'experience': host.experience, "age": host.age}


class Host(BaseModel):
    host_name: str
    experience: int
    age: int


@app.post("/add_host")
def add_host(new_host: Host):
    db_manager.add_host(new_host.host_name, new_host.experience, new_host.age)
    return new_host


@app.put("/update_host/{id}")
def update_host(new_host: Host, id: int):
    db_manager.update_host(id, new_host.host_name, new_host.experience, new_host.age)
    return new_host


@app.delete("/delete_host/{id}")
def delete_host(id: int):
    db_manager.delete_host(id)


@app.get("/list_host_and_program")
def get_all_hosts_program_pairs():
    db_res = db_manager.get_all_hosts_program_pair()
    res = []
    for elem in db_res:
        res.append({"id": elem.id, "host_id": elem.host_id, "program_id": elem.program_id})
    return {"все пары ведущих и программ": res}


@app.get("/get_host_and_program/{id}")
def get_hosts_program_pair(id: int):
    elem = db_manager.get_hosts_program_pair_by_id(id)
    if elem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"id": elem.id, "host_id": elem.host_id, "program_id": elem.program_id}


class HostProgramPair(BaseModel):
    host_id: int
    program_id: int


@app.post("/add_host_and_program")
def add_host_and_program(new_elem: HostProgramPair):
    db_manager.add_hosts_program_pair(new_elem.program_id, new_elem.host_id)
    return new_elem


@app.put("/update_host_and_program/{id}")
def update_host_and_program(new_elem: HostProgramPair, id: int):
    db_manager.update_hosts_program_pair(id, new_elem.program_id, new_elem.host_id)
    return new_elem


@app.delete("/delete_host_and_program/{id}")
def delete_host_and_program(id: int):
    db_manager.delete_hosts_program_pair(id)


@app.get("/list_genres")
def get_all_genres():
    db_res = db_manager.get_all_genres()
    res = []
    for elem in db_res:
        res.append({"id": elem.id, "genre_name": elem.genre_name, "genre_desc": elem.genre_desc})
    return {"все пары ведущих и программ": res}


@app.get("/get_genre/{id}")
def get_genre(id: int):
    elem = db_manager.get_genre(id)
    if elem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"id": elem.id, "genre_name": elem.genre_name, "genre_desc": elem.genre_desc}


class Genre(BaseModel):
    genre_name: str
    genre_desc: str


@app.post("/add_genre")
def add_genre(new_elem: Genre):
    db_manager.add_genre(new_elem.genre_name, new_elem.genre_desc)
    return new_elem


@app.put("/update_genre/{id}")
def update_genre(new_elem: Genre, id: int):
    db_manager.update_genre(id, new_elem.genre_name, new_elem.genre_desc)
    return new_elem


@app.delete("/delete_genre/{id}")
def delete_genre(id: int):
    db_manager.delete_genre(id)


@app.get("/list_artists")
def get_all_artists():
    db_res = db_manager.get_all_artists()
    res = []
    for elem in db_res:
        res.append({"id": elem.id, "artist_name": elem.artist_name, "country_name": elem.country_name,
                    "birthdate": elem.birthdate, "genre_id": elem.genre_id})
    return {"все артисты": res}


@app.get("/get_artist/{id}")
def get_artist(id: int):
    elem = db_manager.get_artist(id)
    if elem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"id": elem.id, "artist_name": elem.artist_name, "country_name": elem.country_name,
            "birthdate": elem.birthdate, "genre_id": elem.genre_id}


class Artist(BaseModel):
    artist_name: str
    country_name: str
    birthdate: str
    genre_id: int


@app.post("/add_artist")
def add_artist(new_elem: Artist):
    db_manager.add_artist(new_elem.artist_name, new_elem.country_name, new_elem.birthdate, new_elem.genre_id)
    return new_elem


@app.put("/update_artist/{id}")
def update_artist(new_elem: Artist, id: int):
    db_manager.update_artist(id, new_elem.artist_name, new_elem.country_name, new_elem.birthdate, new_elem.genre_id)
    return new_elem


@app.delete("/delete_artist/{id}")
def delete_artist(id: int):
    db_manager.delete_artist(id)


@app.get("/list_tracks")
def get_all_tracks():
    db_res = db_manager.get_all_tracks()
    res = []
    for elem in db_res:
        res.append({"id": elem.id, "track_name": elem.track_name, "release_date": elem.release_date,
                    "duration": elem.duration, "artist_id": elem.artist_id, "genre_id": elem.genre_id})
    return {"все треки": res}


@app.get("/get_track/{id}")
def get_track(id: int):
    elem = db_manager.get_track(id)
    if elem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"id": elem.id, "track_name": elem.track_name, "release_date": elem.release_date,
            "duration": elem.duration, "artist_id": elem.artist_id, "genre_id": elem.genre_id}


class Track(BaseModel):
    track_name: str
    release_date: str
    duration: str
    artist_id: int
    genre_id: int


@app.post("/add_track")
def add_track(new_elem: Track):
    db_manager.add_track(new_elem.track_name, new_elem.release_date, new_elem.duration, new_elem.artist_id,
                         new_elem.genre_id)
    return new_elem


@app.put("/update_track/{id}")
def update_track(new_elem: Track, id: int):
    db_manager.update_track(id, new_elem.track_name, new_elem.release_date, new_elem.duration, new_elem.artist_id,
                            new_elem.genre_id)
    return new_elem


@app.delete("/delete_track/{id}")
def delete_track(id: int):
    db_manager.delete_track(id)


@app.get("/list_albums")
def get_all_albums():
    db_res = db_manager.get_all_albums()
    res = []
    for elem in db_res:
        res.append({"id": elem.id, "album_name": elem.album_name, "track_id": elem.track_id,
                    "year_of_release": elem.year_of_release, "artist_id": elem.artist_id})
    return {"все альбомы": res}


@app.get("/get_album/{id}")
def get_album(id: int):
    elem = db_manager.get_album(id)
    if elem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"id": elem.id, "album_name": elem.album_name, "track_id": elem.track_id,
            "year_of_release": elem.year_of_release, "artist_id": elem.artist_id}


class Album(BaseModel):
    album_name: str
    artist_id: int
    track_id: int
    year_of_release: int


@app.post("/add_album")
def add_album(new_elem: Album):
    db_manager.add_album(new_elem.album_name, new_elem.artist_id, new_elem.track_id, new_elem.year_of_release)
    return new_elem


@app.put("/update_album/{id}")
def update_album(new_elem: Album, id: int):
    db_manager.update_album(id, new_elem.album_name, new_elem.artist_id, new_elem.track_id, new_elem.year_of_release)
    return new_elem


@app.delete("/delete_album/{id}")
def delete_album(id: int):
    db_manager.delete_album(id)


@app.get("/list_song_requests")
def get_all_reqs():
    db_res = db_manager.get_all_song_requests()
    res = []
    for elem in db_res:
        res.append({"id": elem.id, "program_id": elem.program_id, "track_id": elem.track_id,
                    "request_time": elem.request_time, "request_date": elem.request_date})
    return {"все запросы на песню": res}


@app.get("/get_song_request/{id}")
def get_req(id: int):
    elem = db_manager.get_song_request(id)
    if elem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"id": elem.id, "program_id": elem.program_id, "track_id": elem.track_id,
            "request_time": elem.request_time, "request_date": elem.request_date}


class SongRequest(BaseModel):
    program_id: int
    track_id: int
    request_time: str
    request_date: str


@app.post("/add_song_request")
def add_req(new_elem: SongRequest):
    db_manager.add_song_request(new_elem.program_id, new_elem.track_id, new_elem.request_time, new_elem.request_date)
    return new_elem


@app.put("/update_song_request/{id}")
def update_req(new_elem: SongRequest, id: int):
    db_manager.update_song_request(id, new_elem.program_id, new_elem.track_id, new_elem.request_time,
                                   new_elem.request_date)
    return new_elem


@app.delete("/delete_song_request/{id}")
def delete_req(id: int):
    db_manager.delete_song_request(id)


@app.get("/list_playlists")
def get_all_playlists():
    db_res = db_manager.get_all_playlists()
    res = []
    for elem in db_res:
        res.append({"id": elem.id, "program_id": elem.program_id, "airtime": elem.airtime,
                    "playlist_date": elem.playlist_date})
    return {"все плейлисты": res}


@app.get("/get_playlist/{id}")
def get_playlist(id: int):
    elem = db_manager.get_playlist(id)
    if elem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"id": elem.id, "program_id": elem.program_id, "airtime": elem.airtime,
            "playlist_date": elem.playlist_date}


class Playlist(BaseModel):
    program_id: int
    airtime: str
    playlist_date: str


@app.post("/add_playlist")
def add_playlist(new_elem: Playlist):
    db_manager.add_playlist(new_elem.program_id, new_elem.airtime, new_elem.playlist_date)
    return new_elem


@app.put("/update_playlist/{id}")
def update_playlist(new_elem: Playlist, id: int):
    db_manager.update_playlist(id, new_elem.program_id, new_elem.airtime, new_elem.playlist_date)
    return new_elem


@app.delete("/delete_playlist/{id}")
def delete_playlist(id: int):
    db_manager.delete_playlist(id)


@app.get("/list_playlists_and_tracks")
def get_all_playlists_and_tracks():
    db_res = db_manager.get_all_playlists_and_tracks()
    res = []
    for elem in db_res:
        res.append({"id": elem.id, "playlist_id": elem.playlist_id, "track_id": elem.track_id})
    return {"все пары плейлистов и треков": res}


@app.get("/get_playlist_and_tracks/{id}")
def get_playlist_and_track(id: int):
    elem = db_manager.get_playlist_and_track(id)
    if elem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"id": elem.id, "playlist_id": elem.playlist_id, "track_id": elem.track_id}


class PlaylistTrack(BaseModel):
    playlist_id: int
    track_id: int


@app.post("/add_playlist_and_track")
def add_playlist_and_track(new_elem: PlaylistTrack):
    db_manager.add_playlist_and_track(new_elem.playlist_id, new_elem.track_id)
    return new_elem


@app.put("/update_playlist_and_track/{id}")
def update_playlist_and_track(new_elem: PlaylistTrack, id: int):
    db_manager.update_playlist_and_track(id, new_elem.playlist_id, new_elem.track_id)
    return new_elem


@app.delete("/delete_playlist_and_track/{id}")
def delete_playlist_and_track(id: int):
    db_manager.delete_playlist_and_track(id)


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
