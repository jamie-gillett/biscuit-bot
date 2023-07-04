import pyautogui
from pynput.keyboard import Listener, Key
from multiprocessing import Process

class ProcessComponent():
    def __init__(self, toggle_key='[', target=None, args=[], kwargs={}):
        self.toggle_key = toggle_key
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.process = None

    def toggle_activity(self):
        if not self.process:
            self.process = Process(target=self.activity, daemon=True)
            self.process.start()
        else:
            self.process.terminate()
            self.process = None

    def activity(self):
        if not self.target:
            print("No activity designated for ProcessComponent")
            return
        elif self.kwargs:
            while True:
                self.target(**self.kwargs)
        elif self.args:
            while True:
                self.target(*self.args)
        else:
            while True:
                self.target()

class Bot:
    def __init__(self) -> None:
        pyautogui.PAUSE = 0.001
        self.components : dict[str, list[ProcessComponent]] = {}
        self.kill_switch = Key.esc

    def start(self) -> None:
        with Listener(on_release=self.on_release) as listener:
            listener.join()

    def on_release(self, key: Key):
        if key == self.kill_switch:
            return False
        if key.char in self.components:
            for component in self.components[key.char]:
                component.toggle_activity()

    def add_component(self, component: ProcessComponent):
        if component.toggle_key not in self.components:
            self.components[component.toggle_key] = []
        self.components[component.toggle_key].append(component)

# if __name__ == "__main__":
#     test_bot = Bot()
#     test_bot.add_component()
#     test_bot.start()