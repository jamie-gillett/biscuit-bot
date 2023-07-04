import pyautogui
from pynput.keyboard import Listener, KeyCode
from threading import Thread
from PIL import Image



class Bot:
    def __init__(self) -> None:
        pyautogui.PAUSE = 0.001
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
        self.target = Image.open('images/upgrade_border.png')
        self.active = False

    def toggle_active(self) -> None:
        self.active = not self.active

    def run(self) -> None:
        while True:
            if self.active:
                try:
                    x,y = pyautogui.locateCenterOnScreen(self.target, grayscale=True, region=(1600, 40, 64, 950))
                    pyautogui.click(x,y)
                except:
                    continue

class Builder(Thread):
    def __init__(self) -> None:
        super().__init__(daemon=True)
        image_files = ['shipment.png', 'wizard.png', 'temple.png', 'bank.png', 'factory.png', 'mine.png', 'farm.png', 'grandma.png', 'cursor.png']
        self.images = [Image.open('images/buildings/' + file) for file in image_files]
        self.active = False
    
    def toggle_active(self) -> None:
        self.active = not self.active

    def run(self) -> None:
        while True:
            if self.active:
                for image in self.images:
                    try:
                        x,y = pyautogui.locateCenterOnScreen(image, grayscale=True, region=(1600, 40, 64, 950))
                        pyautogui.click(x,y)
                        break
                    except:
                        continue

class Gold_Digger(Thread):
    def __init__(self) -> None:
        super().__init__(daemon=True)
        self.target = 'images/gold.png'
        self.active = False

    def toggle_active(self) -> None:
        self.active = not self.active

    def run(self) -> None:
        while True:
            if self.active:
                try:
                    x,y = pyautogui.locateCenterOnScreen(self.target, confidence=0.8)
                    pyautogui.click(x,y)
                except:
                    continue

class BikiBot(Bot):
    def __init__(self) -> None:
        super().__init__()
        # self.components = [Upgrader(), Builder(), Gold_Digger()]
        # self.components = [Upgrader(), Builder()]
        self.components = [Upgrader()]

    def start(self):
        self.keyboard.start()
        for component in self.components:
            component.start()
        while self.running:
            if self.active:
                pyautogui.click(x=290,y=450)

    def toggle_active(self) -> None:
        super().toggle_active()
        for component in self.components:
            component.toggle_active()


if __name__ == "__main__":
    bot = BikiBot()
    bot.start()