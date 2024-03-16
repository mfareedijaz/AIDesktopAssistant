import tkinter as tk
from PIL import ImageGrab
from tkinter.filedialog import *
from time import sleep
from output_data import display_output

def ScreenShot():
    root = tk.Tk()
    window = tk.Canvas(root, width=200, height=200)
    window.pack()

    def takeScreenShot():
        display_output("Capturing screenshot...")
        root.withdraw()
        sleep(2)
        screen_shot = ImageGrab.grab()
        root.deiconify()
        save_path = asksaveasfilename()
        screen_shot.save(save_path+"_screenshot.png")

    screenShotButton = tk.Button(text="TAKE SCREENSHOT", command=takeScreenShot, font=5)
    window.create_window(100,100,window=screenShotButton)

    root.mainloop()