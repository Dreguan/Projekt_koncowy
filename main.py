'''
INSTRUKCJA:

python main.py *przycisk, który chcemy wyszukać na ekranie*

Dostępne przyciski do wyszukania:
1. "play"
2. "chrome"
'''

import sys
import pyautogui
import cv2
import numpy as np

play_button = "play_button.png"
chrome_button = "chrome_button.png"

pyautogui.screenshot("ss.png")
ss = "ss.png"

akcja = sys.argv[1]


class Finding:

    def show_find_thing(self):
        img_rgb = cv2.imread(ss)
        template = cv2.imread(find)
        w, h = template.shape[:-1]
        result = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .8
        loc = np.where(result >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        cv2.imwrite('result.png', img_rgb)


if akcja == "play":
    find = play_button
    Finding.show_find_thing(find)

if akcja == "chrome":
    find = chrome_button
    Finding.show_find_thing(find)

