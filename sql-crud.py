from sqlalchemy import (
    create_engine, Column, Integer, String
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



# This time, however, we don't need to worry about importing Float or ForeignKey.
# If you wanted to build new records on any of the existing tables, you certainly can,
# but for this lesson, we will focus on building a brand new table.
# Our new table will be to celebrate and acknowledge some of the greatest programmers of all time,
# so we'll call this class-based model "Programmer". We will, of course, extend the declarative_base
# once again, and for our __tablename__ it'll match the class itself, "Programmer".
# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
# For this table, we're going to keep it simple, and only include a few basic details.
# Our primary_key will be 'id', an Integer column, and since it's the primary key, it'll auto-increment
# with each new record added. This means that the first item added on this
# table will be assigned the ID of 1, and the second will be assigned the ID of 2, and so on.
# The remaining 5 columns will all be Strings,
# just to keep things simple. Those columns are: 'first_name', 'last_name',
# 'gender', 'nationality', and finally 'famous_for'.
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)





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



# For each new record we add, we'll assign it to a variable using the programmer's name
# as the actual variable. I think it's fair to say, the first person
# that we should add here would definitely be Ada Lovelace, the first computer programmer ever.
# We will define the variable as 'ada_lovelace',
# and this will use the Programmer() object above to define the various key/value pairs.
# Instead of using her actual name, we'll just stick to the first name of Ada, and last name
# of Lovelace, since that's how we all know her.
# For nationality, she was from London, so we'll use "British", and she's most famous for being the first programmer.

# creating records on our Progammer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

willy_wonka = Programmer(
    first_name="Willy",
    last_name="Wonka",
    gender="M",
    nationality="Ukrainisch",
    famous_for="3D WWW"
)


# Now, all that's left to do, is to add her to the table by using our current session,
# and then commit that session. session.add(ada_lovelace) and session.commit()
# The lovely thing about using the ORM and sessions, is that the formatting for adding records
# is quite similar to using Git when pushing files to GitHub.

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(willy_wonka)

# commit our session to the database
# session.commit()




# In order to update a specific record, we need to first identify which record that needs
# to be updated. Let's create a new variable of "programmer",
# and set that to our normal session.query() on the Programmer table.
# This time, however, we need to include the .filter_by() method.
# In some cases, your records might actually have very similar data, such as the same first
# or last name. As you can see, I share the same first name
# as Tim Berners-Lee, so filtering by first name is not practical.
# Ideally, we always want to try to use something unique with data retrieval, and that's precisely
# where our primary_key is most helpful on a relational database.
# If you've been following along exactly on the previous lesson, then your own record
# should have the primary_key of number 7. Since we only want one specific record, it's
# important to be sure to add the .first() method at the end of our query.
# If you don't add the .first() method, then you'll have to use a for-loop to iterate over
# the query list, even though it'll only find a single record using that ID.
# Once we've finished defining the query, we can simply use that 'programmer' variable
# and then define which columns need updating. In this case, let's go ahead and update our
# column of 'famous_for', and set that equal to "World President".

# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# commit our session to the database
# session.commit()


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")


# delete multiple/all records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# Before we start to add more Programmers to our table, let's make sure that Ada is added correctly.
# This is where the 'R' in CRUD comes back into
# action, as you've seen in our previous lessons, so this part should be familiar to you by now.
# We'll create a new variable to find all 'programmers',
# and then use the session to query our Programmer table.
# Then, even though we know there should only be one programmer, we will create a for-loop
# over this list of programmers, which will also prepare us for having more added later.
# We can print each key for the programmer, and use the Python separator of a vertical
# bar or pipe. This will be done using dot-notation, so programmer.id,
# programmer.first_name, and I’ll combine the first and last name using a space to separate
# them, then programmer.gender, programmer.nationality, and finally, programmer.famous_for.
# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
