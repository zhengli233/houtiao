import pymysql

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
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        except pymysql.Error as error:
            print(str(error))
            raise Error(str(error))

    def renew_cursor(self):
        '''更新数据库游标'''
        if self.conn.open:
            self.conn.close()
        self._connect_db()

    def execute_sql_command(self, sql_command, info=None):
        '''执行sql语句，返回当前游标'''
        try:
            self.renew_cursor()
            self.cursor.execute(sql_command, info)
            self.conn.commit()
        except pymysql.Error as error:
            print(str(error))
            self.conn.rollback()
            raise Error(str(error))

    def execute_sql_transaction(self, sql_commands, info_list=None):
        '''执行一组命令组成的事务'''
        try:
            self.renew_cursor()
            for index, sql_command in enumerate(sql_commands):
                if(info_list == None):
                    self.cursor.execute(sql_command)
                else:
                    self.cursor.execute(sql_command, info_list[index])
            self.conn.commit()
        except pymysql.Error as error:
            print(str(error))
            self.conn.rollback()
            raise Error(str(error))

'''
if __name__ == '__main__':
    db = MySQLCommand()
    db.connectMysql()
    rtn = db.write2Table(name='123', level='1')
    print('-----------------')
    print(rtn)
    db.conn.close()
'''