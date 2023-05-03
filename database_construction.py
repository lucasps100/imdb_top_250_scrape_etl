import mysql.connector
from mysql.connector import Error
import pandas as pd
import os
import dotenv

dotenv.load_dotenv()

HOST = 'localhost'
USER = 'root'
PASSWD = os.environ["PASSWD"]


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("Connection made.")
    except Error as err:
        print(f"Error: {err}")
    return connection

connection = create_server_connection(HOST, USER, PASSWD)

db = "imdb_clone"

# def create_database(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Database created.")
#     except Error as err:
#         print(f"Error: {err}")
#
# create_db_query = f"CREATE DATABASE {db};"
#
# create_database(connection, create_db_query)

def use_database(connection, db):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db};")
        print(f"Now using database {db}.")
    except Error as err:
        print(f"Error: {err}")

use_database(connection, db)


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query successfully executed.")
    except Error as err:
        print(f"Error: {err}")


execute_query(connection, "DROP TABLE IF EXISTS casts;")
execute_query(connection, "DROP TABLE IF EXISTS artists;")
execute_query(connection, "DROP TABLE IF EXISTS movies;")
connection.commit()


create_movietable_query = "CREATE TABLE movies (" \
                          "id INT PRIMARY KEY AUTO_INCREMENT," \
                          "title VARCHAR(500) NOT NULL," \
                          "year_ INT NOT NULL," \
                          "description_ VARCHAR(1500)," \
                          "img VARCHAR(1000)" \
                          ")"
execute_query(connection, create_movietable_query)
execute_query(connection, "ALTER TABLE movies AUTO_INCREMENT=1;")

create_artisttable_query = "CREATE TABLE artists(" \
                           "id INT PRIMARY KEY AUTO_INCREMENT," \
                           "first_name VARCHAR(250) NOT NULL," \
                           "last_name VARCHAR(250) NOT NULL" \
                           ")"
execute_query(connection, create_artisttable_query)
execute_query(connection, "ALTER TABLE movies AUTO_INCREMENT=1;")

create_casttable_query = "CREATE TABLE casts (" \
                         "role_ VARCHAR(100) NOT NULL," \
                         "movie_id INT NOT NULL," \
                         "artist_id INT NOT NULL," \
                         "FOREIGN KEY(movie_id) REFERENCES movies(id)," \
                         "FOREIGN KEY(artist_id) REFERENCES artists(id)," \
                         "PRIMARY KEY(role_, movie_id, artist_id)" \
                         ");"
execute_query(connection, create_casttable_query)

movie_fields = ["Title", "Year", "Description", "Img"]
movies_data = pd.read_csv("movie_data.csv", delimiter=";", encoding="unicode escape",skiprows=1, names = movie_fields)

insert_movie_data_query = "INSERT INTO movies(title, year_, description_, img) VALUES "
for i in movies_data.iterrows():
    print(i[1])
    insert_movie_data_query += f"('{i[1]['Title']}', {i[1]['Year']}, '{i[1]['Description']}', '{i[1]['Img']}'),"
insert_movie_data_query = insert_movie_data_query.strip(",")


execute_query(connection, insert_movie_data_query)
connection.commit()

artist_fields = ["First Name", "Last Name"]
artists_data = pd.read_csv("artists_data.csv", delimiter=";", skiprows=1, names=artist_fields)

insert_artist_data_query = "INSERT INTO artists(first_name, last_name) VALUES "
for i in artists_data.iterrows():
    print(i[1])
    insert_artist_data_query += f"(\"{i[1]['First Name']}\", \"{i[1]['Last Name']}\"), "
insert_artist_data_query = insert_artist_data_query.strip(", ")
print(insert_artist_data_query)

execute_query(connection, insert_artist_data_query)
connection.commit()

cast_fields = ["role", "movie_id", "artist_id"]
casts_data = pd.read_csv("cast_data.csv", delimiter=";", encoding="unicode escape", skiprows=1, names = cast_fields)

insert_cast_data_query = "INSERT INTO casts(role_, movie_id, artist_id) VALUES "
for i in casts_data.iterrows():
    print(i[1])
    insert_cast_data_query += f"(\"{i[1]['role']}\", {i[1]['movie_id']}, {i[1]['artist_id']}), "
insert_cast_data_query = insert_cast_data_query.strip(", ")
print(insert_cast_data_query)

execute_query(connection, insert_cast_data_query)
connection.commit()
