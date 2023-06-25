import pyautogui
from pynput.keyboard import Listener, KeyCode
from threading import Thread

pyautogui.PAUSE = 0.001

class Bot:
    def __init__(self) -> None:
        self.running = True
        self.kill_switch = KeyCode(char=']')
        self.active = False
        self.toggle_key = KeyCode(char='[')
        self.keyboard = Listener(on_press=self.key_press)

    def start(self) -> None:
        self.keyboard.start()
        while self.running:
            continue

    def key_press(self, key) -> None:
        if key == self.kill_switch:
            self.kill()
            return
        if key == self.toggle_key:
            self.toggle_active()

    def kill(self) -> None:
        self.running = False

    def toggle_active(self) -> None:
        self.active = not self.active


class Upgrader(Thread):
    def __init__(self) -> None:
        super().__init__(daemon=True)
        self.target = 'images/upgrade_border.png'
        self.active = False

    def toggle_active(self) -> None:
        self.active = not self.active

    def run(self) -> None:
        while True:
            if self.active:
                try:
                    x,y = pyautogui.locateCenterOnScreen(self.target, region=(1600, 40, 64, 950))
                    pyautogui.click(x,y)
                except:
                    continue



class Builder(Thread):
    def __init__(self) -> None:
        super().__init__(daemon=True)
        self.green = (102, 255, 102)
        self.active = False
    
    def toggle_active(self) -> None:
        self.active = not self.active

    def run(self) -> None:
        i = 1
        while True:
            if self.active:
                print(i)
                i += 1
                for x in range(1718, 1725):
                    for y in range(40, 1016, 7):
                        if pyautogui.pixelMatchesColor(x, y, self.green):
                            pyautogui.click(x,y)



class BikiBot(Bot):
    def __init__(self) -> None:
        super().__init__()
        self.upgrader = Upgrader()
        self.builder = Builder()

    def start(self):
        self.keyboard.start()
        self.upgrader.start()
        self.builder.start()
        while self.running:
            if self.active:
                pyautogui.click(x=290,y=450)

    def toggle_active(self) -> None:
        super().toggle_active()
        self.upgrader.toggle_active()
        self.builder.toggle_active()


if __name__ == "__main__":
    bot = BikiBot()
    bot.start()


