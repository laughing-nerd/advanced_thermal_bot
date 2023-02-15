from time import sleep, sleep_ms, sleep_us
import network
import socket
from machine import Pin, ADC
import urequests
import utime
import _thread

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)
MOVE=True
TEMPERATURE=0
ssid=""
password=""

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="./style/style.css" /> -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />
    <style>
      * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
      }

      .remote-container {
        width: 100vw;
        min-height: 100vh;
        background-color: rgb(0, 0, 0);

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
      }

      .remote {
        width: 300px;
        height: 300px;
        border-radius: 10px;
        background-color: transparent;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden;
      }

      .remote-switches {
        width: 80%;
        height: 80%;
        background-color: transparent;
        border-radius: 50%;
        background: #000000;

        position: relative;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0px 0px 42px 0px rgba(255, 0, 0, 1);
      }

      .right {
        width: 50px;
        height: 50px;
        font-size: 44px !important;

        color: white;
        background: transparent;
        position: absolute;
        right: 0px;
        top: 40%;

        /* border: 1px red solid; */
        border-radius: 50%;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.3s;
      }

      .right:hover {
        background-color: rgba(239, 117, 117, 0.352);
      }

      .left {
        width: 50px;
        height: 50px;
        font-size: 44px !important;

        color: white;
        background: transparent;
        position: absolute;
        left: 0px;
        top: 40%;

        /* border: 1px red solid; */
        border-radius: 50%;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.3s;
      }

      .left:hover {
        background-color: rgba(239, 117, 117, 0.352);
      }

      .up {
        width: 50px;
        height: 50px;
        font-size: 44px !important;

        color: white;
        background: transparent;
        position: absolute;
        top: 3px;
        left: 40%;

        /* border: 1px red solid; */
        border-radius: 50%;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.3s;
      }

      .up:hover {
        background-color: rgba(239, 117, 117, 0.352);
      }

      .down {
        width: 50px;
        height: 50px;
        font-size: 44px !important;

        color: white;
        background: transparent;
        position: absolute;
        bottom: 0px;
        left: 40%;

        /* border: 1px red solid; */
        border-radius: 50%;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.3s;
      }

      .down:hover {
        background-color: rgba(239, 117, 117, 0.352);
      }

      button {
        border: transparent;
      }

      .power-on {
        width: 120px !important;
        height: 120px !important;
        border-radius: 50%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        background-color: rgba(30, 30, 30, 0.779);
        /* background-color: red; */
        color: white;

        box-shadow: 0px 0px 53px 0px rgba(255, 0, 0, 1);

        font-size: 18px;
        font-weight: 600;
        border: none;
      }

      .on-of-status {
        width: 120px !important;
        height: 120px !important;
        border-radius: 50%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        background-color: rgba(30, 30, 30, 0.779);
        color: white;

        box-shadow: 1px 5px 42px -3px rgba(0, 170, 255, 1);

        font-size: 18px;
        font-weight: 600;
        border: none;
      }

      @media only screen and (max-width: 600px) {
        .remote {
          width: 280px;
          height: 280px;
        }
      }
    </style>
  </head>
  <body>
    <div class="remote-container">
      <form class="remote">
        <div class="remote-switches">
          <button
            class="up fa fa-caret-up"
            name="button"
            value="forward"
            type="submit"
          ></button>

          <button
            class="left fa fa-caret-left"
            name="button"
            value="left"
            type="submit"
          ></button>

          <button
            class="right fa fa-caret-right"
            name="button"
            value="right"
            type="submit"
          ></button>

          <button
            class="down fa fa-caret-down"
            name="button"
            value="backward"
            type="submit"
          ></button>

          <button class="power-on" name="button" value="stop" type="submit">
            stop
          </button>
        </div>
      </form>
    </div>
  </body>
</html>

 """

#Motor Pins 
motor_left_1 = Pin(10, Pin.OUT)
motor_left_2 = Pin(13, Pin.OUT)
motor_right_1 = Pin(12, Pin.OUT)
motor_right_2 = Pin(11, Pin.OUT)

#In-built status led 
led = Pin("LED", Pin.OUT)

#HC-SR04 pins
echo = Pin(2, Pin.IN)
trigger = Pin(3, Pin.OUT)

#ThingSpeak
# HTTP_HEADERS={'Content-Type': 'aplication/json'}

def Forward():  
    motor_left_1.value(0)
    motor_left_2.value(1)
    motor_right_1.value(1)
    motor_right_2.value(0)
    
def Left():
    motor_left_1.value(1)
    motor_left_2.value(0)
    motor_right_1.value(1)
    motor_right_2.value(0)
    
def Backward():
    motor_left_1.value(1)
    motor_left_2.value(0)
    motor_right_1.value(0)
    motor_right_2.value(1)

def Right():
    motor_left_1.value(0)
    motor_left_2.value(1)
    motor_right_1.value(0)
    motor_right_2.value(1)

def Stop():
    motor_left_1.value(0)
    motor_left_2.value(0)
    motor_right_1.value(0)
    motor_right_2.value(0)

def wifi_conector():
    global ip
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if (wlan.status()==3):
        wlan.disconnect()
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Conected IP: {ip}')
    led.value(1)
    return ip
    
def socket_fun(ip):
    add = (ip, 80)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.bind(add)
    except:
        connection.close()
        connection.bind(add)
        
    connection.listen(5)
    while True:
        cliente = connection.accept()[0]
        request = cliente.recv(1024)
        request  = str(request)
        mot_forward = request.find('button=forward')
        mot_backward = request.find('button=backward')
        mot_right = request.find('button=right')
        mot_left = request.find('button=left')
        mot_stop = request.find('button=stop')
        
        if mot_forward  == 8 and MOVE==True:
            print('forward')
            Forward()
        elif mot_left == 8 and MOVE==True:
            print('left')
            Left()
        elif mot_stop  == 8:
            print('stop')
            Stop()
        elif mot_right == 8 and MOVE==True:
            print('right')
            Right()
        elif mot_backward  == 8 and MOVE==True:
            print('backward')
            Backward()
        cliente.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
        cliente.send(html)
        cliente.close()

    
def ultra():
    global MOVE
    global TEMPERATURE
    while True:
#         #Temperature
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = 27 - (reading - 0.706)/0.001721
        TEMPERATURE=temperature
        print (temperature)
#         #HC-SR04 output
        trigger.value(0)
        utime.sleep_us(2)
        trigger.value(1)
        utime.sleep_us(2)
        trigger.value(0)
        utime.sleep_us(2)
        while echo.value() == 0:
            signaloff = utime.ticks_us()
        while echo.value() == 1:
            signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        if (distance<12):
            MOVE=False
            Stop()
        else:
            MOVE=True
        utime.sleep_us(400_000)
    
led.value(1)
sleep(1)
led.value(0)
ip = wifi_conector()
_thread.start_new_thread(ultra,())
socket_fun(ip)






