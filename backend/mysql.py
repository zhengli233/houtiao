import pymysql

class MySQLCommand(object):
    # 类的初始化
    def __init__(self):
        self.host = 'localhost'
        self.user = 'houtiaowang'  # 用户名
        self.password = 'houtiao'  # 密码
        self.db = 'playground' # 库
        self.table = 'houtiao_people'  # 表

    # 链接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,  
                user=self.user,
                password=self.password,
                db=self.db)
            self.cursor = self.conn.cursor()
            print('connect database success.')
        except:
            print('connect mysql error.')

    def getCursor(self):
        if self.conn.open:
            self.conn.close()
        self.connectMysql()
        return self.cursor

    def write2Table(self, name, level):
        cmd = 'insert into %s (name, level, time) values ("%s", "%s", now());'%(self.table, name, level)
        try:
            cursor = self.getCursor()
            cursor.execute(cmd)
            self.conn.commit()
        except:
            print('insert table failed.')
            self.conn.rollback()  
            return 'failed'           

    def getNames(self):
        cmd = 'select name from %s' %(self.table)
        try:
            cursor = self.getCursor()
            cursor.execute(cmd)
            return cursor.fetchall()
        except:
            print('read table failed.')
            return 'failed'        

    def getLevel(self, name):
        cmd = 'select level from %s where name=%s'%(self.table, name)
        try:
            cursor = self.getCursor()
            cursor.execute(cmd)
            return cursor.fetchall()
        except:
            print('read table failed.')
            return 'failed' 

    def getAll(self):
        cmd = 'select * from %s'%(self.table)
        try:
            cursor = self.getCursor()
            cursor.execute(cmd)
            return cursor.fetchall()
        except:
            print('getAll(): read table failed.')
            return 'failed'

    def deleteRow(self, name):
        cmd = 'delete from %s where name=\"%s\"'%(self.table, name)
        try:
            cursor = self.getCursor()
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