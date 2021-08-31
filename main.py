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
import tkinter as tk

play_button = "images/play_button.png"
chrome_button = "images/chrome_button.png"
write_button = "images/write_button.png"
to_who = "images/to_who.png"
subject = "images/subject.png"
send_button = "images/send.png"
attach = "images/attach_files.png"

pyautogui.screenshot("ss.png")
ss = "ss.png"

action = sys.argv[1]

class Finding:

    def show_find_thing(self):
        img_rgb = cv2.imread(ss)
        template = cv2.imread(find)
        w, h = template.shape[:-1]
        print(template.shape)
        result = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)


        threshold = .8
        loc = np.where(result >= threshold)
        print(loc)
    
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2)


        ''' <--- działa na "write_button" -->
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = (min_loc[0] + h, min_loc[1] + w)
        print(top_left)
        print(w)
        print(h)
        print(min_loc)
        print(max_val)

        bottom_right = (top_left[0] + h, top_left[1] + w)

        print(top_left)
        print(bottom_right)

        cv2.rectangle(img_rgb,top_left, bottom_right, (0,0,255), 2)
        <--- działa na "write_button" --> '''

        cv2.imwrite("result.png", img_rgb)


        #cv2.imshow('result.png', img_rgb)
        #cv2.waitKey(0)


if action == "play":
    find = play_button
    Finding.show_find_thing(find)


if action == "chrome":
    find = chrome_button
    Finding.show_find_thing(find)

if action == "write":
    find = write_button
    Finding.show_find_thing(find)

if action == "send":
    find = send_button
    Finding.show_find_thing(find)

if action == "files":
    find = attach
    Finding.show_find_thing(find)

if action == "who":
    find = to_who
    Finding.show_find_thing(find)

if action == "subject":
    find = subject
    Finding.show_find_thing(find)