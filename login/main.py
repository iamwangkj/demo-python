from flask import Flask, render_template, request
import pymysql
import traceback
# 传递根目录
app = Flask(__name__)

db_config = {
    'name': 'root',
    'password': '123456',
    'db': 'test_python'
}

'''
我是
多行注释
'''
# 默认路径访问登录页面
@app.route('/')
def login():
    return render_template('login.html')

# 默认路径访问注册页面
@app.route('/regist')
def regist():
    return render_template('regist.html')

    # 获取登录参数及处理
@app.route('/user', methods=['post'])
def createUser():
    conn = pymysql.connect("localhost", db_config['name'], db_config['password'], db_config['db'])
    cursor = conn.cursor()
    user = str(request.json['name'])
    password = str(request.json['password'])
    sql = "INSERT INTO user(user, password) VALUES ('%s','%s')" % (user, password)
    try:
        cursor.execute(sql)
        conn.commit()
        return 'ok'
    except: 
        traceback.print_exc()
        conn.rollback()
        return 'fail'

@app.route('/registuser')
def getRigistRequest():
    #把用户名和密码注册到数据库中
    #连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect("localhost", db_config['name'], db_config['password'], db_config['db'])
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    cursor.execute('select * from user where user=' + request.json['name'] + ' and password=' + request.json['password'])
    # SQL 插入语句
    sql = "INSERT INTO user(user, password) VALUES ("+request.args.get('user')+", "+request.args.get('password')+")"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
         #注册成功之后跳转到登录页面
        return render_template('login.html') 
    except:
        #抛出错误信息
        traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
        return '注册失败'
    # 关闭数据库连接
    db.close()

@app.route('/login', methods=['GET', 'POST'])
def getLoginRequest():
    try:
        connection = pymysql.connect("localhost", db_config['name'], db_config['password'], db_config['db'])
        # 使用cursor()方法获取操作游标
        cursor = connection.cursor()
        # SQL 查询语句
        sql = 'select * from user where user=' + request.json['name'] + ' and password=' + request.json['password']
        # 执行sql语句
        # return '1用户名或密码不正确'
        cursor.execute(sql)
        
        results = cursor.fetchall()
        print(len(results))
        if len(results) == 1:
            return '登录成功'
        else:
            return '用户名或密码不正确'
        # 提交到数据库执行
        connection.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        connection.rollback()
    # 关闭数据库连接
    connection.close()


# 使用__name__ == '__main__'是 Python 的惯用法，确保直接执行此脚本时才
# 启动服务器，若其他程序调用该脚本可能父级程序会启动不同的服务器
if __name__ == '__main__':
    app.run(debug=True)
