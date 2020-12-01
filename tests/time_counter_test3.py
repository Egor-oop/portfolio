import time
from datetime import datetime
import keyboard as key


class TimeCounter:
    def __init__(self):
        self.now_none = datetime.now()
        self.current_time_none = self.now_none.strftime('%H:%M')

    def time_now(self):
        return self.current_time_none

    @staticmethod
    def time_now_counter():
        while True:
            now = datetime.now()
            current_time = now.strftime('%H:%M')

            if now.strftime('%S') == '00':
                print(current_time)
                time.sleep(1)
            elif key.is_pressed('alt+q'):
                break
            else:
                continue


tc = TimeCounter()
print(tc.time_now())
print(tc.time_now_counter())
