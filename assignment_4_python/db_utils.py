import mysql.connector
from requests import delete
import datetime

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

        # for i in result:
        #     print(i) ##Prints the results
            # print(i[1]) ##Prints the names of the food

        cursor.close()
        return result

    except Exception:
        raise DbconnectionError("Unable to read data from database")

    finally:
        if database_cnx:
            database_cnx.close()
            print("Connection to the database has closed.")

def get_all_reviews():
    try:
        database_cnx = establish_cnx()
        cursor = database_cnx.cursor()
        print("Connected to the database...")

        query = """SELECT * FROM reviews"""
        cursor.execute(query)
        result = cursor.fetchall()

        for i in result:
            print(i) ##Prints the results
            # print(i[1]) ##Prints all the reviews

        cursor.close()

        return result

    except Exception:
        raise DbconnectionError("Unable to read data from database")

    finally:
        if database_cnx:
            database_cnx.close()
            print("Connection to the database has closed.")

def delete_review_by_id_db(id):
    try:
        database_cnx = establish_cnx()
        cursor = database_cnx.cursor()
        print("Connected to the database...")

        deleter_query = "DELETE FROM reviews WHERE review_id = {}".format(id)
        cursor.execute(deleter_query)

        database_cnx.commit()

        print(f"Review with id: {id} deleted.")

        view_remaining_query = "SELECT * FROM reviews"
        cursor.execute(view_remaining_query)
        new_records = cursor.fetchall()
        cursor.close()

        return new_records

    except Exception:
        raise DbConnectionError("Unable to read data from database")

    finally:
        if database_cnx:
            database_cnx.close()
            print("Connection to the database has closed.")

if __name__ == '__main__':
#     # print("Testing DB Connection")
#     # print(get_all_food())
#     # print(get_all_reviews())
        delete_review_by_id_db()
