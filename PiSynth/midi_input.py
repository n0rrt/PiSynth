import pygame
from pygame import midi
import pyfirmata
import time
import pyaudio
import math
PyAudio = pyaudio.PyAudio
BITRATE = 320000

length = 0.5
frames = int(BITRATE * length)
restframes = frames % BITRATE

p = PyAudio()

midi.init()
input = midi.Input(midi.get_default_input_id())
board = pyfirmata.Arduino('COM11')
it = pyfirmata.util.Iterator(board)
it.start()
time.sleep(0.05)
pin = board.get_pin('d:3:o')
while True:
    wavedata = ''
    new_input = input.read(1)

    if new_input != []:
        print(new_input)
        frequency = midi.midi_to_frequency(new_input[0][0][1])
        for x in range(frames):
            if frequency is not None and frequency != 0:
                wavedata = wavedata + chr(int(math.sin(x/((BITRATE/frequency)/math.pi))*127+128))
        
    new_input = []
    stream = p.open(format = p.get_format_from_width(1), channels = 1, rate = BITRATE, output = True)
    stream.write(wavedata)
stream.stop_stream()
stream.close()
p.terminate()