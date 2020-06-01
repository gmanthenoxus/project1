import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#Set up database
engine = create_engine(os.getenv("postgres://veyvwgmurymfsv:69b5667c92bfce605201072f1d795ba0b5d1ebd66b8acb655433e6e9746efac7@ec2-54-86-170-8.compute-1.amazonaws.com:5432/dfngc8qg8hpqb5"))
db = scoped_session(sessionmaker(bind=engine))

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

def main():
    i = open("books.csv")
    reader = csv.reader(i)
    for isbn, year, title, author in reader:
        db.execute("INSERT INTO books (isbn, year, title, author) VALUES (:isbn, :year, :title, :author)", {isbn: isbn, year:year, title:title, author:author})
        print(f"Added book Named {title} written by {author} in the year {year} with ISBN {isbn}")
    db.commit()

    if __name__ == "__main__":
        main()