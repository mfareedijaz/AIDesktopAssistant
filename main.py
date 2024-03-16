from input_data import take_input
from process_data import process_input
from output_data import display_output
from greeting import greet
from remainder import about, notification
from battery import battery_percentage
import os
os.system('cls')

greet()
about()
battery_percentage = battery_percentage()
if int(battery_percentage) < 65:
    notification("ALERT", "Please connect a charger your battery is less than 65%", 7)

while(True):
    i = take_input()
    processedInput = process_input(i)
    display_output(processedInput)