import keyboard
from datetime import datetime, timedelta
import time


def get_dates():
    real_date = datetime.now()
    comfort_date = real_date - timedelta(hours=9)
    return real_date, comfort_date


def main(key_event):
    real_date, comfort_date = get_dates()
    if key_event.event_type == 'down':
        with open(comfort_date.strftime('%d-%m-%Y') + '.txt', 'a') as file:
            file.write(str(real_date) + '\n')


if __name__ == '__main__':
    keyboard.hook(main)
    while True:
        time.sleep(10)
