from flask import Flask,request ,render_template , jsonify
from time import time, ctime, localtime


app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template('/index.html')

@app.route('/welcome',methods=['POST'])
def welcome_mes():
    if(request.method == 'POST'):
        name1 = request.form['name1']
        stobj=localtime()               #extrect all thing about time & date
        hour = stobj.tm_hour
        if 4<=hour<=12:
            result = f"Good Morning {name1}"
        elif 12<hour<20:
            result = f"Good Afternoon {name1}"
        elif 20<=hour<24 or 1<=hour<4:
            result = f"Good Night {name1}"
        result = result.split(' ')
        wel_mes = ' '.join([str(i) for i in result[0:2]])
        mes_name = ' '.join([str(i) for i in result[2:]])
        return render_template('results.html' , result = [wel_mes,mes_name])


@app.route('/postman_welcome',methods=['POST'])
def welcome_mes1():
    if(request.method == 'POST'):
        name1 = request.json['name1']
        stobj=localtime()               #extrect all thing about time & date
        hour = stobj.tm_hour
        if 4<=hour<=12:
            result = f"Good Morning {name1}"
        elif 12<hour<18:
            result = f"Good afternoon {name1}"
        elif 18<=hour<24 or 1<=hour<4:
            result = f"Good Night {name1}"
        result = result.split(' ')
        wel_mes = ' '.join([str(i) for i in result[0:2]])
        mes_name = ' '.join([str(i) for i in result[2:]])
        return jsonify([wel_mes,mes_name])
        # return render_template('results.html' , result = [wel_mes,mes_name])






if __name__=="__main__":
    # app.run(host="127.0.0.1", port=5000, debug=True)
    app.run(host="0.0.0.0")