#!/usr/bin/env python
import pika
import time
import random
import sys


time.sleep(20)


conn_params = pika.ConnectionParameters(host = "rabbit")
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()
channel.queue_declare(queue='random')

while True:
	try:
		number = random.randint(-100, 100)
		time.sleep((number + 100)/50)
		print('send: ', number, flush = True)

		channel.basic_publish(exchange='', routing_key='random',
		  body=str(number))
	except pika.exceptions.ConnectionClosed:
	    print("lost connection")


connection.close()