import pkgutil
#import sqlite3 as lite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os

#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


"""
    vrati spojenie k databaze
"""

current_filedir_path = os.path.dirname(__file__)
#(sqlite:) engine_path = 'sqlite:///' + current_filedir_path + '/../../project.sqlite'

 # mysql
#engine_path = 'mysql://root:rafael@localhost:3306/radio3sk'
engine_path = 'mysql+mysqlconnector://root:rafael@localhost/radio3sk'

#db_path = "../../project.sqlite"

#engine_path = 'sqlite:///' + db_path
engine = create_engine(engine_path)
connection = engine.connect()

Session = sessionmaker(bind=connection)


_session = Session()

