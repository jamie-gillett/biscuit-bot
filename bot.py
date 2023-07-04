import pyautogui
# from pynput.keyboard import Listener, KeyCode
from pynput import keyboard
from threading import Thread
from multiprocessing import Process
# from PIL import Image

class BotComponent():
    def __init__(self, toggle_key='['):
        self.activated = False
        self.toggle_key = toggle_key

    def toggle_activity(self):
        self.activated = not self.activated
        if self.activated:
            Thread(target=self.active, daemon=True).start()

    def active(self):
        i = 1
        while self.activated:
            print(i, end='\r')
            i += 1

class Bot:
    def __init__(self) -> None:
        pyautogui.PAUSE = 0.001
        self.components : dict[str, list[BotComponent]] = {}
        self.kill_switch = keyboard.Key.esc

    def start(self) -> None:
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()

    def on_release(self, key: keyboard.Key):
        if key == self.kill_switch:
            return False
        print('{0} released'.format(key))
        if key.char in self.components:
            print("yup")
            for component in self.components[key.char]:
                component.toggle_activity()

    def add_component(self, component: BotComponent):
        if component.toggle_key not in self.components:
            self.components[component.toggle_key] = []
        self.components[component.toggle_key].append(component)

if __name__ == "__main__":
    test_bot = Bot()
    test_bot.add_component(
        BotComponent('[')
    )
    test_bot.start()