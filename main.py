from time import sleep, sleep_ms, sleep_us
import network
import socket
from machine import Pin, ADC
import uasyncio
import urequests
import utime
import html_file #For the HTML file to be served
import credentials
import gc
import _thread
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)
MOVE=True

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
HTTP_HEADERS={'Content-Type': 'aplication/json'}
API=""

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
    wlan.connect(credentials.ssid, credentials.password)
    while wlan.isconnected() == False:
        print('waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Conected IP: {ip}')
    led.value(1)
    return ip
    
def socket_fun(ip):
    print("Hello")
    add = (ip, 80)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.bind(add)
    except:
        connection.close()
        connection.bind(add)
        
    connection.listen(5)
    while True:
        print("Hello")
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
        cliente.send(html_file.html)
        cliente.close()

    
async def ultra():
# def ultra():
    global MOVE
    while True:
#         #Temperature
#         reading = sensor_temp.read_u16() * conversion_factor
#         temperature = 27 - (reading - 0.706)/0.001721
#         print (temperature)

#         request=urequests.post('https://api.thingspeak.com/update?api_key=J3I0ZYEC4TMK6PL1&field1='+str(temperature), headers=HTTP_HEADERS)
#         request.close()
#         #HC-SR04 output
        trigger.value(0)
        utime.sleep_us(2)
#         await uasyncio.sleep_ms(2)
        trigger.value(1)
        utime.sleep_us(2)
#         await uasyncio.sleep_ms(2)
        trigger.value(0)
        utime.sleep_us(2)
#         await uasyncio.sleep_ms(2)

        while echo.value() == 0:
            signaloff = utime.ticks_us()
        while echo.value() == 1:
            signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        print(distance)
        if (distance<5):
            MOVE=False
            Stop()
        else:
            MOVE=True
#         request=urequests.post('https://api.thingspeak.com/update?api_key=J3I0ZYEC4TMK6PL1&field1='+str(distance), headers=HTTP_HEADERS)
#         request.close()
#         utime.sleep(1)
        await uasyncio.sleep_ms(200)
    
async def main():
    led.value(1)
    sleep(1)
    led.value(0)
    ip = wifi_conector()
#     await ultra()
    uasyncio.create_task(ultra())
    socket_fun(ip)    

uasyncio.run(main())
# led.value(1)
# sleep(1)
# led.value(0)
# ip = wifi_conector()
# _thread.start_new_thread(ultra,())
# socket_fun(ip)







