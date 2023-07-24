import pymysql


def getConnect():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='Cjq51729',
                           db='springboot')
    return conn


def printVersion(conn):
    # 使用 cursor() 方法创建一个游标对象 cursor
    with conn.cursor() as cursor:
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        print("Database version : %s " % data)


def createTable(conn):
    # 使用 cursor() 方法创建一个游标对象 cursor
    with conn.cursor() as cursor:
        # 使用 execute() 方法执行 SQL，如果表存在则删除
        cursor.execute("DROP TABLE IF EXISTS Employee")
        # 使用预处理语句创建表
        createSql = """
                CREATE TABLE Employee (
                FIRST_NAME  CHAR(20) NOT NULL,
                LAST_NAME  CHAR(20),
                AGE INT,  
                SEX CHAR(1),
                INCOME FLOAT )
                """
        cursor.execute(createSql)


def insert(conn):
    with conn.cursor() as cursor:
        # SQL 插入语句
        sql = """
            INSERT INTO Employee(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES 
            ('Mac', 'Mohan', 20, 'F', 2000),
            ('Jack', 'Moyu', 21, 'M', 5000),
            ('Jone', 'Mona', 23, 'M', 3000),
            ('Amy', 'Mobi', 31, 'M', 500);
            """
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            print("新增异常")
            # 如果发生错误则回滚
            conn.rollback()


def update(conn):
    with conn.cursor() as cursor:
        try:
            affected_rows = cursor.execute(
                'update `Employee` set INCOME = 10000 where `FIRST_NAME`= "Amy"'
            )
            if affected_rows == 1:
                print('更新用户Amy成功!')
            # 提交到数据库执行
            conn.commit()
        except:
            print("更新异常")
            # 如果发生错误则回滚
            conn.rollback()


def delete(conn):
    with conn.cursor() as cursor:
        try:
            affected_rows = cursor.execute(
                'delete from `Employee` where `FIRST_NAME`="Mac"')
            if affected_rows == 1:
                print('删除用户Mac成功!')
            # 提交到数据库执行
            conn.commit()
        except:
            print("删除异常")
            # 如果发生错误则回滚
            conn.rollback()


def select(conn):
    with conn.cursor() as cursor:
        # SQL 查询语句
        sql = "SELECT * FROM Employee"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                (fname, lname, age, sex, income ))


if __name__ == "__main__":
    try:
        conn = getConnect()
        printVersion(conn)
        createTable(conn)
        insert(conn)
        select(conn)
        print("=" * 30)
        update(conn)
        select(conn)
        print("=" * 30)
        delete(conn)
        select(conn)
    except RuntimeError as err:
        print(err)
        print("出现异常")
    finally:
        #关闭连接释放资源
        conn.close()
        print("执行结束")
