from sense_hat import SenseHat
sense = SenseHat()

from time import sleep

import time
start_time = time.time()

white = (255, 255, 255)
teal = (66, 244, 182)

bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], teal)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
         ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y +1):
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[0] == 0:
        sense.show_message("You Lose")
    
    
def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1
sense.stick.direction_up = move_up

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1
sense.stick.direction_down = move_down



while True:
    sense.clear(0, 0, 0)
    draw_bat()
    draw_ball()
    if time.time() - start_time < 15:
        sleep(0.50)
    if time.time() - start_time >= 15:
        sleep(0.25)
    if time.time() - start_time >= 30:
        sense.show_message("You Win!")
    
        
