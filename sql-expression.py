from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)


# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
# Next, we need to link our Python file to our Chinook database, and that's where the 'create_engine'
# component comes into play.

meta = MetaData(db)
# The MetaData class will contain a collection of our table objects, and the associated data
# within those objects.

# create variable for "Artist" table
# Our first table class, or model, will be for the Artist table, which I'll assign to the variable of 'artist_table'.
# Using the Table import, we need to specify the name of our table, and provide the meta schema.
# Now, all that's left to do is provide a breakdown of each of the columns within this table.
# Table () taken from import
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)
# Back within our file, the format when defining columns, is the column name, followed by the
# type of data presented, and then any other optional fields after that.
# In our case, we have a column for "ArtistId", which is an Integer, and for this one, we
# can specify that primary_key is set to True.
# The next column is for "Name", and this is simply just a String, with no other values necessary.


# In order to perform all six original queries that we've been using so far, we also need
# to create variables for the Album and Track tables.

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

# Now, we need to actually connect to the database, using the .connect() method, and the Python with-statement.
# This saves our connection to the database into a variable called 'connection'.
# Before we start to query the database, we need to construct our tables, so that Python
# knows the schema that we're working with.


# For the sake of ease, let's define all six queries into a variable called 'select_query',
# which we can comment-out after each time it's used.
# Using the Expression Language, all we need to do is apply the .select() method onto our table.

 # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()


# It's going to be exactly the same, but this time we can use the .with_only_columns() method.
# Even if we want to grab results from a single column, we need to wrap the column selection inside of a list.
# Also, using dot-nation, we need to use ".c" in our selection, which will identify a specific
# column header on the table.
    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])


# Again, we're selecting from the artist_table, but this time we need to use the .where()
# method, and from the Name column, looking for only "Queen".
    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")



    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)

#     Now all that's left to do, is run this query using the .execute() method from our database connection.
# We're going to store the query results into a variable called "results", that way we can
# iterate over each result found, and print it to the Terminal.