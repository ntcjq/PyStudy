import json


def transfer():
    jsonStr = "{"
    # 通过for-in循环逐行读取
    with open('file/headerFile.txt', mode='r') as f:
        i = 1
        for line in f:
            #去除换行
            temp = line.replace("\n", "") 
            #转义"
            temp = temp.replace("\"", "\\\"")
            if i % 2 != 0:
                #去除:
                temp = temp[0:len(temp) - 1 ]
                jsonStr += f"\"{temp}\":"
            else:
                jsonStr += f"\"{temp}\","
            i += 1
    jsonStr = jsonStr[0:len(jsonStr) - 1]
    jsonStr += "}"
    print(jsonStr)


if __name__ == "__main__":
    transfer()