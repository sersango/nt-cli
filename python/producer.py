#!/usr/bin/python
import sys
import json
from os import path
from kafka import KafkaProducer
from google.protobuf.json_format import Parse

def main(file):
	with open(file) as json_file:
		json_data = validateJSON(json_file)
	 	if (not json_data):
	 		print("The file '{0}' contains a wrong formed JSON".format(file))
	 	else:
			print('Sending message: {0}'.format(json_data))
			# protobuf_data = parseJsonToProtobuf(json_data)
			sendJSON(json_data)

def validateJSON(file):
	try:
		return json.load(file)
	except ValueError as err:
		return False

def parseJsonToProtobuf(json_data):
	return Parse(json.dumps(json_data), Person())

def sendJSON(json_data):
	producer = KafkaProducer(
		value_serializer=lambda m: json.dumps(m).encode('utf-8'),
		bootstrap_servers=['localhost:9092'])

	producer.send('protopic', value=json_data)
	producer.flush()

if __name__ == "__main__":
	argv = sys.argv[1:]
	if (not len(argv) == 1):
		print("It is mandatory to pass a file as parameter")
	elif(not path.isfile(argv[0])):
		print("The argument '{0}' must by a file".format(argv[0]))
	else:
		main(argv[0])
