import mysql.connector


def connect():
    try:
        conn = mysql.connector.connect(
            host="192.168.0.4",
            port="3306",
            database="mydb",
            user="user",
            password="userpassword",
        )

        if conn.is_connected():
            print(conn)
            return conn
        else:
            raise Exception("Connection Error")
    except Exception as e:
        print("[ERROR]", e)
        return None
