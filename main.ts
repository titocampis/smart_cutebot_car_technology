//  Forever method for movement and sound
//  Main
let stop_distance = 10
let high_speed_turn = 60
let low_speed_turn = 10
let forward_left_speed = 50
let forward_right_speed = 47
let backward_speed = 40
let backward_seconds = 0.2
let turn_perc = 60
let turn_time = 0.3
let stop_time = 500
basic.forever(function on_forever() {
    let distance = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
    if (distance < stop_distance) {
        cuteBot.stopcar()
        basic.pause(stop_time)
        cuteBot.moveTime(cuteBot.Direction.right, turn_perc, turn_time)
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_R_line)) {
        cuteBot.motors(forward_left_speed, forward_right_speed)
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_line_R_unline)) {
        cuteBot.motors(low_speed_turn, high_speed_turn)
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_unline_R_line)) {
        cuteBot.motors(high_speed_turn, low_speed_turn)
    } else {
        //  When no object and both AIR sensors to 0
        cuteBot.stopcar()
        cuteBot.moveTime(cuteBot.Direction.backward, backward_speed, backward_seconds)
    }
    
})
