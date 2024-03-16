import os
import ctypes
import random

def changeBackground():
    wallpaperPath = r'C:\Users\AHC\Pictures\Saved Pictures'
    wallpapers = os.listdir(wallpaperPath)
    # print(wallpapers)
    wallpapers = wallpapers[1:]
    # print(wallpapers)
    wallpaper = random.choice(wallpapers)
    # print(wallpaper)
    if wallpaper:
        FullPath = wallpaperPath + '/' +wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, FullPath, 3)
        return "Background image changed successfully"
    else:
        return "Unfortunately, the background image could not be changed."
    
# changeBackground()