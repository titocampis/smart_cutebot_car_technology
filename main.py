# Forever method for movement and sound
def on_forever():
    global repeat, playing, happy

    distance = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
    
    # Filter hallucinations
    if distance == 0:
        pass
    elif distance < stop_distance:
        if repeat < 10:
            cuteBot.stopcar()
            music.stop_all_sounds()
            music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            repeat = repeat + 1
            playing = False
        else:
            cuteBot.move_time(cuteBot.Direction.RIGHT, turn_perc, turn_time)
            repeat = 0
        happy = False
    else:
        if not playing:
            music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
                music.PlaybackMode.LOOPING_IN_BACKGROUND)
            playing = True
        if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
            cuteBot.motors(forward_left_speed, forward_right_speed)
        elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
            cuteBot.motors(low_speed_turn, high_speed_turn)
        elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
            cuteBot.motors(high_speed_turn, low_speed_turn)
        else:
            cuteBot.stopcar()
            cuteBot.move_time(cuteBot.Direction.BACKWARD, backward_speed, backward_seconds)
        happy = True
        repeat = 0

# Forever method for faces
def on_forever_faces():
    if happy:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)

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
repeat = 0
playing = False
happy = True

basic.forever(on_forever)
basic.forever(on_forever_faces)
