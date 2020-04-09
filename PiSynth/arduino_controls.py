import pyfirmata
import arduino_input_classes
board = pyfirmata.Arduino('COM11')

button1 = Button(6, 0, 10, 0)

def on_click(button):
    while True:
        if(button.get_pressed()):
            button.set_led_status(1)
        else:
            button.set_led_status(0)
