import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import ctypes

# read before run
# print("WARNING, the program will keep on running until 'e' is pressed!")
# print("press 's' to start and pause.")
print("running")
delay = 0.000001
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


# def on_press(key):
#     if key == start_stop_key:
#         if click_thread.running:
#             # click_thread.stop_clicking()
#             # ctypes.windll.user32.MessageBoxW(0, "Program paused. Press s to cont'd or press e to exit program", "Your title", 0x1000)
#             # print("Program pause.")
#             # changed here to press s to exit program too
#             click_thread.exit()
#             listener.stop()
#             ctypes.windll.user32.MessageBoxW(0, "Program exit.", "Your title", 0x1000)
#         else:
#             click_thread.start_clicking()
#     elif key == exit_key:
#         click_thread.exit()
#         listener.stop()
#         print("Program EXIT.")
#         ctypes.windll.user32.MessageBoxW(0, "Program exit.", "Your title", 0x1000)

def on_press2(key):
    if click_thread.running:
        click_thread.exit()
        listener.stop()
        print("Program EXIT.")
        ctypes.windll.user32.MessageBoxW(0, "Program exit.", "Your title", 0x1000)
    elif key == start_stop_key:
        click_thread.start_clicking()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Press s to start auto click", "Your title", 0x1000)


# with Listener(on_press=on_press) as listener:
#     listener.join()

with Listener(on_press=on_press2) as listener:
    listener.join()
