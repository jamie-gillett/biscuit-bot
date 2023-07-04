from bot import ProcessComponent, Bot
from PIL import Image
import pyautogui

pyautogui.PAUSE = 0.001

def builder():
    for x in range(1718, 1725):
        for y in range(40, 1016, 7):
            if pyautogui.pixelMatchesColor(x, y, (102, 255, 102)):
                pyautogui.click(x,y)

def upgrader(image, grayscale=True, region=None):
    try:
        x,y = pyautogui.locateCenterOnScreen(image, grayscale=grayscale, region=region)
        pyautogui.click(x,y)
    except:
        pass

if __name__ == "__main__":
    bikibot = Bot()
    bikibot.add_component( ProcessComponent(target=pyautogui.click, kwargs={'x':290,'y':450}) )
    bikibot.add_component( ProcessComponent(target=builder) )
    upgrade_image = Image.open('images/upgrade_border.png')
    upgrade_kwargs = {
        'image': upgrade_image,
        'grayscale': True,
        'region': (1600, 40, 64, 950)
    }
    bikibot.add_component( ProcessComponent(target=upgrader, kwargs=upgrade_kwargs) )
    bikibot.start()