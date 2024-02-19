from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    tryitle = Column(String)
    artist_id = Column(Integer, ForeignKey("Artist.artist_id"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unit_price = Column(Float)


#create session with DB
Session = sessionmaker(db)
#opens the actual session
session = Session()

#create the db using declarative_base subclass
base.metadata.create_all(db)
# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.artist_id, artist.name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.name)

# Query 3 - select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(name="Queen").first()
# print(artist.artist_id, artist.name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(artist_dd=51).first()
# print(artist.artist_id, artist.name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(composer="Queen")
for track in tracks:
    print(
        track.track_id,
        track.name,
        track.album_id,
        track.media_type_id,
        track.genre_id,
        track.composer,
        track.milliseconds,
        track.bytes,
        track.unit_price,
        sep=" | "
    )