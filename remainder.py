from winotify import Notification, audio
from win10toast import ToastNotifier
import time

def about():
    toast = Notification(app_id="ABOUT DEVELOPER",
                     title="AI Desktop Assistant",
                     msg="Feel free to share your thoughts or suggestions with us; click the button below to get in touch and contribute to our continuous improvement."
                    #  icon=r"c:\path\to\icon.png"
                    )
    toast.add_actions(label="About Developer", 
                    launch="https://portfolio-mfareed.netlify.app/")
    # toast.set_audio(audio.Reminder, loop=False)
    toast.show()

def notification(title, message, duration):
    try:
        toaster = ToastNotifier()
        time.sleep(duration)
        toaster.show_toast(title, message, duration=0)
    except Exception as e:
        print(f"An error occurred: {e}")
