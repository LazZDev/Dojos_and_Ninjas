import pymysql.cursors


class MySQLConnection:
    def __init__(self, db):
        # Initialize the MySQL connection with the provided database name
        # Change the host, user, password, and charset as needed
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        try:
            # Execute the query using a cursor within a context manager
            with self.connection.cursor() as cursor:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query, data)

                if query.lower().startswith("insert"):
                    # If the query is an INSERT statement, return the ID NUMBER of the inserted row
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().startswith("select"):
                    # If the query is a SELECT statement, return the result as a list of dictionaries
                    return cursor.fetchall()
                else:
                    # For UPDATE and DELETE statements, return nothing
                    self.connection.commit()
        except Exception as e:
            # If the query fails, raise an exception with the error message
            print("Something went wrong:", e)
            raise
        finally:
            # Close the database connection in the finally block to ensure it always happens
            self.connection.close()


def connectToMySQL(db):
    # Create an instance of MySQLConnection with the provided database name
    return MySQLConnection(db)
