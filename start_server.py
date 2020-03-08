import os
import time
import pyautogui

os.startfile('C:/Users/AMALYGIN/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt')
time.sleep(0.5)
pyautogui.typewrite("C: \n")
pyautogui.typewrite("cd C:\\Users\\AMALYGIN\\PycharmProjects\\password_generator \n")
pyautogui.typewrite("python manage.py runserver 3333 \n")
