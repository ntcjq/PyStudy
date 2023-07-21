"""
操作模式	具体含义
'r'	读取 （默认）
'w'	写入（会先清空之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）
"""

import json


def main():
    try:
        #获取文件 如果要写入的文件不存在会自动创建文件而不是引发异常
        f = open("file/a.txt", 'w', encoding='utf-8')
        for x in range(100):
            f.write(str(x) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        f.close()
    print('操作完成!')


#保存json数据
def writeJson():
    mydict = {
        'name':
        'Sea',
        'age':
        30,
        'qq':
        12345,
        'friends': ['王大锤', '白元芳'],
        'cars': [{
            'brand': 'BYD',
            'max_speed': 180
        }, {
            'brand': 'Audi',
            'max_speed': 280
        }, {
            'brand': 'Benz',
            'max_speed': 320
        }]
    }
    try:
        #对象转json写入到文件
        with open('file/data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
        #读取JSON文件转化成对象
        with open('file/data.json', 'r', encoding='utf-8') as f:
            newDict = json.load(f)
            print(type(newDict))
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()
    writeJson()