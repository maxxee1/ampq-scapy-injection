import pika
import time

print("🐇 Insaneado despertando...")

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
        print("🐇 Conejo encontrado, escuchando 📥")
        break
    except pika.exceptions.AMQPConnectionError:
        print("🐇 Conejo dormido, retry en 5s 🫠")
        time.sleep(5)

channel = connection.channel()
channel.queue_declare(queue='insane_queue')

def callback(ch, method, properties, body):
    print(f" [x] Recibido: {body.decode()} 🫶🐇😭")

channel.basic_consume(queue='insane_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Esperando locuras... Ctrl+C pa soltar todo 🧃')
channel.start_consuming()
