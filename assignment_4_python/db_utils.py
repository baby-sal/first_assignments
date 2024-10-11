#maybe import requests
# + Have db_utils file and use exception handling (db_utils)
# + Use appropriate SQL queries to interact with the database in your Flask application, and
# demonstrate at least two different queries (dbutils)


import mysql.connector
from requests import delete

from config import HOST, USER, PASSWORD, DATABASE

class DbConnectionError(Exception):
    pass

def establish_cnx():
    db_cnx = mysql.connector.connect(
        host= HOST,
        user= USER,
        password= PASSWORD,
        auth_plugin= "mysql_native_password",
        database=DATABASE
    )
    return db_cnx



def get_all_food():
    try:
        database_cnx = establish_cnx()
        cursor = database_cnx.cursor()
        print("Connected to the database...")

        query = """SELECT * FROM food"""
        cursor.execute(query)
        result = cursor.fetchall()

        for i in result:
            print(i) ##Prints the results
            # print(i[1]) ##Prints the names of the food

        cursor.close()

    except Exception:
        raise DbconnectionError("Unable to read data from database")

    finally:
        if database_cnx:
            database_cnx.close()
            print("Connection to the database has closed.")


if __name__ == '__main__':
    print("Testing DB Connection")
    print(get_all_food())


def delete_review_by_id(id):
    try:
        database_cnx = establish_cnx()
        cursor = database_cnx.cursor()
        print("Connected to the database...")

        deleter_query = """DELETE FROM reviews WHERE review_id = {}""".format(id)
        cursor.execute(deleter_query)

        database_cnx.commit()  # Commit the transaction to apply the deletion

        # you can leave little messages for yourself and debugging like this
        print(f"Review with id: {id} deleted.")

        view_remaining_query = "SELECT * FROM reviews"
        cursor.execute(view_remaining_query)
        new_records = cursor.fetchall()  # Get all remaining records

        return new_records

    except Exception:
        raise DbConnectionError("Unable to read data from database")

    finally:
        if database_cnx:
            database_cnx.close()
            print("Connection to the database has closed.")



## Add review
def add_review(record):
    record = None
    try:
        database_cnx = establish_cnx()
        cursor = database_cnx.cursor()
        print("Connected to the database...")

        inserter_query = """INSERT INTO reviews ({}) VALUES ("{}", "{}", "{}", "{}", {}, {}, {})""".format(
            ", ".join(record.keys()),
            record["food_id"],
            record["review_date"],
            record["review"],
        )
        cursor.execute(inserter_query)

        database_cnx.commit()  # VERY IMPORTANT, otherwise, rows would not be added or reflected in the DB!
        cursor.close()


    except Exception:
        raise DbConnectionError("Unable to read data from database")

    finally:
        if database_cnx:
            database_cnx.close()
            print("Connection to the database has closed.")

def main():
    add_review(record)

if __name__ == '__main__':
    print("Testing DB Connection")
    # print(get_all_food())
    print(get_all_regions())
    print(delete_review_by_id())
