#########################################################################################
#
# Methods
#
#########################################################################################
# Method to rest
def rest():
    cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
    cuteBot.stopcar()
    basic.show_icon(IconNames.HEART)

# Method when press A
def on_button_pressed_a():
    global cont
    cont = 1

# Method when press B
def on_button_pressed_b():
    global cont
    cont = 2

# Method when press A + B
def on_button_pressed_ab():
    global cont
    cont = 3

# Forever 1 method (for movement)
def on_forever():
    if cont == 1:
        # LEDs
        basic.show_leds("""
                        # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
                        """)
        # Movement and lights
        cuteBot.move_time(cuteBot.Direction.RIGHT, square_turn_perc, square_turn_sec)
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 255, 80, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 98, 255, 180)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 222, 222, 40)
        basic.pause(square_lights_pause_end)
    elif cont == 2:
        # LEDS
        basic.show_leds("""
                . . # . .
                . . . . .
                . # . # .
                . . . . .
                # . # . #
                """)
        # Movement and lights
        cuteBot.move_time(cuteBot.Direction.RIGHT,
                triangle_turn_perc,
                triangle_turn_sec)
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 125, 144, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 15, 10, 233)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 155, 10, 190)
        basic.pause(square_lights_pause_end)
    elif cont == 3:
        # LEDs
        basic.show_leds("""
                . # # # .
                # . . . #
                # . . . #
                # . . . #
                . # # # .
                """)
        # Movement
        cuteBot.motors(circle_lspeed, circle_rspeed)
        # Lights
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 10, 244, 111)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 111, 10, 59)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 240, 190, 10)
        basic.pause(square_lights_pause_end)
    else:
        rest()

#########################################################################################
#
# Main
#
#########################################################################################
# Variables
## Square
square_lspeed = 50
square_rspeed = 46
square_turn_perc = 50
square_turn_sec = 0.3
square_ligths_pause = 350
square_lights_pause_end = 0
square_forward_pause = 1000

## Triangle
triangle_turn_perc = 50
triangle_turn_sec = 0.4

## Circle
circle_lspeed = 50
circle_rspeed = 20

# Execute
cont = 0
rest()
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
basic.forever(on_forever)
