// ########################################################################################
// 
//  Methods
// 
// ########################################################################################
//  Method to rest
function rest() {
    cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
    cuteBot.stopcar()
    basic.showIcon(IconNames.Heart)
}

//  Method when press A
//  Method when press B
//  Method when press A + B
//  Forever 1 method (for movement)
// ########################################################################################
// 
//  Main
// 
// ########################################################################################
//  Variables
// # Square
let square_lspeed = 50
let square_rspeed = 46
let square_turn_perc = 50
let square_turn_sec = 0.3
let square_ligths_pause = 350
let square_lights_pause_end = 0
let square_forward_pause = 1000
// # Triangle
let triangle_turn_perc = 50
let triangle_turn_sec = 0.4
// # Circle
let circle_lspeed = 50
let circle_rspeed = 20
//  Execute
let cont = 0
rest()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    cont = 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    cont = 2
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    cont = 3
})
basic.forever(function on_forever() {
    if (cont == 1) {
        //  LEDs
        basic.showLeds(`
                        # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
                        `)
        //  Movement and lights
        cuteBot.moveTime(cuteBot.Direction.right, square_turn_perc, square_turn_sec)
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 255, 80, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 98, 255, 180)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 222, 222, 40)
        basic.pause(square_lights_pause_end)
    } else if (cont == 2) {
        //  LEDS
        basic.showLeds(`
                . . # . .
                . . . . .
                . # . # .
                . . . . .
                # . # . #
                `)
        //  Movement and lights
        cuteBot.moveTime(cuteBot.Direction.right, triangle_turn_perc, triangle_turn_sec)
        cuteBot.motors(square_lspeed, square_rspeed)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 125, 144, 10)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 15, 10, 233)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 155, 10, 190)
        basic.pause(square_lights_pause_end)
    } else if (cont == 3) {
        //  LEDs
        basic.showLeds(`
                . # # # .
                # . . . #
                # . . . #
                # . . . #
                . # # # .
                `)
        //  Movement
        cuteBot.motors(circle_lspeed, circle_rspeed)
        //  Lights
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 10, 244, 111)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 111, 10, 59)
        basic.pause(square_ligths_pause)
        cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 240, 190, 10)
        basic.pause(square_lights_pause_end)
    } else {
        rest()
    }
    
})
