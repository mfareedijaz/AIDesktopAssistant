import sys
from output_data import display_output
from time import sleep
def close():
    display_output("Closing application...")
    sleep(2)
    display_output("Application closed")
    sys.exit()
