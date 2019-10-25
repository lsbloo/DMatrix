import psycopg2

commands_create_tables = [
    (("CREATE TABLE IF NOT EXISTS address (id serial primary key, street varchar(255), number varchar(255), neighborhood varchar(255), city varchar(255), state varchar(255));")),
    (("CREATE TABLE IF NOT EXISTS locates (id serial primary key, latitude varchar(255) , longitude varchar(255), srid varchar(255));"))
]

class DataBase(object):

    def __init__(self,database_name,database_host_connect,database_user,database_password,database_port):
        self.database_name=database_name
        self.database_host_connect=database_host_connect
        self.database_user=database_user
        self.database_password=database_password
        self.database_port=database_port

    def createConnector(self):
        self.connector = psycopg2.connect(host=self.database_host_connect,dbname=self.database_name,
        user=self.database_user,password=self.database_password,port=self.database_port)
        self.connector.autocommit = True
        if self.connector != None:
            return self.connector
        return None

    def create_tables(self):
        cursor = self.connector.cursor()
        for i in range(len(commands_create_tables)):
            res = cursor.execute(commands_create_tables[i])
        cursor.close()
        return 'Table created'

    def insert_adress(self,adress):
        cursor = self.connector.cursor()
        data=(adress.street,adress.number,adress.neighborhood,adress.city,adress.state)
        sql=("INSERT INTO address (default,street,number,neighborhood,city,state) VALUES (?,?,?,?,?,?);")
        cursor.execute(sql,data)
        cursor.close()

    def get_all_adress(self,adress):
        cursor = self.connector.cursor()
        sql=("SELECT * FROM address")
        cursor.execute(sql)
        all = [r for r in cursor.fetchall()]

