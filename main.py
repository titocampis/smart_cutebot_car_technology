def on_forever():
    global status, playing, repeat

    # --- CONTROLLER ---
    distance = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)

    if distance < stop_distance:
        if repeat < 10:
            status = 0
            repeat = repeat + 1
        else:
            status = 5
            repeat = 0
    elif cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        status = 1
        repeat = 0
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        status = 2
        repeat = 0
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        status = 3
        repeat = 0
    else:
        status = 4
        repeat = 0

    # --- ACT (movement) ---
    if status == 0:
        cuteBot.stopcar()
    elif status == 1:
        cuteBot.motors(forward_left_speed, forward_right_speed)
    elif status == 2:
        cuteBot.motors(low_speed_turn, high_speed_turn)
    elif status == 3:
        cuteBot.motors(high_speed_turn, low_speed_turn)
    elif status == 4:
        cuteBot.move_time(cuteBot.Direction.BACKWARD, backward_speed, backward_seconds)
    elif status == 5:
        cuteBot.move_time(cuteBot.Direction.RIGHT, turn_perc, turn_time)

    # --- ACT (sound) ---
    if status == 0:
        music.stop_all_sounds()
        music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
                        music.PlaybackMode.UNTIL_DONE)
        playing = False
    elif not playing:
        music._play_default_background(
            music.built_in_playable_melody(Melodies.PRELUDE),
            music.PlaybackMode.LOOPING_IN_BACKGROUND
        )
        playing = True

    # # --- Faces (LEDs screen) --- CANNOT GO HERE OVERLOAD AND FAIL
    # --> Needs to go into another forever
    # if status == 0:
    #     basic.show_icon(IconNames.SAD)
    # else:
    #     basic.show_icon(IconNames.HAPPY)

# Foreer faces to avoid overload
def on_forever_faces():
    if status == 0:
            basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.HAPPY)

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
status = 1

basic.forever(on_forever)
basic.forever(on_forever_faces)