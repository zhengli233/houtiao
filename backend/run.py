from flask import Flask, jsonify, request
from mysql import MySQL, Error

APP = Flask(
    __name__
)

DB = MySQL()


@APP.route('/material/get', methods=['GET'])
def material_get():
    json = request.json
    id = json['id']
    sql = 'SELECT * from matrial WHERE id=%s'%(id)
    rtn = []
    try:
        DB.execute_sql_command(sql)
    except Error as e:
        json = {
            'success': False,
            'errorMessage': str(e),
            'data': {}
        }
        rtn.append(json)
        return rtn


    json = {
            'success': True,
            'errorMessage': '',
            'data': {
                'name': DB.cursor.fetchall()[0][0]
            }
        }
    rtn.append(json)
    return rtn



@APP.route('/houtiao_person', methods=['GET'])
def show_houtiao():
    results = DB.getAll()
    APP.logger.info(results)
    rtn = []
    for row in results:
        json = {
            'name': row[0],
            'level': row[1],
            'time': row[2]
        }
        rtn.append(json)
    
    return jsonify(rtn)

@APP.route('/write_houtiao_name', methods=['POST'])
def write_houtiao():
    json = request.json
    name = json['name']
    level = json['level']
    return DB.write2Table(name=name, level=level)
    

@APP.route('/delete_houtiao', methods=['POST'])
def delete_houtiao():
    json = request.json
    name = json['name']
    return DB.deleteRow(name=name)
    

if __name__ == '__main__':    
    APP.run(host='127.0.0.1', port=8000)
