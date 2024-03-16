import screen_brightness_control as sbc

def setBrightness(set):
    sbc.set_brightness(set)
    getBrightness = sbc.get_brightness()
    return getBrightness