import pyautogui
import time      # 30분 기다리기

page=(30,193)

pyautogui.screenshot('./confirmed/1.png', region=(22,195,130,80))
pyautogui.screenshot('./deaths/1.png', region=(698,201,120,80))
pyautogui.screenshot('./recovered/1.png', region=(841,205,100,80))

pyautogui.click(page)
pyautogui.typewrite(['F5'])
