import pyautogui as pa
import time
pa.hotkey('winleft','r')
pa.write('cmd')
pa.press('enter') 
pa.write('ipconfig/flushDNS')
pa.press('enter')
time.sleep(3)
pa.write('del /q/f/s %TEMP%\*')
pa.press('enter')
time.sleep(5)
pa.hotkey('alt','f4')
pa.hotkey('winleft')
pa.write('Cleanmgr')
pa.press('enter')
pa.press('enter')
time.sleep(3)
pa.press('enter')
pa.press('enter')