import keyboard
import numpy as np
import cv2

from PIL import ImageGrab
import pyautogui
import time
import win32api, win32con
import threading
import ctypes

hpx=234
hpy=10
mpx=167
mpy=26

def hpmpbas():
    global hpx, hpy, mpx, mpy
    canr, cang, canb, = pyautogui.pixel(hpx, hpy)
    manar, manag, manab = pyautogui.pixel(mpx, mpy)

    if canr < 10:
        keyboard.press('8')
        time.sleep(0.03)
        keyboard.release('8')
    if manab < 10:
        keyboard.press('1')
        time.sleep(0.03)
        keyboard.release('1')


def caps_lock_state():
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


def z2bas():
    keyboard.press('2')
    time.sleep(0.3)
    keyboard.release('2')
    time.sleep(0.3)


def click(x, y):

    win32api.SetCursorPos((x, y))
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def solclick():

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def sagclick():

    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def kututopla2():
    screen = pyautogui.screenshot()
    try:
        location = pyautogui.locateCenterOnScreen('para.png', grayscale=True, confidence=0.8)
        click(location[0], location[1])
        time.sleep(0.2)
    except:
        time.sleep(0.2)

    try:
        location = pyautogui.locateCenterOnScreen('kekuri.png', grayscale=True, confidence=0.8)
        click(location[0], location[1])
        time.sleep(0.2)
        click(location[0], location[1])
    except:
        time.sleep(0.2)




def kututopla():
    slot = [[25, -125], [47, 0], [-47, 50], [47, 0], [-47, 50], [47, 0]]


    for i in slot:
        time.sleep(0.03)
        pyautogui.move(i)
        time.sleep(0.03)
        a = pyautogui.position()
        time.sleep(0.03)
        renk = pyautogui.pixel(a.x, a.y)
        time.sleep(0.03)
        if renk[0] > 5:
            time.sleep(0.03)
            sagclick()
            print("sagbasti")
            time.sleep(0.03)
        else:
            print("renksiyah")
            break


def skilbas():
    while True:
        capslockdurum = caps_lock_state()
        if capslockdurum == 1:

            hpmpbas()
            z2bas()
            time.sleep(0.2)


def govde():

    while True:
        capslockdurum = caps_lock_state()
        if capslockdurum==1:
            screen = np.array(ImageGrab.grab())
            screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.833
            loc = np.where(res >= threshold)

            coords = []
            for pt in zip(*loc[::-1]):
                coords.append(pt)

            if len(coords) > 0:
                center = (int(coords[0][0] + w / 2), int(coords[0][1] + h / 2))
                print("Found template at:", center)
                x, y = center

                min_distance = float('inf')
                closest_coord = None
                for coord in coords:
                    dist = np.sqrt((coord[0] - screen.shape[1] / 2) ** 2 + (coord[1] - screen.shape[0] / 2) ** 2)
                    if dist < min_distance:
                        min_distance = dist
                        closest_coord = coord

                x, y = closest_coord
                try:
                    click(x+30, y+50)
                    time.sleep(1.5)
                    sagclick()
                    time.sleep(0.1)
                    pyautogui.move(0,15)
                    sagclick()
                    time.sleep(0.1)
                    kututopla2()
                    time.sleep(0.2)


                except Exception as e:
                    print("Error clicking at ({}, {}): {}".format(x, y, e))
                    continue
            coords.clear()
        else:
            pass



if __name__ == "__main__":

    para = cv2.imread("para.png", 0)

    kekuri = cv2.imread("kekuri.png", 0)

    item5k = cv2.imread("5k.png", 0)

    template = cv2.imread('mob.png', 0)
    
    w, h = template.shape[::-1]
    t1 = threading.Thread(target=govde)
    t2 = threading.Thread(target=skilbas)
    t1.start()
    t2.start()
