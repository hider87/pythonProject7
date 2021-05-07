import pika


class Send:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hi')

    def __init__(self, res):
        self.channel.basic_publish(exchange='', routing_key='hi', body=res)
        print(" [x] Sent 'Hello World!'")

    # connection.close()
