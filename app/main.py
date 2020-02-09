from flask import Flask, jsonify, request, make_response, url_for, redirect, render_template, session
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
        with DB() as db:
            sql = 'SELECT sno, sname, pswd FROM student WHERE logn = "%s"' % logn
            db.execute(sql)
        data = db.fetchone()
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
    # 查询个人课程成绩
    try:
        with DB() as db:
            sql = 'SELECT course.cname,sc.grade FROM sc,course WHERE sc.cno = course.cno and sno = "%s"' % \
                  session['sno']
            db.execute(sql)
            data = db.fetchall()
        return render_template("query.html", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


@app.route("/inputGrade")
def inputGrade():
    return render_template("inputGrade.html")


@app.route("/grade", methods=["GET", 'POST'])
def grade():
    json_data = request.json  # 获取数据
    cno = json_data.get("cno")  # 按课程号查询所有选课学生成绩
    try:
        with DB() as db:
            sql = 'SELECT course.cname,sc.sno, sc.grade FROM sc,course WHERE course.cno=sc.cno = "%s"' % cno
            db.execute(sql)
            data = db.fetchall()
        return render_template("grade.html", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")

    return render_template("grade.html")


@app.route("/logout")
def logout():
    del session['sno']
    del session['sname']
    return redirect('/index')


class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(host="cdb-518aglpe.bj.tencentcdb.com", port=10101, user="root",
                                    password="zyx1999zyx",
                                    database="xkxt")
        self.cursor = self.conn.cursor()
        # self.num = self.cos.execute()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        self.cursor.close()

if __name__ == '__main__':
    app.run(debug = True, host= '0.0.0.0')
