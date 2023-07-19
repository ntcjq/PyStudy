import json

#dumps  python-->json
#loads  json-->python
print('='*30)

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


