import pika
from os import system
from time import sleep
import pyautogui as auto

print('[Coding_Foundation] - [Controler]\n')

sleep(0.5)
# v Fará a conexão
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()                                     # ^ Em quê a conexão será estabelecida
channel.queue_declare(queue='Commands')
                    # ^ Declará onde os dados serão armazenados
print('Connection started [Dont use space]')
sleep(2.5)

while True:
    system('cls') # < Irá limpar o cmd, apagando os prints anteriores
    print('[1] PRESS LETTERS KEYS [a, b, f]')
    print('[2] PRESS ESPECIAL KEYS [win, shift, left]\n')
    TYPE = int(input('TYPE: '))
    system('cls')

    K1 = str(input('[EXIT/PURGE/KEYS] Key pressed: '))
    K2 = K1.split()
    Key = K2[0]

    if len(Key) > 1:
        pass

    if Key.upper() == 'EXIT':
        system('cls')
        print('[Terminating the System]')

        # v Irá fechar a conexão
        channel.close()
        connection.close()
        break
    if Key.upper() == 'PURGE':
        system('cls')
        print('- Purging queue...')
        channel.queue_purge(queue='Commands') # < Irá expurgar os dados da queue
        print('- Queue purged')
        sleep(1)
        continue

    if Key.upper() == 'KEYS':
        system('cls')
        for K in auto.KEYBOARD_KEYS: # < Irá mostrar separadamente as teclas que podem ser utilizadas
            print(f'[{str(K)}]')
        
        input('Exit: ')

    if TYPE == 1:
        if len(Key) > 1:
            for K in Key: # < Irá separar as letras 
                channel.basic_publish(exchange='', routing_key='Commands', body=K)
        else:
            channel.basic_publish(exchange='', routing_key='Commands', body=Key)
    else:
        channel.basic_publish(exchange='', routing_key='Commands', body=Key)
