import json

#dumps  python-->json
#loads  json-->python

# dump - 将Python对象按照JSON格式序列化到文件中 dump(pythonObject,file)
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象       obj = load(file)
# loads - 将字符串的内容反序列化成Python对象

print('=' * 30)

dd = {
    "code": "0000",
    "msg": "success",
    "result": {
        "access_token": "LGRHgrLGQ",
        "access_token_type": "bearer",
        "expiration_time": 1689323335
    }
}

jsonStr = json.dumps(dd)
print('json type = %s' % type(jsonStr))
dd2 = json.loads(jsonStr)
print('loads type = %s' % type(dd2))
