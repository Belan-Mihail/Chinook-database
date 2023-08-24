from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")
base = declarative_base()

class FavoriteCountries(base):
    __tablename__ = "Favorite Country"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)
    population = Column(Integer)
    famous_for = Column(String)



Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)


ukraine = FavoriteCountries(
    name = "Ukraine",
    capital = "Kiev",
    population = 30000000,
    famous_for = "Brave and strong people"
)

germany = FavoriteCountries(
    name = "Germany",
    capital = "Berlin",
    population = 100000000,
    famous_for = "Oktober fest"
)

great_britain = FavoriteCountries(
    name = "Greate Britain",
    capital = "London",
    population = 90000000,
    famous_for = "Footbal"
)

uuuu = FavoriteCountries(
    name = "UUUU",
    capital = "KKK",
    population = 1,
    famous_for = "Apple"
)

# add each instance of our programmers to our session
# session.add(ukraine)
# session.add(germany)
# session.add(great_britain)
# session.add(uuuu)


# commit our session to the database
# session.commit()


# updating a single record
# country = session.query(FavoriteCountries).filter_by(id=4).first()
# country.famous_for = "KKK" + country.famous_for

# commit our session to the database
# session.commit()

# updating multiple records
# countries = session.query(FavoriteCountries)
# for country in countries:
#     country.capital = country.capital + "FFFF"
#     session.commit()

# deleting a single record
country = session.query(FavoriteCountries).filter_by(id=3).first()
session.delete(country)
session.commit()

countries = session.query(FavoriteCountries)
for country in countries:
    print(
        country.id,
        country.name + '!!!',
        country.capital,
        country.population,
        country.famous_for,
        sep=" |\/| "
    )