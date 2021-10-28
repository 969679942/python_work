import pymysql
class MYSQLTool(object):
    def __init__(self,host,port,database,user,pwd,charset):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.pwd = pwd
        self.charset = charset

    def __connect(self):
        #创建连接 建立游标对象
        self.conn = None
        self.cursor = None
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    database=self.database,
                                    user=self.user,
                                    password=self.pwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    def __close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    #增删改
    def __cud(self,sql,params):
        rowcount = 0
        try:
            self.__connect()
            rowcount = self.cursor.execute(sql,params)
            self.conn.commit()
            self.__close()
        except Exception as e:
            print(e)
        return rowcount

    def insert(self,sql,params = []):
        return self.__cud(sql,params)

    def delete(self,sql,params = []):
        return self.__cud(sql,params)

    def update(self,sql,params = []):
        return self.__cud(sql,params)

    def select(self,sql,params = []): #查
        try:
            self.__connect()
            self.cursor.execute(sql,params)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

