from flask import Flask, jsonify, request
from mysql import MySQL, Error
from flask_cors import CORS

APP = Flask(
    __name__
)
CORS(APP, resources={r'*': {'origins': r'http://qztejm.coding-pages.com/*'}})
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
    material_id = request.args.get('id')
    sql = 'SELECT * from material WHERE id=%s'
    try:
        DB.execute_sql_command(sql, material_id)
    except Error as e:
        json = error_json(e)
        print(str(e))
        return jsonify(json)

    result = DB.cursor.fetchone()
    json = {
        'success': True,
        'errorMessage': '',
        'data': {
            'id': material_id,
            'name': result['name'],
            'endDate': result['end_date']
        }
    }
    return jsonify(json)

@APP.route('/material/list', methods=['GET'])
def get_material_list():
    name = request.args.get('name')
    materials = []
    if name != 'null':
        sql = 'SELECT * FROM material WHERE name LIKE CONCAT(\"%%\", %s, \"%%\")' #python需要2个%表示1个%
        try:
            DB.execute_sql_command(sql, name)
        except Error as e:
            json = error_json(e)
            print(str(e))
            return jsonify(json)

        materials = DB.cursor.fetchall()
    else:
        sql = 'SELECT * FROM material'
        try:
            DB.execute_sql_command(sql)
        except Error as e:
            json = error_json(e)
            print(str(e))
            return jsonify(json)
        materials = DB.cursor.fetchall()

    if len(materials) == 0:
        json = error_json('未找到符合的材料')
        return jsonify(json)
    else:
        sql = 'select * from user'
        DB.execute_sql_command(sql)
        users = DB.cursor.fetchall()
        user_list = []
        for user in users:
            json = {
                'id': user['id'],
                'name': user['name']
            }
            user_list.append(json)

        material_list = []                 
        for material in materials:
            requirement_list = []
            for user in users:
                sql = 'SELECT required FROM record WHERE material_id=%s AND user_id=%s'
                DB.execute_sql_command(sql, (material['id'], user['id']))
                required_number = DB.cursor.fetchone()              
                sql = 'SELECT owned FROM record WHERE material_id=%s AND user_id=%s'
                DB.execute_sql_command(sql, (material['id'], user['id']))
                owned_number = DB.cursor.fetchone()
                if required_number and owned_number:
                    json = {
                        'userId': user['id'],
                        'requiredNumber': required_number['required'],
                        'ownedNumber': owned_number['owned']
                    }
                    requirement_list.append(json)

            json = {
                'id': material['id'],
                'name': material['name'],
                'endDate': material['end_date'],
                'requirementList': requirement_list
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


@APP.route('/material/update', methods=['POST'])
def update_material_name():
    data = request.json
    sql = 'UPDATE material SET name=%(name)s, end_date=%(endDate)s WHERE id=%(id)s'
    try:
        DB.execute_sql_command(sql, data)
    except Error as e:
        json = error_json(e)
        print(str(e))
        return jsonify(json)
    json = {
        'success': True,
        'errorMessage': '',
    }
    return jsonify(json)

@APP.route('/material/updateRequirement', methods=['POST'])
def update_material_number():
    data = request.json
    sql = 'UPDATE record SET required=%(requiredNumber)s, owned=%(ownedNumber)s WHERE user_id=%(userId)s AND material_id=%(materialId)s'
    try:
        DB.execute_sql_command(sql, data)
    except Error as e:
        json = error_json(e)
        print(str(e))
        return jsonify(json)
    json = {
        'success': True,
        'errorMessage': '',
    }
    return jsonify(json)

@APP.route('/material/removeRequirement', methods=['POST'])
def remove_user_material():
    data = request.json
    print(data)
    sql = 'DELETE FROM record WHERE material_id=%(materialId)s AND user_id=%(userId)s'
    try:
        DB.execute_sql_command(sql, data)
    except Error as e:
        json = error_json(e)
        print(str(e))
        return jsonify(json)
    json = {
        'success': True,
        'errorMessage': '',
    }
    return jsonify(json)

@APP.route('/material/remove', methods=['POST'])
def remove_material():
    material_id = request.json['id']
    sql_commands = []
    sql_commands.append('DELETE FROM material WHERE id=%(id)s')
    sql_commands.append('DELETE FROM record WHERE material_id=%(material_id)s')
    info_list = []
    info_list.append({'id': int(material_id)})
    info_list.append({'material_id': int(material_id)})
    try:
        DB.execute_sql_transaction(sql_commands, info_list)
    except Error as e:
        json = error_json(e)
        print(str(e))
        return jsonify(json)
    json = {
        'success': True,
        'errorMessage': '',
    }
    return jsonify(json)

@APP.route('/material/save', methods=['POST'])
def add_material():
    material_name = request.json
    sql = 'INSERT INTO material (name, end_date) VALUES (%(name)s, %(endDate)s)'
    try:
        DB.execute_sql_command(sql, material_name)
    except Error as e:
        json = error_json(e)
        print(str(e))
        return jsonify(json)
    json = {
        'success': True,
        'errorMessage': '',
    }
    return jsonify(json)

@APP.route('/material/saveRequirement', methods=['POST'])
def add_material_record():
    data = request.json
    print(data)
    sql = 'INSERT INTO record (user_id, material_id, required, owned) VALUES (%(userId)s, %(materialId)s, %(requiredNumber)s, %(ownedNumber)s)'
    try:
        DB.execute_sql_command(sql, data)
    except Error as e:
        json = error_json(e)
        print(str(e))
        return jsonify(json)
    json = {
        'success': True,
        'errorMessage': '',
    }
    return jsonify(json)


@APP.route('/houtiao_person', methods=['GET'])
def show_houtiao():
    sql = 'SELECT * FROM houtiao_people'
    DB.execute_sql_command(sql)
    results = DB.cursor.fetchall()
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
    

if __name__ == '__main__':    
    APP.run(debug=True, host='127.0.0.1', port=8000)

