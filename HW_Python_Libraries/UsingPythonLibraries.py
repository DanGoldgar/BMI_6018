import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# SQLAlchemy is an open source python library which provides users with a toolkit for SQL operations
# and an API feature called Object Relational Mapper to allow interactions between databases and python objects.
# Original creator: Michael Bayer / 2006
# Current release version: 2.0.36
# https://github.com/sqlalchemy/sqlalchemy

# Advantages to using SQLAlchemy include the ability to communicate with a database via SQL transactions
# from within a complex Python program. It also permits the creation of a python Class to represent individual
# tables, allowing users to bypass the usage of SQL statements entirely.
# Limitations: SQLAlchemy does not provide native support for Database Change Management (DCM) and migrations require
# a complicated workaround. Some users also seem to find the syntax to be a bit clunky.

# The following code demonstrates how SQLAlchemy is used to convert a dataset to a SQL table
# Dataset used: breast-cancer.data

bc_data = pd.read_csv("breast-cancer.data", header = None)
bc_data.columns = ['Class','Age','Menopause','Tumor-Size','Inv-Nodes','Node-Caps','Deg-Malig','Breast','Breast-Quad','Irradiat']

# Here sqlalchemy creates a database object in local memory
# echo set to False in order to prevent display of query metadata
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)

# Convert the pandas dataframe to sql table
bc_data.to_sql('breast_cancer_data', engine)

# Initialize connection to database object. Using the connection object we can execute SQL statements
with engine.connect() as conn:
    # Here we use SQL to select the rows from the table where the Menopause value is 'ge40'
    result = conn.execute(text("SELECT * FROM breast_cancer_data WHERE Menopause = 'ge40' "))
    # Print the result
    for row in result:
        print(row)

# The following code demonstrates how SQLAlchemy can be used to manipulate a database in Python
# without using SQL statements. Here a simple example table is created to demonstrate basic operations
# (this method is inefficient for producing a new table from a large dataset, but excellent for manipulation of
# existing data)

Base = sqlalchemy.orm.declarative_base()
# Create class Movie, which defines the table object and corresponding python objects (row entries)
class Movie(Base):
    __tablename__ = "movies"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    year = Column(Integer)
    director = Column(String(50))

    def __init__(self, title=None, year=None):
        self.title = title
        self.year = year

    def __repr__(self):
        return f"Movie({self.title}, {self.year}, {self.director})"

# Create
Base.metadata.create_all(engine)

# Initialize session for database queries
Session = sessionmaker(bind=engine)
session1 = Session()

# Test row to insert
m1 = Movie("Alien: Romulus", 2024)
# Try data insertion, commit if no exceptions, rollback to prior state if exception thrown
try:
    session1.add(m1)
    session1.commit()
except:
    session1.rollback()

# Query db and print data
film_data = session1.query(Movie).all()
print("Contents of table:")
print(film_data)