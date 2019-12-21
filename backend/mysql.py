import pymysql
from DBUtils.PersistentDB import PersistentDB

class Error(Exception):
    '''数据库错误'''
    pass



class MySQL(object):
    '''用来操作数据库的类'''
    def __init__(self):
        self.host = 'localhost'
        self.user = 'houtiaowang'  # 用户名
        self.password = 'houtiao'  # 密码
        self.db = 'playground' # 库
        self.table = 'houtiao_people'
        self._connect_db()

    def _connect_db(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,  
                user=self.user,
                password=self.password,
                db=self.db)
            self.cursor = self.conn.cursor()
        except pymysql.Error as error:
            print(str(error))
            raise Error(str(error))

    def renew_cursor(self):
        '''更新数据库游标'''
        if self.conn.open:
            self.conn.close()
        self._connect_db()

    def execute_sql_command(self, sql_command):
        '''执行sql语句，返回当前游标'''
        try:
            self.renew_cursor()
            self.cursor.execute(sql_command)
            self.conn.commit()
        except pymysql.Error as error:
            print(str(error))
            self.conn.rollback()
            raise Error(str(error))

    def write2Table(self, name, level):
        cmd = 'insert into %s (name, level, time) values ("%s", "%s", now());'%(self.table, name, level)
        try:
            self.renew_cursor()
            self.cursor.execute(cmd)
            self.conn.commit()
        except:
            print('insert table failed.')
            self.conn.rollback()  
            return 'failed'           

    def getNames(self):
        cmd = 'select name from %s' %(self.table)
        try:
            cursor = self.renew_cursor()
            cursor.execute(cmd)
            return cursor.fetchall()
        except:
            print('read table failed.')
            return 'failed'        

    def getLevel(self, name):
        cmd = 'select level from %s where name=%s'%(self.table, name)
        try:
            cursor = self.renew_cursor()
            cursor.execute(cmd)
            return cursor.fetchall()
        except:
            print('read table failed.')
            return 'failed' 

    def getAll(self):
        cmd = 'select * from %s'%(self.table)
        try:
            self.renew_cursor()
            cursor.execute(cmd)
            return cursor.fetchall()
        except:
            print('getAll(): read table failed.')
            return 'failed'

    def deleteRow(self, name):
        cmd = 'delete from %s where name=\"%s\"'%(self.table, name)
        try:
            cursor = self.renew_cursor()
            cursor.execute(cmd)
            self.conn.commit()
            return 'ok'
        except:
            print('delete table failed')
            self.conn.rollback()
            return 'failed' 

'''
if __name__ == '__main__':
    db = MySQLCommand()
    db.connectMysql()
    rtn = db.write2Table(name='123', level='1')
    print('-----------------')
    print(rtn)
    db.conn.close()
'''