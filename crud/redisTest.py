import redis
import time


def main():
    #普通方式
    # redis_conn = redis.Redis(host='127.0.0.1', port= 6379, db= 0,decode_responses=True)
    #连接池方式（无需主动关闭连接）
    redis_pool = redis.ConnectionPool(host='127.0.0.1',
                                      port=6379,
                                      db=0,
                                      decode_responses=True)
    redis_conn = redis.Redis(connection_pool=redis_pool)
    redis_conn.set("name", "cjq", 2)
    if redis_conn.exists("name"):
        #bytes -> str
        print(redis_conn.get("name"))
    time.sleep(3)
    if redis_conn.exists("name"):
        print(redis_conn.get("name"))
    else:
        print("key not exist")


if __name__ == "__main__":
    main()
