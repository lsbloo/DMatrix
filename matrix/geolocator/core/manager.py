from database import DataBase

from auth import DATABASE_NAME,DATABASE_HOST_CONNECT,DATABASE_USER,DATABASE_PASSWORD,DATABASE_PORT

db = DataBase(DATABASE_NAME,DATABASE_HOST_CONNECT,DATABASE_USER,DATABASE_PASSWORD,DATABASE_PORT)


def createConnetor():
    res = db.createConnector()
    db.create_tables()
    return res

def insertAddress(adress):
    db.insert_adress(adress)

def getAllAddress():
    return db.get_all_adress()

def getAddress(address):
    return db.get_address(address)

def insertLocate(locate):
    db.insert_locate(locate)

def getAllLocate():
    return db.get_all_locate()

def getLocate(locate):
    return db.get_locate(locate)


