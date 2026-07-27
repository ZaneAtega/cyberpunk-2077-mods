import time
from threading import Thread
from pygetwindow import getActiveWindow
from pynput.mouse import Button, Controller, Listener

holding = False
controller = Controller()

def on_click(x, y, button, pressed):
    global holding

    if (window := getActiveWindow()) and window.title != "Cyberpunk 2077 (C) 2020 by CD Projekt RED":
        holding = False
        return

    if button == Button.middle and (holding := pressed):
        Thread(target=spam, daemon=True).start()

def spam():
    while holding:
        controller.click(Button.left)
        time.sleep(0.05)

if __name__ == "__main__":
    Listener(on_click=on_click).run()