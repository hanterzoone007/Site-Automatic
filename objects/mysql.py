import pymysql


class MySql:

    def __init__(self,host,port,username,password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = self.connect()

    def connect(self):
        return pymysql.connect(host=self.host,
                                       port=self.port,
                                       user=self.username,
                                       password=self.password,
                                       autocommit=True)
    
    def query(self,query,params=None):
        with self.connection.cursor() as cursor:
            if params:
                cursor.executemany(query,params)
            else:
                cursor.execute(query)
            return cursor.fetchall()