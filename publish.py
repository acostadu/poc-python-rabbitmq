import os
import pika

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='hello')  # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello Quasar 2!')

print("[x] Sent 'Hello Quasar!'")
connection.close()
