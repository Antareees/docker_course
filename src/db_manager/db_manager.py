from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import insert, update, delete
from schemas.models import *


class DBManager:
    def __init__(self, user, password) -> None:
        self.user = user
        self.__password = password
        self.engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres:8033/postgres")
        self.session = Session(bind=self.engine)

    def get_all_programs(self) -> list:
        session = self.session
        select_result = session.query(Programs).all()
        return select_result

    def get_program_by_id(self, id: int):
        session = self.session
        select_result = session.query(Programs).get(id)
        return select_result

    def add_program(self, name, duration, ratings):
        session = self.session
        session.execute(insert(Programs), [{"program_name": name, "duration": duration, "program_ratings": ratings}, ])
        session.commit()

    def update_program(self, id, name, duration, ratings):
        session = self.session
        session.execute(update(Programs),
                        [{"id": id, "programm_name": name, "duration": duration, "program_ratings": ratings}, ])
        session.commit()

    def delete_program(self, id):
        session = self.session
        delete_cmd = delete(Programs).where(Programs.id == id)
        session.execute(delete_cmd)
        session.commit()

    def get_all_hosts(self) -> list:
        session = self.session
        select_result = session.query(Hosts).all()
        return select_result

    def get_host_by_id(self, id: int):
        session = self.session
        select_result = session.query(Hosts).get(id)
        return select_result

    def add_host(self, host_name, experience, age):
        session = self.session
        session.execute(insert(Hosts), [{"host_name": host_name, "experience": experience, "age": age}, ])
        session.commit()

    def update_host(self, id, host_name, experience, age):
        session = self.session
        session.execute(update(Hosts), [{"id": id, "host_name": host_name, "experience": experience, "age": age}, ])
        session.commit()

    def delete_host(self, id):
        session = self.session
        delete_cmd = delete(Hosts).where(Hosts.id == id)
        session.execute(delete_cmd)
        session.commit()

    def get_all_hosts_program_pair(self) -> list:
        session = self.session
        select_result = session.query(HostProgramPair).all()
        return select_result

    def get_hosts_program_pair_by_id(self, id: int):
        session = self.session
        select_result = session.query(HostProgramPair).get(id)
        return select_result

    def add_hosts_program_pair(self, program_id, host_id):
        session = self.session
        session.execute(insert(HostProgramPair), [{"program_id": program_id, "host_id": host_id}, ])
        session.commit()

    def update_hosts_program_pair(self, id, program_id, host_id):
        session = self.session
        session.execute(update(HostProgramPair), [{"id": id, "program_id": program_id, "host_id": host_id}, ])
        session.commit()

    def delete_hosts_program_pair(self, id):
        session = self.session
        delete_cmd = delete(HostProgramPair).where(HostProgramPair.id == id)
        session.execute(delete_cmd)
        session.commit()

    def get_all_genres(self) -> list:
        session = self.session
        select_result = session.query(Genres).all()
        return select_result

    def get_genre(self, id: int):
        session = self.session
        select_result = session.query(Genres).get(id)
        return select_result

    def add_genre(self, genre_name, genre_desc):
        session = self.session
        session.execute(insert(Genres), [{"genre_name": genre_name, "genre_desc": genre_desc}, ])
        session.commit()

    def update_genre(self, id, genre_name, genre_desc):
        session = self.session
        session.execute(update(Genres), [{"id": id, "genre_name": genre_name, "genre_desc": genre_desc}, ])
        session.commit()

    def delete_genre(self, id):
        session = self.session
        delete_cmd = delete(Genres).where(Genres.id == id)
        session.execute(delete_cmd)
        session.commit()

    def get_all_artists(self) -> list:
        session = self.session
        select_result = session.query(Artists).all()
        return select_result

    def get_artist(self, id: int):
        session = self.session
        select_result = session.query(Artists).get(id)
        return select_result

    def add_artist(self, artist_name, country_name, birthdate, genre_id):
        session = self.session
        session.execute(insert(Artists), [{"artist_name": artist_name,
                                           "country_name": country_name,
                                           "birthdate": birthdate,
                                           "genre_id": genre_id}, ])
        session.commit()

    def update_artist(self, id, artist_name, country_name, birthdate, genre_id):
        session = self.session
        session.execute(update(Artists), [{"id": id, "artist_name": artist_name,
                                           "country_name": country_name,
                                           "birthdate": birthdate,
                                           "genre_id": genre_id}, ])
        session.commit()

    def delete_artist(self, id):
        session = self.session
        delete_cmd = delete(Artists).where(Artists.id == id)
        session.execute(delete_cmd)
        session.commit()

    def get_all_tracks(self) -> list:
        session = self.session
        select_result = session.query(Tracks).all()
        return select_result

    def get_track(self, id: int):
        session = self.session
        select_result = session.query(Tracks).get(id)
        return select_result

    def add_track(self, track_name, release_date, duration, artist_id, genre_id):
        session = self.session
        session.execute(insert(Tracks), [{"track_name": track_name,
                                          "release_date": release_date,
                                          "duration": duration,
                                          "artist_id": artist_id,
                                          "genre_id": genre_id}, ])
        session.commit()

    def update_track(self, id, track_name, release_date, duration, artist_id, genre_id):
        session = self.session
        session.execute(update(Tracks), [{"id": id,
                                          "track_name": track_name,
                                          "release_date": release_date,
                                          "duration": duration,
                                          "artist_id": artist_id,
                                          "genre_id": genre_id}, ])
        session.commit()

    def delete_track(self, id):
        session = self.session
        delete_cmd = delete(Tracks).where(Tracks.id == id)
        session.execute(delete_cmd)
        session.commit()

    def get_all_albums(self) -> list:
        session = self.session
        select_result = session.query(Album).all()
        return select_result

    def get_album(self, id: int):
        session = self.session
        select_result = session.query(Album).get(id)
        return select_result

    def add_album(self, album_name, artist_id, track_id, year_of_release):
        session = self.session
        session.execute(insert(Album), [{"album_name": album_name,
                                         "artist_id": artist_id,
                                         "track_id": track_id,
                                         "year_of_release": year_of_release}, ])
        session.commit()

    def update_album(self, id, album_name, artist_id, track_id, year_of_release):
        session = self.session
        session.execute(update(Album), [{"id": id,
                                         "album_name": album_name,
                                         "artist_id": artist_id,
                                         "track_id": track_id,
                                         "year_of_release": year_of_release}, ])
        session.commit()

    def delete_album(self, id):
        session = self.session
        delete_cmd = delete(Album).where(Album.id == id)
        session.execute(delete_cmd)
        session.commit()

    def get_all_song_requests(self) -> list:
        session = self.session
        select_result = session.query(SongRequests).all()
        return select_result

    def get_song_request(self, id: int):
        session = self.session
        select_result = session.query(SongRequests).get(id)
        return select_result

    def add_song_request(self, program_id, track_id, request_time, request_date):
        session = self.session
        session.execute(insert(SongRequests), [{"program_id": program_id,
                                                "track_id": track_id,
                                                "request_time": request_time,
                                                "request_date": request_date}, ])
        session.commit()

    def update_song_request(self, id, program_id, track_id, request_time, request_date):
        session = self.session
        session.execute(update(SongRequests), [{"id": id,
                                                "program_id": program_id,
                                                "track_id": track_id,
                                                "request_time": request_time,
                                                "request_date": request_date}, ])
        session.commit()

    def delete_song_request(self, id):
        session = self.session
        delete_cmd = delete(SongRequests).where(SongRequests.id == id)
        session.execute(delete_cmd)

    def get_all_playlists(self) -> list:
        session = self.session
        select_result = session.query(Playlists).all()
        return select_result

    def get_playlist(self, id: int):
        session = self.session
        select_result = session.query(Playlists).get(id)
        return select_result

    def add_playlist(self, program_id, airtime, playlist_date):
        session = self.session
        session.execute(insert(Playlists), [{"program_id": program_id,
                                             "airtime": airtime,
                                             "playlist_date": playlist_date}, ])
        session.commit()

    def update_playlist(self, id, program_id, airtime, playlist_date):
        session = self.session
        session.execute(update(Playlists), [{"id": id,
                                             "program_id": program_id,
                                             "airtime": airtime,
                                             "playlist_date": playlist_date}, ])
        session.commit()

    def delete_playlist(self, id):
        session = self.session
        delete_cmd = delete(Playlists).where(Playlists.id == id)
        session.execute(delete_cmd)
        session.commit()

    def get_all_playlists_and_tracks(self) -> list:
        session = self.session
        select_result = session.query(PlaylistAndTrackPair).all()
        return select_result

    def get_playlist_and_track(self, id: int):
        session = self.session
        select_result = session.query(PlaylistAndTrackPair).get(id)
        return select_result

    def add_playlist_and_track(self, playlist_id, track_id):
        session = self.session
        session.execute(insert(PlaylistAndTrackPair), [{"playlist_id": playlist_id,
                                                        "track_id": track_id}, ])
        session.commit()

    def update_playlist_and_track(self, id, playlist_id, track_id):
        session = self.session
        session.execute(update(PlaylistAndTrackPair), [{"id": id,
                                                        "playlist_id": playlist_id,
                                                        "track_id": track_id}, ])
        session.commit()


    def delete_playlist_and_track(self, id):
        session = self.session
        delete_cmd = delete(PlaylistAndTrackPair).where(PlaylistAndTrackPair.id == id)
        session.execute(delete_cmd)
        session.commit()
