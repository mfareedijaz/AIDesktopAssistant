from datetime import datetime, date

def get_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M")
    return current_time

def get_hours():
    now = datetime.now()

    current_time = now.strftime("%H")
    return current_time

def get_date():
    return str(date.today())