import sqlite3
import pytz
import dateutil
from prettytable import PrettyTable

# 连接到数据库（如果不存在则会创建新的数据库文件）
conn = sqlite3.connect('example.db')

# 创建游标对象
cursor = conn.cursor()

# 创建表
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   age INTEGER)''')

# 插入数据
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Alice', 18))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Tom', 18))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Bob', 22))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)",
               ('Charlie', 19))

# 提交事务
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print("query", row)

# 更新数据
cursor.execute("UPDATE students SET age = ? WHERE name = ?", (21, 'Alice'))
conn.commit()

# 删除数据
cursor.execute("DELETE FROM students WHERE age > ?", (20, ))
conn.commit()

# 查询删除后的数据
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print("delete query", row)

# prettyTbale
table = PrettyTable()
table.title = "学生信息"
table.field_names = ["姓名", "年龄"]
for row in rows:
    table.add_row([row[0], row[1]])
print(table)

# 关闭游标和连接
cursor.close()
conn.close()