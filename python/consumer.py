from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
   'protopic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=json.loads,
    bootstrap_servers='localhost:9092',
    session_timeout_ms=6000)

try:
    while True:
        msg_dict = consumer.poll(1000)
        if not bool(msg_dict):
            continue
        for key, msgs in msg_dict.items():
            for msg in msgs:
                if not hasattr(msg, 'error'):
                    print('Received message: {0}'.format(msg.value))
                else:
                    print('KAFKA ERROR: {0}'.format(msg.error))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()