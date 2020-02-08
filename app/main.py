from flask import Flask, jsonify, request, make_response, url_for, redirect, render_template, session, Session
import datetime
import pymysql

app = Flask(__name__, static_url_path = "")
app.config['SECRET_KEY'] = '123456'

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")
@app.route('/login/in', methods=['GET', 'POST'])    
def login_in():                                         # 用户输入信息登录
    json_data = request.json                            # 获取数据
    logn = json_data.get("logn")
    pswd = json_data.get("pswd")
    try:
        conn, cursor = conn2mysql() 
        sql = 'SELECT sno, sname, pswd FROM student WHERE logn = "%s"'%logn
        cursor.execute(sql)

        data = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        if data:
            if pswd == data[2]:
                session['sno'] = data[0]
                session['sname'] = data[1]
                session.permanent = True
                app.permanent_session_lifetime = datetime.timedelta(minutes=10)
                return jsonify(errno='ok', errmsg="登录成功")
            else:
                return jsonify(errno='notok', errmsg="用户名或密码错误")
        else:
            return jsonify(errno='notok', errmsg="用户名或密码错误")
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")

@app.route("/option")
def option():
    return render_template("option.html")

@app.route("/mycourse")
def mycourse():
    return render_template("mycourse.html")

@app.route("/query")
def query():
    return render_template("query.html")

def conn2mysql():
    conn = pymysql.connect(host="cdb-518aglpe.bj.tencentcdb.com", port=10101, user="root", password="zyx1999zyx",
                           database="xkxt")
    cursor = conn.cursor()
    return conn, cursor



if __name__ == '__main__':   
    app.run(debug = True, host= '0.0.0.0')
