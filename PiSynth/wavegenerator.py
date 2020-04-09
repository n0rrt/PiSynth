import math 
import pyaudio
import pyfirmata
import time

board = pyfirmata.Arduino('COM11')
it = pyfirmata.util.Iterator(board)
it.start()
time.sleep(0.05)
PyAudio = pyaudio.PyAudio

BITRATE = 16000

pin = board.get_pin('a:5:i')

length = 1
frames = int(BITRATE * length)
restframes = frames % BITRATE

p = PyAudio()
while True:
    wavedata = ''
    
    frequency = pin.read() * 1000
    if frequency is not None and frequency != 0:
        wavedata = wavedata + chr(int(math.sin(100/((BITRATE/frequency)/math.pi))*127+128))
        
    
    stream = p.open(format = p.get_format_from_width(1), channels = 1, rate = BITRATE, output = True)
    stream.write(wavedata)
stream.stop_stream()
stream.close()
p.terminate()