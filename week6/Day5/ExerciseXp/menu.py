import psycopg2
from config import config

class MenuItem:
    def __init__(self):
       pass
    def save(self,name,price):
        """ insert a new menu into the menus table """
        sql = """INSERT INTO restaurant(name,price)
                VALUES(%s,%s) RETURNING menu_id;"""
        conn = None
        menu_id = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (name,price))
            # get the generated id back
            menu_id = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return menu_id
    
    def delete(self,part_id):
        """ delete part by part id """
        conn = None
        rows_deleted = 0
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the UPDATE  statement
            cur.execute("DELETE FROM restaurant WHERE menu_id = %s", (part_id,))
            # get the number of updated rows
            rows_deleted = cur.rowcount
            # Commit the changes to the database
            conn.commit()
            # Close communication with the PostgreSQL database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return rows_deleted
    def update(self,name,price):
        """ insert a new menu into the menus table """
        sql = """INSERT INTO restaurant(name,price)
                VALUES(%s,%s) RETURNING menu_id;"""
        conn = None
        menu_id = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (name,price))
            # get the generated id back
            menu_id = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return menu_id
    def get_by_name(self,name):
        pass