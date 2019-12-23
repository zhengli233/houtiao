from flask import Flask, jsonify, request
from mysql import MySQL, Error

APP = Flask(
    __name__
)

DB = MySQL()

def error_json(e):
    json = {
        'success': False,
        'errorMessage': str(e),
        'data': {}
    }
    return json


@APP.route('/material/get', methods=['GET'])
def get_material_name():
    id = request.args.get('id')
    sql = 'SELECT name from material WHERE id=%d'%(int(id))
    rtn = []
    try:
        DB.execute_sql_command(sql)
    except Error as e:
        json = error_json(e)
        rtn.append(json)
        print(str(e))
        return jsonify(rtn)

    result = DB.cursor.fetchall()
    print(result)
    json = {
        'success': True,
        'errorMessage': '',
        'data': {
            'name': result[0][0]
        }
    }
    rtn.append(json)
    return jsonify(rtn)

@APP.route('/material/list', methods=['GET'])
def get_material_list():
    name = request.args.get('name')
    rtn = []
    material_names = ''
    if name != 'null':
        sql = 'SELECT name FROM material WHERE name LIKE \"%' + '%s'%(name) + '%\"'
        try:
            DB.execute_sql_command(sql)
        except Error as e:
            json = error_json(e)
            rtn.append(json)
            print(str(e))
            return jsonify(rtn)

        material_names = DB.cursor.fetchall()
    else:
        sql = 'SELECT name FROM material'
        try:
            DB.execute_sql_command(sql)
        except Error as e:
            json = error_json(e)
            rtn.append(json)
            print(str(e))
            return jsonify(rtn)
        material_names = DB.cursor.fetchall()

    if len(material_names) == 0:
        json = error_json('未找到符合的材料')
        rtn.append(json)
        return jsonify(rtn)
    else:
        sql = 'select * from user'
        DB.execute_sql_command(sql)
        user_ids = DB.cursor.fetchall()
        user_list = []
        for user_id in user_ids:
            json = {
                'id': user_id[0],
                'name': user_id[1]
            }
            user_list.append(json)

        material_list = []            
        for m_name in material_names:
            sql = 'SELECT id FROM material WHERE name=\"%s\"'%(m_name)
            DB.execute_sql_command(sql)
            material_id = DB.cursor.fetchall()[0][0]
            sql = 'SELECT id from user'
            DB.execute_sql_command(sql)
            user_ids = DB.cursor.fetchall()
            requirement_list = []
            for user_id in user_ids:
                sql = 'SELECT `%s` FROM required WHERE user_id=%s'%(material_id, user_id[0])
                DB.execute_sql_command(sql)
                required_number = DB.cursor.fetchall()
                print(required_number)                 
                sql = 'SELECT `%s` FROM owned WHERE user_id=%s'%(material_id, user_id[0])
                DB.execute_sql_command(sql)
                owned_number = DB.cursor.fetchall()
                print(owned_number)
                if required_number and owned_number:
                    json = {
                        'userId': user_id[0],
                        'requiredNumber': required_number[0][0],
                        'ownedNumber': owned_number[0][0]
                    }
                    requirement_list.append(json)

            json = {
                'id': material_id,
                'name': m_name[0],
                'requirementList': requirement_list,
            }
            material_list.append(json)

        rtn = {
            'success': True,
            'errorMessage': '',
            'data': {
                'materialList': material_list,
                'userList': user_list
            }
        }
        return jsonify(rtn)


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
    APP.run(debug=True, host='127.0.0.1', port=8000)
