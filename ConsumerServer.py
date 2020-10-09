from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='localhost:9091',
                         client_id='1',
                         auto_offset_reset='earliest'
                        )

consumer.subscribe(['udacity.data.streaming.project.two.san.fran.police'])

for message in consumer:
    print(message.value)