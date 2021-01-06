from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

class MySqlconn:
    def __init__(self):
        # Variable que determina si estamos conectados a MySQL...
        self.connected =0
        self.error =""


    def mysqlConnect(self, config):
        try:
            self.db = mysql.connector.connect(**config)
            self.cursor = self.db.cursor()
            self.connected=1
            return True
        except Exception as e:
            self.error="Error: %s" % (e)
        except:
            self.error="Error desconocido"
        return False


    def prepare(self,query,params=None,execute=True):
        """
        - query=> Sentencia sql
        - params => tupla con las variables
        - execute => devuelve los registros
        Devuelve False en caso de error
        """
        if self.connected:
            self.error=""
            try:
                self.cursor.execute(query,params)
                self.db.commit()
                if execute:
                    # convert de result to dictionary
                    result = []
                    columns = tuple([d[0].decode('utf8') for d in self.cursor.description])
                    for row in self.cursor:
                        result.append(dict(zip(columns, row)))
                    return result
                return True
            except Exception as e:
                self.error="Error: %s" % (e)
        return False

    def lastId(self):
        return self.cursor.lastrowid

    def affectedRows(self):
        return self.cursor.rowcount

    def mysqlClose(self):
        self.connected=0
        try:
            self.cursor.close()
        except:pass
        try:
            self.cnx.close()
        except:pass
