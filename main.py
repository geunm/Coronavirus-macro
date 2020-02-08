import pyautogui
import time      # 30분 기다리기

page=(30,193)

while True:
    pyautogui.screenshot('./confirmed/' + time.strftime('%d-%H-%M', time.localtime(time.time())) + '.png', region=(22,195,130,80))
    pyautogui.screenshot('./deaths/' + time.strftime('%d-%H-%M', time.localtime(time.time()))+ '.png', region=(698,201,120,80))
    pyautogui.screenshot('./recovered/'+ time.strftime('%d-%H-%M', time.localtime(time.time()))+ '.png', region=(841,205,100,80))

    pyautogui.click(page)
    pyautogui.typewrite(['F5'])

    time.sleep(1800) # 30분 
