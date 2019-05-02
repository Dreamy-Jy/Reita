'''
This code contains all the constants associated with database
functionality.
'''

# Database URL
db_dialect = 'sqlite:///' 
'''
^NOTE the amount of '/'s is import
automate this in the future? - @Dreamy Jy
'''
db_path = '/Users/jordanethomas/Projects/Mobile-Apps/Reita/backend/database/data/'
db_file_name = 'test.db'
db_url = db_dialect+db_path+db_file_name

'''
NOTE sqlite won't be used in the future
therefore our database URLs will look radically different
below are some variables that make more sense in the future


Generalized database URL > dialect+driver://username:password@host:port/database
taken from: https://docs.sqlalchemy.org/en/13/core/engines.html
 - @Dreamy Jy
'''
db_driver, db_username, db_password, db_host, db_port = [None, None, None, None, None]
# Database URL