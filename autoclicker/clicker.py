import pyautogui as auto
import keyboard as key

start_key = input('Клавиша старта: ')
stop_key = input('Клавиша остановки: ')

while True:
    if key.is_pressed(start_key):
        auto.tripleClick()
    elif key.is_pressed(stop_key):
        break
