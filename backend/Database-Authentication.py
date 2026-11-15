
import psycopg
from getpass import getpass



password = getpass("Authentication Required: ")

class Databaseconnection:

    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user

        try: 
            connection = psycopg.connect(
                host = host,
                port = port,
                dbname = database,
                user = user,
                password = password


            )
            print("Connected Successfully: Welcome back Young Master!")

        except Exception as error:
            print("Connection Failed", error)



database1 = Databaseconnection(
    "localhost",
    5432,
    "website_db",
    "postgres",
    password
   
)


