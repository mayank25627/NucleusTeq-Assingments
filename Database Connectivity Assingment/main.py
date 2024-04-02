import mysql.connector

# show databases


def show_databases(host, username, password):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=username,
            password=password
        )

        c = mydb.cursor()

        # Execute SHOW DATABASES query
        c.execute("SHOW DATABASES")

        for i in c:
            print(i[0])

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:

        if 'mydb' in locals():
            mydb.close()


# create table

def create_table():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mayank@123",
            database="students"
        )

        c = mydb.cursor()

        # Create statement for tblStudent
        studentTable = """CREATE TABLE IF NOT EXISTS `students`.`tblStudent` (
            `sid` INT NOT NULL AUTO_INCREMENT,
            `sname` VARCHAR(45) NULL,
            `sdept` VARCHAR(45) NULL,
            `age` INT NULL,
            PRIMARY KEY (`sid`)
        )"""

        # Execute table creation query
        c.execute(studentTable)

        # Fetch tblemployee details in the database
        c.execute("DESC tblStudent")

        # Print the table details
        for column in c:
            print(column)

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        # Finally, close the database connection
        if 'mydb' in locals():
            mydb.close()


# insert data

def insert_data():
    try:
        # Connecting to the MySQL server
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mayank@123",
            database="students"
        )

        # Cursor object
        c = db.cursor()

        # Insert statement for tblemployee
        # This statement will enable us to insert multiple rows at once.
        studentTable_insert = """INSERT INTO tblStudent (
            sname,
            sdept,
            age) 
            VALUES (%s, %s, %s)"""

        # Row data to be inserted
        data = [("Mayank", "IT", 20),
                ("Krish", "CSE", 21),
                ("Raju", "CSE", 22),
                ("Dadu", "BCA", 20)]

        # Execute the insert commands for all rows
        c.executemany(studentTable_insert, data)

        # Commit changes to the database
        db.commit()

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        # Finally, close the database connection
        if 'db' in locals():
            db.close()


# print table data

def select_all_from_table():
    try:
        # Connecting to the MySQL server
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mayank@123",
            database="students"
        )

        # Cursor object
        c = db.cursor()

        # Execute SELECT * FROM tblemployee query
        c.execute("SELECT * FROM tblStudent")

        # Fetch all records
        records = c.fetchall()

        # Print all records
        print("\nAll Records in tblStudent:")
        for record in records:
            print(record)

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        # Finally, close the database connection
        if 'db' in locals():
            db.close()


show_databases('localhost', 'root', 'Mayank@123')
create_table()
insert_data()
select_all_from_table()