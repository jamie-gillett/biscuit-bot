from bot import ProcessComponent, Bot
import pyautogui

pyautogui.PAUSE = 0.001

if __name__ == "__main__":
    bikibot = Bot()
    bikibot.add_component( ProcessComponent(target=pyautogui.click, kwargs={'x':290,'y':450}) )
    bikibot.start()