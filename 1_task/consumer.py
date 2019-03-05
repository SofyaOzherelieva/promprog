#!/usr/bin/env python
import pika
import traceback
import time
import sys


def callback(ch, method, properties, body):
    print("receive: ", body, flush = True)

time.sleep(20)

params = pika.ConnectionParameters(host= "rabbit", socket_timeout = 15)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='random')

print("Ready to receive messages")

channel.basic_consume(callback, queue='random')

while True:
	try:
	    channel.start_consuming()
	except pika.exceptions.ConnectionClosed:
	    channel.stop_consuming()
	    traceback.print_exc(file=sys.stdout)

connection.close()