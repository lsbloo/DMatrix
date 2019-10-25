from core.manager import createConnetor,insertAddress,getAllAddress,getAddress

class Address(object):
    def __init__(self,street,number,neighborhood,city,state):
        self.number=number
        self.neighborhood=neighborhood
        self.city=city
        self.state=state
        self.street=street
    def save(self):
        createConnetor()
        insertAddress(self)

    def get_address(self):
        getAddress(self)

    def get_all():
        createConnetor()
        q = getAllAddress()
        print(q)

class Locate(object):
    def __init__(self,latitude,longitude,srid,address_id):
        self.latitude=latitude
        self.longitude=longitude
        self.srid=srid
        self.address_id=address_id
    

    