CREATE TABLE "books"(
    "id" SERIAL PRIMARY KEY,
    "isbn" INTEGER NOT NULL,
    "year" INTEGER NOT NULL,
    "title" VARCHAR NOT NULL,
    "author" VARCHAR NOT NULL,
)

CREATE TABLE "user"(
     "id" SERIAL PRIMARY KEY,
    "username" VARCHAR NOT NULL,
    "password" VARCHAR NOT NULL,
)

CREATE TABLE "review"(
    "id" SERIAL PRIMARY KEY,
    "user_id" INTEGER NOT NULL,
    "books_id" INTEGER NOT NULL,
    "comment" VARCHAR NOT NULL,
    "rating" VARCHAR NOT NULL,
    FOREIGN KEY("") REFERENCES ""
    FOREIGN KEY("") REFERENCES ""
)