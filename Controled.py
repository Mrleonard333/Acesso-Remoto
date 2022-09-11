import pika
from os import system
from time import sleep
import pyautogui as auto

                # v Propriedades dos dados coletados
def callback(ch, method, propreties, body):
    auto.press(str(body.decode()))
                        # ^ Irá pressionar a tecla escolhida
    print(f'Pressing [{body.decode()}]')
                        # ^ Irá mostrar o conteudo do dado coletado
system('cls')
# ^ Irá limpar o cmd, apagando os prints anteriores
print('[Coding_Foundation] - [Manipulado]\n')

sleep(0.5)
# v Fará a conexão
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()                                     # ^ Em quê a conexão será estabelecida
channel.queue_declare(queue='Commands')
                    # ^ Declará onde os dados serão coletados
print('Connection started')
sleep(2.5)

auto.alert('[Dont press anything]')
                        # v Onde os dados serão coletados
channel.basic_consume(queue='Commands', auto_ack=None, on_message_callback=callback)
channel.start_consuming()                               # ^ Oque irá fazer ao receber os dados
# ^ Irá começar a coleta