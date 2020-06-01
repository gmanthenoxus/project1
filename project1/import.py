import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

def main():
    i = open("books.csv")
    reader = csv.reader(i)
    for isbn, year, title, author in reader:
        db.execute(INSERT INTO books (isbn, year, title, author) VALUES (:isbn, :year, :title, :author), {isbn: isbn, year:year, title:title, author:author})
    db.commit()