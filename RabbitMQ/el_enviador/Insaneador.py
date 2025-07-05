import pika
import time

print("🐇 Insaneador despertando...")

# Intentos infinitos
while True:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='rabbit',
                port=5672,
                credentials=pika.PlainCredentials('MAXI', 'MAXI')
            )
        )
        print("🐇 Conejo encontrado, enviando 💌")
        break
    except pika.exceptions.AMQPConnectionError:
        print("🐇 Conejo dormido, retry en 5s 🫠")
        time.sleep(5)

channel = connection.channel()
channel.queue_declare(queue='insane_queue')

channel.basic_publish(exchange='',
                      routing_key='insane_queue',
                      body='Holi insaneado 🫶✨🐇')

print(" [x] Enviado: Holi insaneado")

connection.close()
