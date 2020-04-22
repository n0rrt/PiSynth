import math 
import pyaudio
import pyfirmata
import time

board = pyfirmata.Arduino('COM11')
it = pyfirmata.util.Iterator(board)
it.start()
time.sleep(0.05)
PyAudio = pyaudio.PyAudio

BITRATE = 320000

pin = board.get_pin('a:4:i')

length = 0.1
frames = int(BITRATE * length)
restframes = frames % BITRATE

p = PyAudio()
while True:
    wavedata = ''
    
    frequency = pin.read() * 1000
    for x in range(frames):
        if frequency is not None and frequency != 0:
            wavedata = wavedata + chr(int(math.sin(x/((BITRATE/frequency)/math.pi))*127+128))
        
    
    stream = p.open(format = p.get_format_from_width(1), channels = 1, rate = BITRATE, output = True)
    stream.write(wavedata)
stream.stop_stream()
stream.close()
p.terminate()