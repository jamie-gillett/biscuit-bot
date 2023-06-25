import pyautogui
from pynput.keyboard import Listener, KeyCode

pyautogui.PAUSE = 0.01

class Bot:
    def __init__(self) -> None:
        self.running = True
        self.kill_switch = KeyCode(char=']')
        self.active = False
        self.toggle_key = KeyCode(char='[')
        self.keyboard = Listener(on_press=self.key_press)

    def start(self):
        self.keyboard.start()
        while self.running:
            if self.active:
                pyautogui.click()

    def key_press(self, key):
        if key == self.kill_switch:
            self.running = False
            return
        if key == self.toggle_key:
            self.active = not self.active


if __name__ == "__main__":
    bot = Bot()
    bot.start()


