import pyfirmata
board = pyfirmata.Arduino('COM11')

class Button():
    '''a physical button with an LED inside'''
    def __init__(self, led_port, pressed, button_port, button_action, led_status = 0):
        self._led_status = led_status
        self._led_port = led_port
        self._pressed = pressed
        self._button_port = button_port
        self._button_action = button_action
        board.digital[button_port].enable_reporting()
    def __str__(self):
        return str(self._button_port) + ' ' + str(self._led_port)
    def get_led_status(self):
        return self._led_status
    def get_led_port(self):
        return self._led_port
    def get_pressed(self):
        self._pressed = board.digital[self._button_port].read()
        return self._pressed
    def get_button_port(self):
        return self._button_port
    def get_action(self):
        return self._button_action

    def set_led_status(self, status):
        self._led_status = status
        board.digital[self._led_port].write(status)
    def set_led_port(self, port):
        self._led_port = port
    def set_button_port(self,port):
        self._button_port = port
    def set_action(self, action):
        self._button_action = action


class Rotary():
    '''a physical rotary stepper with button'''
    def __init__(self, left_port, right_port, button_port):
        self._left_port = left_port
        self._right_port = right_port
        self._button_port = button_port
    def __str__(self):
        return str(self._left_port) + " " + str(self._right_port) + " " + str(self._button_port)
    def get_left_port(self):
        return self._left_port
    def get_right_port(self):
        return self._right_port
    def get_button_port(self):
        return self._button_port
    def set_left_port(self, port):
        self._left_port = port
    def set_right_port(self, port):
        self._right_port = port
    def set_button_port(self, port):
        self._button_port = port




