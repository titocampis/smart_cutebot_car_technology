# Vehicles Automation Activity
## Lights
### Automatic headlights
```python
# Forever method
def on_forever():
    if input.light_level() >= threshold_light:
        cuteBot.color_light(cuteBot.RGBLights.ALL, 0x000000)
    else:
        cuteBot.color_light(cuteBot.RGBLights.ALL, 0xffffff)

# Main
threshold_light = 16
basic.forever(on_forever)
```

## Ultrasound Sensor
### Park helper
```python
# Forever method
def on_forever():
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) <= threshold_high:
        music.stop_all_sounds()
        music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    elif cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) <= threshold_mid:
        music.stop_all_sounds()
        music.play(music.tone_playable(523, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    elif cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) <= threshold_low:
        music.stop_all_sounds()
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        music.stop_all_sounds()

# Main
threshold_high = 5
threshold_mid = 12
threshold_low = 20
basic.forever(on_forever)
```

### Remaining
// Copy from MSI python codes for intermitents (easy and dificult and pipo)
// Ordena amb el nou ordre de l'activitat

### Explorer
```python
# Forever method
def on_forever():
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) <= turn_distance:
        cuteBot.move_time(cuteBot.Direction.RIGHT, turn_perc, turn_time)
    else:
        cuteBot.motors(50, 45)

# Main
turn_distance = 17
basic.forever(on_forever)
turn_perc = 50
turn_time = 0.2
```

## AIR Sensor
### Lane Detecion
Easiest:

```python
# Forever method
def on_forever():
    cuteBot.motors(50, 45)
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        basic.show_icon(IconNames.HAPPY)
    else:
        music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_icon(IconNames.SAD)
# Main
basic.forever(on_forever)
```

Changing tone by side:
```python
# Forever method
def on_forever():
    cuteBot.motors(50, 45)
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        basic.show_icon(IconNames.HAPPY)
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_icon(IconNames.CONFUSED)
    else:
        music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_icon(IconNames.SAD)
# Main
basic.forever(on_forever)
```

### Force Lane
With music:
```python
# Forever method for movement
def on_forever():
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        cuteBot.motors(forward_left_speed, forward_right_speed)
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        cuteBot.motors(low_speed_turn, high_speed_turn)
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        cuteBot.motors(high_speed_turn, low_speed_turn)
    else:
        cuteBot.stopcar()
        cuteBot.move_time(cuteBot.Direction.BACKWARD, backward_speed, backward_seconds)

# Forever method for sounds
def on_forever2():
    music.play(music.built_in_playable_melody(Melodies.PRELUDE),
        music.PlaybackMode.UNTIL_DONE)

# Main
high_speed_turn = 60
low_speed_turn = 10
forward_left_speed = 50
forward_right_speed = 47
backward_speed = 40
backward_seconds = 0.2

basic.forever(on_forever)
basic.forever(on_forever2)
```

Stop when object and cry:
```python
# Forever method for movement and sound
def on_forever():
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < stop_distance:
        cuteBot.stopcar()
        music.stop_all_sounds()
        music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
            cuteBot.motors(forward_left_speed, forward_right_speed)
        elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
            cuteBot.motors(low_speed_turn, high_speed_turn)
        elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
            cuteBot.motors(high_speed_turn, low_speed_turn)
        else:
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

basic.forever(on_forever)
```

Stop when object and turn:
```python
# Forever method for movement and sound
def on_forever():
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < stop_distance:
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
```

Stop when object, cry 10 clocks and if nothing happens turn:
```python
# Forever method for movement and sound
def on_forever():
    global repeat
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < stop_distance:
        if repeat < 10:
            cuteBot.stopcar()
            music.stop_all_sounds()
            music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            repeat = repeat + 1
        else:
            cuteBot.move_time(cuteBot.Direction.RIGHT, turn_perc, turn_time)
            repeat = 0
    else:
        if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
            cuteBot.motors(forward_left_speed, forward_right_speed)
        elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
            cuteBot.motors(low_speed_turn, high_speed_turn)
        elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
            cuteBot.motors(high_speed_turn, low_speed_turn)
        else:
            cuteBot.stopcar()
            cuteBot.move_time(cuteBot.Direction.BACKWARD, backward_speed, backward_seconds)
        repeat = 0

# Main
stop_distance = 10
high_speed_turn = 60
low_speed_turn = 10
forward_left_speed = 50
forward_right_speed = 47
backward_speed = 40
backward_seconds = 0.2
repeat = 0
turn_perc = 60
turn_time = 0.3

basic.forever(on_forever)
```

## States Machine (Controller)

> ⚠️ **WARNING:** On micro:bit, using multiple `forever` loops at the same time can be dangerous because:
>
> * They run independently.
> * Their execution timing is unpredictable.
> * The program state can change in the middle of an action.
>
> Since variables are not locked, you cannot guarantee the order in which actions are processed.
> It is therefore better to put everything in a single `forever` loop, or keep only non-critical and secondary tasks in additional loops where delayed execution does not matter.

```python
#########################################################################
# DANGEROUS --> Variables collision
#########################################################################
# Forever controller
def on_forever_controller():
    global status
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < stop_distance:
        status = 1
    elif cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        status = 2
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        status = 3
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        status = 4
    else:
        status = 5

# Forever method for movement
def on_forever_movement():
    if status == 1:
        cuteBot.stopcar()
    elif status == 2:
        cuteBot.motors(forward_left_speed, forward_right_speed)
    elif status == 3:
        cuteBot.motors(low_speed_turn, high_speed_turn)
    elif status == 4:
        cuteBot.motors(high_speed_turn, low_speed_turn)
    else:
        cuteBot.stopcar()
        cuteBot.move_time(cuteBot.Direction.BACKWARD, backward_speed, backward_seconds)

...
#########################################################################
# / DANGEROUS --> Variables collision
#########################################################################
#########################################################################
# BEST APPROACH
#########################################################################
# States machine and fuctions on same forever
def on_forever():
    global status, playing

    # --- CONTROLLER ---
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < stop_distance:
        status = 0
    elif cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        status = 1
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        status = 2
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        status = 3
    else:
        status = 4

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
happy = True
status = 1

basic.forever(on_forever)
basic.forever(on_forever_faces)
#########################################################################
# / BEST APPROACH
#########################################################################
```

## Final Boss

Follow lines and when encounters an objects, cry for 10 seconds, if the object is removed it continues, if not it turns.
Playing music at the same time and showing faces:

1. With States machine (more efficient in understanding)

```python
def on_forever():
    global status, playing, repeat

    # --- CONTROLLER ---
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < stop_distance:
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
```

2. Spaguetti Code (more efficient in terms of CPU):

```python
# Forever method for movement and sound
def on_forever():
    global repeat, playing, happy
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < stop_distance:
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
```

> Open this page at [https://titocampis.github.io/smart_cutebot_car_technology/](https://titocampis.github.io/smart_cutebot_car_technology/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/titocampis/smart_cutebot_car_technology** and import

## Edit this project

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/titocampis/smart_cutebot_car_technology** and click import
