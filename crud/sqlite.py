import sqlite3
from contextlib import closing
from prettytable import PrettyTable


def getConnect():
    # 连接到数据库（如果不存在则会创建新的数据库文件）
    conn = sqlite3.connect('file/example.db')
    return conn


def createTable(conn):
    with closing(conn.cursor()) as cursor:
        # 创建表
        cursor.execute('''CREATE TABLE IF NOT EXISTS students
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER)''')


def insert(conn):
    # 创建游标对象
    with closing(conn.cursor()) as cursor:
        try:
            # 插入数据
            cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)",
                           ('Alice', 18))
            cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)",
                           ('Tom', 18))
            cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)",
                           ('Bob', 22))
            cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)",
                           ('Charlie', 19))
            # 提交事务
            conn.commit()
        except:
            conn.rollback()


def update(conn):
    # 创建游标对象
    with closing(conn.cursor()) as cursor:
        try:
            # 更新数据
            cursor.execute("UPDATE students SET age = ? WHERE name = ?",
                           (21, 'Alice'))
            # 提交事务
            conn.commit()
        except:
            conn.rollback()


def delete(conn):
    # 创建游标对象
    with closing(conn.cursor()) as cursor:
        try:
            # 删除数据
            cursor.execute("DELETE FROM students WHERE age > ?", (20, ))
            # 提交事务
            conn.commit()
        except:
            conn.rollback()


def deleteAll(conn):
    # 创建游标对象
    with closing(conn.cursor()) as cursor:
        try:
            # 删除数据
            cursor.execute("DELETE FROM students")
            # 提交事务
            conn.commit()
        except:
            conn.rollback()


def select(conn):
    with closing(conn.cursor()) as cursor:
        # 查询数据
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        # prettyTbale
        table = PrettyTable()
        table.title = "学生信息"
        table.field_names = ["ID", "姓名", "年龄"]
        for row in rows:
            table.add_row([row[0], row[1], row[2]])
        print(table)


if __name__ == "__main__":
    try:
        conn = getConnect()
        createTable(conn)
        deleteAll(conn)
        insert(conn)
        select(conn)
        update(conn)
        select(conn)
        delete(conn)
        select(conn)
    except RuntimeError as err:
        print(err)
    finally:
        conn.close()
    print("执行结束")