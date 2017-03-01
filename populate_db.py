from db_connection import MySQLConnection
from config import Config
import json
import xml.etree.ElementTree as ET


class PopulateDB(object):
    
    def __init__(self):
        self.connection = MySQLConnection(Config.MYSQL_READ)
        
    def read_data(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        sub_root = root[0]
        for child in sub_root.findall('row'):
            title = child.find('title').text.replace('"', "'") if child.find('title') is not None else None
            location = child.find('locations').text.replace('"', "'") if child.find('locations') is not None else None
            insert_query = 'insert into movie_location (name, location) values ("%s", "%s")' % (title, location)
            self.connection.write_db(insert_query)
            
            
class_obj = PopulateDB()
class_obj.read_data(Config.DATAFILE)
        
