from database import DataBase
from auth import *


db = DataBase(DATABASE_NAME,DATABASE_HOST_CONNECT,DATABASE_USER,DATABASE_PASSWORD,DATABASE_PORT)

connector = db.createConnector()
if connector != None:
    print(connector)

res = db.create_table_primary()
print(res)


