import psutil
from win10toast import ToastNotifier
import time

def check_battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if percent <= 30 and not plugged:
        toaster = ToastNotifier()
        toaster.show_toast(
            "Battery Low",
            f"{percent}% Battery remaining!!",
            duration=5,  # Duration in seconds
            threaded=True
        )

while True:
    check_battery()
    time.sleep(20)  # Check every 20 seconds
