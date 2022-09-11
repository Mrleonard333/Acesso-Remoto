# [Remote-Acess]
## Irá permitir que o usuario do sistema Controler.py<br>obter controle sobre o teclado do usuario do sistema Controled.py

# [Basics]
```
  [Coding_Foundation] - [Controled] | [Coding_Foundation] - [Controler]
                                    | 
  Connection started                | [1] PRESS LETTERS KEYS [a, b, f]
  Pressing [H]                      | [2] PRESS ESPECIAL KEYS [win, shift, left]
  Pressing [e]                      | TYPE: 1
  Pressing [l]                      |
  Pressing [l]                      | [EXIT/PURGE/KEYS] Key pressed: HelloWorld!
  Pressing [o]                      |
  Pressing [W]                      |
  Pressing [o]                      |
  Pressing [r]                      |
  Pressing [l]                      |
  Pressing [d]                      |
  Pressing [!]                      |
```
# [Purge]
```
  print('- Purging queue...')
  channel.queue_purge(queue='Commands') # < Irá expurgar os dados da queue
  print('- Queue purged')
```
# [Exit]
```
  system('cls')
  print('[Terminating the System]')

  # v Irá fechar a conexão
  channel.close()
  connection.close()
```

# [Keys]
```
if Key.upper() == 'KEYS':
system('cls')
for K in auto.KEYBOARD_KEYS: # < Irá mostrar separadamente as teclas que podem ser utilizadas
    print(f'[{str(K)}]')
        
input('Exit: ') 
```
