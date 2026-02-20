# Forever method for movement and sound
def on_forever():
    distance = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
    if distance < stop_distance:
        cuteBot.stopcar()
        basic.pause(stop_time)
        cuteBot.move_time(cuteBot.Direction.RIGHT, turn_perc, turn_time)
    elif cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        cuteBot.motors(forward_left_speed, forward_right_speed)
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        cuteBot.motors(low_speed_turn, high_speed_turn)
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        cuteBot.motors(high_speed_turn, low_speed_turn)
    else:
        # When no object and both AIR sensors to 0
        cuteBot.stopcar()
        cuteBot.move_time(cuteBot.Direction.BACKWARD, backward_speed, backward_seconds)

# Main
stop_distance = 10
high_speed_turn = 60
low_speed_turn = 10
forward_left_speed = 50
forward_right_speed = 47
backward_speed = 40
backward_seconds = 0.2
turn_perc = 60
turn_time = 0.3
stop_time = 500
basic.forever(on_forever)
