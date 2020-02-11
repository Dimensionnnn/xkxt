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
                return jsonify(errno='ok', errmsg="登录成功", sno=data[0], sname=data[1])
            else:
                return jsonify(errno='notok', errmsg="用户名或密码错误")
        else:
            return jsonify(errno='notok', errmsg="用户名或密码错误")
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")

@app.route("/getallcourse", methods=['GET', 'POST'])
def option():
    json_data = request.json                            # 获取数据
    sno = json_data.get('sno')
    a = json_data.get('logn')
    print(a)
    try:
        with DB() as db:
            sql = 'SELECT * FROM course'
            db.execute(sql)
            data = db.fetchall()
            sql = 'SELECT cno FROM sc WHERE sno = "%s"'%sno
            db.execute(sql)
            sc = db.fetchall()
            chosed = []
            for i in sc:
                chosed.append(int(i[0])-1)
            res = chose1(len(data), chosed)
            return jsonify(errno='ok', errmsg="获取成功", data=data, cho = res)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")
def chose1(n, l):
    res = []
    for i in range(n):
        if i not in l:
            res.append(i)
    return res

@app.route("/optioncourse", methods=['GET', 'POST'])
def optioncourse():
    json_data = request.json                            # 获取数据
    direction = json_data.get('direction')
    keys = json_data.get('keys')
    sno = json_data.get('sno')
    try:
        with DB() as db:
            if direction == 'left':
                for i in keys:
                    sql = 'INSERT INTO sc(sno, cno) VALUES("%s", "%02d")'%(sno, i+1)
                    db.execute(sql)
            else:
                for i in keys:
                    sql = 'DELETE FROM sc WHERE sno = "%s" and cno = "%02d"'%(sno, i+1)
                    db.execute(sql)
            return jsonify(errno='ok', errmsg="选课成功")
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")

@app.route("/mycourse")
def mycourse():
    return render_template("mycourse.html")

@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/query", methods=['POST'])
def query():
    # 查询个人课程成绩
    json_data = request.json
    sno = json_data.get('sno')
    print(sno)
    cname = []
    grade = []
    js = {}
    try:
        with DB() as db:
            sql = 'SELECT course.cname,sc.grade FROM sc,course WHERE sc.cno = course.cno and sno = "%s"' % sno
            db.execute(sql)
            data = db.fetchall()
            for i in data:
                cname.append(i[0])
                grade.append(i[1])
            js['cname'] = cname
            js['grade'] = grade
        print(js)
        return jsonify(errno='ok', data=js)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


@app.route("/inputGrade")
def inputGrade():
    return render_template("inputGrade.html")


@app.route("/grade", methods=["POST", "GET"])
def grade():

    json_data = request.form  # 获取数据
    cno = json_data.get("cno")  # 按课程号查询所有选课学生成绩
    print(cno)
    try:

        with DB() as db:
            if cno:
                sql = 'SELECT student.sname,sc.sno,sc.grade FROM sc,student WHERE sc.sno = student.sno and  sc.cno= "%s"' % cno
                db.execute(sql)
                data = db.fetchall()
                return render_template("grade.html", data=data)
            else:
                return render_template("grade.html")
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
    app.run(debug = True, host= '0.0.0.0', port='9000')
