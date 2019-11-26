from flask import Flask, render_template, jsonify

APP = Flask(
    __name__, static_folder='../houtiao'
)

@APP.route('/')
def home():
    '''
    主页
    '''
    return render_template('index.html')

@APP.route('/houtiao_person', methods=['GET', 'POST'])
def showHoutiao():
    rtn = {
        'name': 'Hua Xiaocheng houtiao'
    }
    return jsonify(rtn)

if __name__ == '__main__':
    APP.run(debug=True, host='127.0.0.1')
