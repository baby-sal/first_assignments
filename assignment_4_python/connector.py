import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE
#maybe import requests

def establish_cnx(database):
    db_cnx = mysql.connector.connect(
        host= HOST,
        user= USER,
        password= PASSWORD,
        auth_plugin= "mysql_native_password",
        database=DATABASE
    )
    return db_cnx



# cursor = db_cnx.cursor()
#
# query = ("SELECT * FROM food" )
#
# cursor.execute(query)
#
# result = cursor.fetchall()
#
# ##print all the names:
# for food in result:
#     print(food[1])
#
# print("Closing database connection...")
# db_cnx.close()



# EXAMPLE 1
def get_all_records():
    try:
        db_name = 'tests'  # update as required
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM abcreport"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# EXAMPLE 2

def calc_commission(sold_items, commission):
    sales = []

    for item in sold_items:
        sales.append(item[2])

    commission = sum(sales) * (commission / 100)
    return commission


# def get_all_records_for_rep(rep_name):
#     try:
#         db_name = 'tests'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print("Connected to DB: %s" % db_name)
#
#         query = """SELECT Item, Units, Total FROM abcreport WHERE Rep = '{}'""".format(
#             rep_name)  # note extra speech marks around the curly brackets -- we need them!
#         cur.execute(query)
#         result = cur.fetchall()  # this is a list with db records where each record is a tuple
#
#         for i in result:
#             print(i)
#
#         cur.close()
#
#         comp = round(calc_commission(result, commission=10), 2)
#
#     except Exception:
#         raise DbConnectionError("Failed to read data from DB")
#
#     finally:
#         if db_connection:
#             db_connection.close()
#             print("DB connection is closed")
#
#     print("Commission for {} is £{}".format(rep_name, comp))
#     return rep_name, comp
#
#
# def main():
#     get_all_records()
#     # get_all_records_for_rep('Morgan')
#
#
# if __name__ == '__main__':
#     main()