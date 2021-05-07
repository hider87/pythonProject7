import pika
import json
# 创建socket链接
# from src.predict1 import Predict
from src.Send import Send
from src.predict1 import Predict
import os
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', heartbeat=0))
# 创建管道
channel = connection.channel()
# 创建队列Predict
channel.queue_declare('hello')

# 声明回调函数

pre = Predict()


def callback(ch, method, properties, body):
    file_path = open('../data/cnews.simple1.txt', 'a', encoding='utf-8')
    file_path.write(body.decode())
    file_path.write('\n')
    sz = os.path.getsize('../data/cnews.simple1.txt')
    if sz != 0:
        res1 = pre.predict()
        # for val in res1:
        # res1 = '{"batman": "yes"}'
        print(res1)
        json1 = json.loads(res1)
        res = Send(res1)
        file_path.close()
        print()
        file_path = open('../data/cnews.simple1.txt', 'r+', encoding='utf-8')
        file_path.truncate()
        file_path.close()


# 如果接受到消息就调用回调函数,准备接受消息
channel.basic_consume('hello', callback, auto_ack=True)
print('[*] is waiting for receive mess press ctrl+c to exit')
# 开始消费消息
channel.start_consuming()
