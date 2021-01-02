import mysql.connector


def connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port="3306",
            database="mydb",
            user="user",
            password="userpassword"
        )

        if conn.is_connected():
            print(conn)
            return conn
        else:
            raise Exception("Connection Error")
            return None
    except Exception as e:
        print("[ERROR]", e)
