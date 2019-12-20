from flask import Flask, jsonify, request
from mysql import MySQLCommand

APP = Flask(
    __name__
)

db = MySQLCommand()
db.connectMysql()

@APP.route('/houtiao_person', methods=['GET'])
def showHoutiao():
    results = db.getAll()
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
def writeHoutiao():
    json = request.json
    name = json['name']
    level = json['level']
    return db.write2Table(name=name, level=level)
    

@APP.route('/delete_houtiao', methods=['POST'])
def deleteHoutiao():
    json = request.json
    name = json['name']
    return db.deleteRow(name=name)
    

if __name__ == '__main__':    
    APP.run(host='127.0.0.1', port=8000)
