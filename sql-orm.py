from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# The reason that we no longer need to import the Table class, is because with the ORM,
# we're not going to create tables, but instead, we'll be creating Python classes.
# These Python classes that we'll create will subclass the declarative_base, meaning that
# any class we're making will extend from the main class within the ORM.
# It's the same exact thing for the sessionmaker; instead of making a connection to the database
# directly, we'll be asking for a session, which I'll discuss more in a moment.


# Exactly in the same way we did on the previous video, we're going to create a new variable
# of 'db', and use create_engine to point to our specific database location.

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()
# This new 'base' class will essentially grab the metadata that is produced by our database
# table schema, and creates a subclass to map everything back to us here within the 'base' variable.



# Now that we have the file set up, we can start to build our class-based models.
# These will be quite similar to how we did them in the last lesson, but this time, we
# get to simply build a normal Python object, that subclasses 'base'.
# Since we're going to perform the same six queries, we're going to work with the same
# three tables on Chinook, which were Artist, Album, and Track.
# Make sure these are added before the Session is created, but after the base is declared,
# since we need to use the base subclass.

# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
# We're going to call our first class 'Artist', and define the __tablename__, wrapped in two
# underscores, which will be set to "Artist" as a string.
# Just a quick note for best practice, when defining your classes in Python, it's best
# to use PascalCase, meaning the first letter of each word is capitalized, and not to use underscores.
# As you are well aware, the Artist table has two columns.
# ArtistId which uses the imported Column() class,
# and that's going to be set to an Integer, which will also act as our primary_key.
# Then we have Name, which is the second Column() defined simply as a String.

# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)







# This Session variable will instantiate the sessionmaker() class from the ORM, making
# a new instance of the sessionmaker, and point to our 'db' engine variable in order to use
# the database. There are some additional complexities that
# we won't get into here, but in order to connect to the database, we have to call Session()
# and open an actual session. To do that, we need another variable called
# 'session', but this time using a lowercase 's', and we set that to equal the new instance
# of the Session() from above.

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# Both of these concepts, using the declarative_base and sessionmaker, are using the highest layer
# of abstraction versus how we did this with the Expression Language.
# This is bringing us further away from writing raw SQL commands, and allowing us to use more
# Python logic, without having to focus too much on database tables directly.


# creating the database using declarative_base subclass
base.metadata.create_all(db)

# The last thing we need to do before we can work with our database, is to actually create
# the database subclass and generate all metadata. The base variable, given that it's a subclass
# from the declarative_base, will now use the .create_all() method from our database metadata.


# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" ||| ")
# At the bottom of our file, let's create a
# new variable called 'artists', and using our existing 'session' instance, we need to use
# the .query() method to query the Artist class. That should simply select everything on the
# table within the Artist class we defined above. We then need to iterate over the results found,
# and print each of the columns using dot-notation on our for-loop.
# I'm also going to separate each item using the Python separator, and have them split
# using the vertical-bar, or pipe, with a space on either side.



# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)



# Query 3 - select only "Queen" from the "Artist" table
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" | ")
# Next up, query #3, we only want to find "Queen" from the Artist table.
# Since we know that we only want to find a single artist, the new variable will be 'artist', singular.
# This time, we can use the .filter_by() method,
# and using the Name column, we'll specify "Queen". Also, since it should technically only return
# one record, we can use the .first() method to only give us the first item from the query,
# just in case more than one result comes back.


# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )