import os


result=[]

DATABASE_NAME = os.environ.get('DATABASE_NAME','Not Set Name Database')
DATABASE_HOST_CONNECT= os.environ.get('DATABASE_HOST','Not Set Host Connect')
DATABASE_USER = os.environ.get('DATABASE_USER', 'Not Set  User ')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'Not Set Password Database')
DATABASE_PORT = os.environ.get('DATABASE_PORT', 'Not Set Port Database')
GOOGLE_KEY_MATRIX=os.environ.get('GOOGLE_KEY_MATRIX','Not Set Key GOOGLE MATRIX')
GOOGLE_GEOCP_KEY=os.environ.get('GOOGLE_GEOCP_KEY', 'Not Set GEOCP KEY')

result=['DATABASE_NAME' , DATABASE_NAME], ['DATABASE_HOST_CONNECT', DATABASE_HOST_CONNECT], [
    'DATABASE_USER',DATABASE_USER
], ['DATABASE_PASSWORD', DATABASE_PASSWORD], ['DATABASE_PORT', DATABASE_PORT],['GOOGLE_KEY_MATRIX', GOOGLE_KEY_MATRIX],['GEOCP KEY', GOOGLE_GEOCP_KEY]


print(result)