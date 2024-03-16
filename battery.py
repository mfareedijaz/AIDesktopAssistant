import psutil

def battery_percentage():
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
    return percent

def get_battery_percentage():
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
    return f'Remaining battery of your device is {percent}%'

def get_plugged_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    plugged = "plugged in" if plugged else "not plugged in"
    return f'Your device is {plugged}'