try:
  import usocket as socket
except:
  import socket

from machine import Pin, PWM
import network
import esp

esp.osdebug(None)

import gc
gc.collect()

#nome da rede wifi
ssid = 'TCC Carrinho'
password = '123456789'

#criando a rede wifi
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

#ativando a red ewifi
while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

#define os pinos dos motores
esquerda1 = PWM(Pin(12))
esquerda2 = PWM(Pin(13))
direita1 = PWM(Pin(14))
direita2 = PWM(Pin(27))

velocidade = 0

#função para ativar os motores
def movimentar_robo(movimento, vel):
    if movimento == 'andar frente':
        esquerda1.duty(vel)
        esquerda2.duty(0)
        direita1.duty(vel)
        direita2.duty(0)
    if movimento == 'andar tras':
        esquerda1.duty(0)
        esquerda2.duty(vel)
        direita1.duty(0)
        direita2.duty(vel)
    if movimento == 'virar direita':
        esquerda1.duty(0)
        esquerda2.duty(0)
        direita1.duty(vel)
        direita2.duty(0)
    if movimento == 'virar esquerda':
        esquerda1.duty(vel)
        esquerda2.duty(0)
        direita1.duty(0)
        direita2.duty(0)
    if movimento == 'parar':
        esquerda1.duty(0)
        esquerda2.duty(0)
        direita1.duty(0)
        direita2.duty(0)

#cria a página html
def web_page():
  if esquerda1.duty() == 0:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """
    <html>
        <head>
            <title>ESP Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,">
        </head>
        <body>
            <h1>Controlar carrinho</h1>
            <p>Velocidade: <strong>""" + gpio_state + """</strong></p>
            <p><a href="/?velocidade=minima"><button class="button1">MINIMA</button></a>
            <a href="/?velocidade=media"><button class="button2">MEDIA</button></a>
            <a href="/?velocidade=maxima"><button class="button3">MAXIMA</button></a></p>
            <p><a href="/?andar=frente"><button class="button4">FRENTE</button></a></p>
            <p><a href="/?virar=esquerda"><button class="button5">ESQUERDA</button></a>
            <a href="/?virar=direita"><button class="button6">DIREITA</button></a></p>
            <p><a href="/?andar=tras"><button class="button7">TRAS</button></a></p>
            <p><a href="/?parar"><button class="button button8">PARAR</button></a></p>
        </body>
    </html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

#comunicacao do esp32 com a pagina web
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    #chama a pagina web que esta entre parenteses
    vel_min = request.find('/?velocidade=minima')
    vel_med = request.find('/?velocidade=media')
    vel_max = request.find('/?velocidade=maxima')
    andar_frente = request.find('/?andar=frente')
    virar_esquerda = request.find('/?virar=esquerda')
    virar_direita = request.find('/?virar=direita')
    andar_tras = request.find('/?andar=tras')
    parado = request.find('/?parar')
    
    if vel_min == 6:
        velocidade = 60
        print("velocidade: ", velocidade)
    if vel_med == 6:
        velocidade = 180
        print("velocidade", velocidade)
    if vel_max == 6:
        velocidade = 360
        print("velocidade", velocidade)
    if andar_frente == 6:
        movimentar_robo('andar frente', velocidade)
        print(velocidade)
    if parado == 6:
        movimentar_robo('parar', velocidade)
        velocidade=0
        print(velocidade)
    if andar_tras == 6:
        movimentar_robo('andar tras', velocidade)
        print(velocidade)
    if virar_direita == 6:
        movimentar_robo('virar direita', velocidade)
        print(velocidade)
    if virar_esquerda == 6:
        movimentar_robo('virar esquerda', velocidade)
        print(velocidade)
      
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
