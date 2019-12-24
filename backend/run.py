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
    material_names = ''
    if name != 'null':
        sql = 'SELECT name FROM material WHERE name LIKE \"%' + '%s'%(name) + '%\"'
        try:
            DB.execute_sql_command(sql)
        except Error as e:
            json = error_json(e)
            print(str(e))
            return jsonify(json)

        material_names = DB.cursor.fetchall()
    else:
        sql = 'SELECT name FROM material'
        try:
            DB.execute_sql_command(sql)
        except Error as e:
            json = error_json(e)
            print(str(e))
            return jsonify(json)
        material_names = DB.cursor.fetchall()

    if len(material_names) == 0:
        json = error_json('未找到符合的材料')
        return jsonify(json)
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
                sql = 'SELECT required FROM record WHERE material_id=%s AND user_id=%s'%(material_id, user_id[0])
                DB.execute_sql_command(sql)
                required_number = DB.cursor.fetchall()              
                sql = 'SELECT owned FROM record WHERE material_id=%s AND user_id=%s'%(material_id, user_id[0])
                DB.execute_sql_command(sql)
                owned_number = DB.cursor.fetchall()
                if required_number and required_number[0][0] != None and owned_number and owned_number[0][0] != None:
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


@APP.route('/material/update', methods=['POST'])
def update_material_name():
    material_id = request.args.get('id')
    material_name = request.args.get('name')
    sql = 'UPDATE material SET name=%s WHERE id=%s'%(material_name, material_id)
    try:
        DB.execute_sql_command(sql)
    except Error as e:
        json = error_json(e)
        print(str(e))
        return jsonify(json)
    json = {
        'success': True,
        'errorMessage': '',
    }
    return jsonify(json)

@APP.route('/material/updateRequirement')
def update_material_number():
    user_id = request.args.get('userId')
    material_id = request.args.get('materialId')
    required_number = request.args.get('requiredNumber')
    owned_number = request.args.get('ownedNumber')
    sql = 'UPDATE record SET required=%s, owned=%s WHERE user_id=%s AND material_id=%s'%(required_number, owned_number, user_id, material_id)
    try:
        DB.execute_sql_command(sql)
    except Error as e:
        json = error_json(e)
        print(str(e))
        return jsonify(json)
    json = {
        'success': True,
        'errorMessage': '',
    }
    return jsonify(json)

@APP.route('/material/removeRequirement')
def remove_user_material():
    user_id = request.args.get('userId')
    material_id = request.args.get('materialId')
    sql = 'DELETE FROM record WHERE material_id=%s AND user_id=%s'%(material_id, user_id)
    try:
        DB.execute_sql_command(sql)
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
    material_id = request.args.get('id')
    sql_commands = []
    sql_commands.append('DELETE FROM material WHERE id=%s'%(material_id))
    sql_commands.append('DELETE FROM record WHERE material_id=%s'%(material_id))
    try:
        DB.execute_sql_transaction(sql_commands)
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
    material_name = request.args.get('name')
    sql = 'INSERT INTO material (name) VALUES (\"%s\")'%(material_name)
    try:
        DB.execute_sql_command(sql)
    except Error as e:
        DB.cursor.rollback()
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
