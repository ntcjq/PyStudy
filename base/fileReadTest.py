import time
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


def main():
    f = None
    try:
        f = open('file/test.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


def withTest():
    try:
        #如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
        with open('file/test.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


def readLineTest():
    print("=" * 30)
    # 一次性读取整个文件内容
    with open('file/test.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('file/test.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(1)
    print()

    # 读取文件按行读取到列表中
    with open('file/test.txt') as f:
        lines = f.readlines()
    print(lines)


#图片复制
#二进制读写
def picCopy():
    try:
        #'r'	读取 （默认）
        #'b'	二进制模式
        #组合使用
        with open('file/ftype.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('file/car.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
    readLineTest()
    picCopy()