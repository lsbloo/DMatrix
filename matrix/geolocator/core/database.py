import psycopg2

commands_create_tables = [
    (("CREATE TABLE IF NOT EXISTS address (id serial primary key, street varchar(255), number varchar(255), neighborhood varchar(255), city varchar(255), state varchar(255));")),
    (("CREATE TABLE IF NOT EXISTS locates (id serial primary key, latitude varchar(255) , longitude varchar(255), srid varchar(255), address_id varchar(255));"))
]
commands_getter_tables = [
    (
        
    )
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
        return 'Tables created'

    def insert_adress(self,adress):
        cursor = self.connector.cursor()
        data=(adress.street,adress.number,adress.neighborhood,adress.city,adress.state)
        sql=("INSERT INTO address (street,number,neighborhood,city,state) VALUES ('%s','%s','%s','%s','%s')"
        %(adress.street,adress.number,adress.neighborhood,adress.city,adress.state))
        cursor.execute(sql)
        cursor.close()

    def get_all_adress(self):
        cursor = self.connector.cursor()
        sql=("SELECT * FROM address")
        cursor.execute(sql)
        lista=[]
        for r in cursor.fetchall():
            lista.append(r)
        return lista

    def get_address(self,address):
        cursor = self.connector.cursor()
        sql=("SELECT * FROM address where street='%s' and number='%s' and neighborhood='%s' and city='%s' and state='%s'")
        cursor.execute(sql)
        print(cursor.fetch())


    def insert_locate(self,locate):
        cursor = self.connector.cursor()
        sql = ("INSERT INTO locates (latitude,longitude,srid,address_id) VALUES ('%s','%s','%s','%s')"
        %(locate.latitude,locate.longitude,locate.srid,locate.address_id))
        cursor.execute(sql)
        cursor.close()
    
    def get_all_locate(self):
        cursor = self.connector.cursor()
        sql = ("SELECT * FROM locates")
        cursor.execute(sql)
        lista_locates=[]
        for r in cursor.fetchall():
            lista_locates.append(r)
        return lista_locates
    
    def get_locate(self,locate):
        cursor=self.connector.cursor()
        sql=("SELECT * FROM locates WHERE latitude='%s' and longitude='%s' and srid='%s' and address_id='%s'"
        %(locate.latitude,locate.longitude,locate.srid,locate.address_id))
        cursor.execute(sql)
        print(cursor.fetch())
        

