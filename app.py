# Drake Costa <drake@saeris.io>
# CNE370 Spring 2024
#
# Test queries to run against a Maxscale MariaDB sharded database
import mysql.connector

def db():
    conn = mysql.connector.connect(
        user="maxuser",
        password="maxpwd",
        database="zipcodes_one",
        host="localhost",
        port=4000
    )
    return conn

def getLargest(cursor):
    cursor.execute("""
        SELECT * FROM zipcodes_one ORDER BY Zipcode DESC LIMIT 1;
    """)

    results = cursor.fetchall()

    print(results[0])

def allInKY(cursor):
    cursor.execute("""
        SELECT * FROM zipcodes_one WHERE State = "KY";
    """)

    results = cursor.fetchall()

    for result in results:
        print(result)

def allBetween(cursor):
    cursor.execute("""
        SELECT * FROM zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000 ORDER BY Zipcode;
    """)

    results = cursor.fetchall()

    for result in results:
        print(result)

def totalWages(cursor):
    cursor.execute("""
        SELECT SUM(TotalWages) as TotalWages FROM `zipcodes_one` WHERE State = "PA";
    """)

    results = cursor.fetchall()

    for result in results:
        print(result[0])

def main():
    conn = db()
    cursor = conn.cursor()
    print("Largest Zipcode:\n")
    getLargest(cursor)
    print("\nAll Zipcodes in Kentucky:\n")
    allInKY(cursor)
    print("\nAll Zipcodes between 40000 and 41000:\n")
    allBetween(cursor)
    print("\nToal Wages in Pennsylvania:\n")
    totalWages(cursor)
    

if __name__ == '__main__':
    main()
