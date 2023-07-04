from bot import ProcessComponent, Bot
from PIL import Image
import pyautogui

pyautogui.PAUSE = 0.001

def builder():
    GREEN = (102, 255, 102)
    for x in range(1710, 1740):
        for y in range(1016, 40, -7):
            if pyautogui.pixelMatchesColor(x, y, GREEN):
                pyautogui.click(x,y)

def image_clicker(image, grayscale=True, region=None):
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
    bikibot.add_component( ProcessComponent(target=image_clicker, kwargs={'image': upgrade_image, 'region':(1600, 40, 64, 950)}) )
    gold_image = Image.open('images/gold.png')
    bikibot.add_component( ProcessComponent(toggle_key=']', target=image_clicker, kwargs={'image': gold_image}) )
    bikibot.start()