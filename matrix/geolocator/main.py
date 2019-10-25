from model import Address
from model import Locate
from reader.hcsv import generate_csv_address


generate_csv_address(Address.get_all())

