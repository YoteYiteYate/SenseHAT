from sense_hat import SenseHat
sense = SenseHat()

white = (255, 255, 255)

bat_y = 4

#function ------------------------------

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)
# Main Program -------------------------

draw_bat()
