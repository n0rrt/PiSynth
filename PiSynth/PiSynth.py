import pyfirmata
import time
import matplotlib.pyplot as plt
from pippi import dsp, fx

board = pyfirmata.Arduino('COM11')
it = pyfirmata.util.Iterator(board)
it.start()
time.sleep(0.05)
board.analog[5].enable_reporting()

pin = board.analog[5]
button4 = board.get_pin('d:13:i')
button3 = board.get_pin('d:12:i')
button2 = board.get_pin('d:11:i')
button1 = board.get_pin('d:10:i')
pin1 = board.get_pin('d:7:i')
pin2 = board.get_pin('d:8:i')
led4 = board.get_pin('d:3:o')
led3 = board.get_pin('d:4:o')
led2 = board.get_pin('d:5:o')
led1 = board.get_pin('d:6:o')
min_bpm = 60
max_bpm = 200

def blink_sequence(bpm):
    if bpm is not None:
        led1.write(1)
        time.sleep(bpm)
        led1.write(0)

        led2.write(1)
        time.sleep(bpm)
        led2.write(0)
        
        led3.write(1)
        time.sleep(bpm)
        led3.write(0)
        
        led4.write(1)
        time.sleep(bpm)
        led4.write(0)
def on_click():
    if button1.read() == 1 and led1.read() == 0:
        led1.write(1)
    if button2.read() == 1:
        led2.write(1)
    if button3.read() == 1:
        led3.write(1)
    if button4.read() == 1:
        led4.write(1)
    else:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
while True:
    if pin.read() != 0 and pin.read() is not None:
        print('bpm:', 60 / pin.read())

    on_click()
