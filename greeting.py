from time_module import get_hours
from output_data import display_output
from memory import update_last_seen, get_last_seen
from time_module import get_date

def greet():

    previous_date = get_last_seen()

    today_date = get_date()
    update_last_seen(today_date)

    if previous_date == today_date:
        display_output("Welcome back, sir")
    else:
        hours = int(get_hours())
        if hours >=4 and hours < 12:
            display_output("Good Morning!, sir")
        elif hours > 12 and hours <= 17:
            display_output("Good Afternoon!, sir")
        else:
            display_output("Good Evening!, sir")

