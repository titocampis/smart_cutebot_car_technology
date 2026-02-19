# Vehicles Automation Activity
## Lights
### Automatic headlights
```python
# Forever method
def on_forever():
    if input.light_level() >= 16:
        cuteBot.color_light(cuteBot.RGBLights.ALL, 0x000000)
    else:
        cuteBot.color_light(cuteBot.RGBLights.ALL, 0xffffff)

# Main
basic.forever(on_forever)
```

## Ultrasound Sensor
### Park helper
```python
# Forever method
def on_forever():
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) <= 5:
        music.stop_all_sounds()
        music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    elif cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) <= 12:
        music.stop_all_sounds()
        music.play(music.tone_playable(523, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    elif cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) <= 20:
        music.stop_all_sounds()
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        music.stop_all_sounds()

# Main
basic.forever(on_forever)
```

### Remaining
// Copy from MSI python codes for intermitents (easy and dificult and pipo)
// Ordena amb el nou ordre de l'activitat

### Explorer
```python
# Forever method
def on_forever():
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) <= 17:
        cuteBot.move_time(cuteBot.Direction.RIGHT, 50, 0.2)
    else:
        cuteBot.motors(50, 45)

# Main
basic.forever(on_forever)
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
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < 20:
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
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < 20:
        cuteBot.stopcar()
        basic.pause(500)
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
high_speed_turn = 60
low_speed_turn = 10
forward_left_speed = 50
forward_right_speed = 47
backward_speed = 40
backward_seconds = 0.2
turn_perc = 60
turn_time = 0.3

basic.forever(on_forever)
```

Stop when object, cry 10 clocks and if nothing happens turn:
```python
# Forever method for movement and sound
def on_forever():
    global repeat
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < 20:
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
        repeat = 0
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
high_speed_turn = 60
low_speed_turn = 10
forward_left_speed = 50
forward_right_speed = 47
backward_speed = 40
backward_seconds = 0.2
status = 2
playing = 0
repeat = 0
turn_perc = 60
turn_time = 0.3

basic.forever(on_forever)
```

Music, stop when object and cry (with controller):
> :warning: **WARNING:** Controllers can be very dangerous because the variables are not locked and you don't know in which order the acitons are processed.
> And with a lot of actions can be a mess. Like here if we want to implement the status, it can modify the repeat and set another status and be different for movement and sound forevers.
> Better everything in one forever

```python
#########################################################################
# DANGEROUS --> Wrong Performance
#########################################################################
# Forever controller
def on_forever_controller():
    global status
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < 20:
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

# Forever method for sound
def on_forever_sound():
    global playing
    if status == 1:
        music.stop_all_sounds()
        basic.pause(100)
        music.play(music.tone_playable(831, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        playing = 0
    elif playing == 0:
        music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        playing = 1

# Main
high_speed_turn = 60
low_speed_turn = 10
forward_left_speed = 50
forward_right_speed = 47
backward_speed = 40
backward_seconds = 0.2
status = 2
playing = 0

basic.forever(on_forever_controller)
basic.forever(on_forever_movement)
basic.forever(on_forever_sound)
#########################################################################
# DANGEROUS --> Wrong Performance
#########################################################################
```

Final boss: follow lines and when encounters an objects, cry for 10 seconds, if the object is removed it continues, if not it turns.
Playing music at the same time:

```python
# Forever method for everything
def on_forever():
    global repeat
    global playing
    if cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS) < 20:
        if repeat < 10:
            cuteBot.stopcar()
            music.stop_all_sounds()
            music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            repeat = repeat + 1
            playing= 0
        else:
            cuteBot.move_time(cuteBot.Direction.RIGHT, turn_perc, turn_time)
            repeat = 0
    else:
        repeat = 0
        if playing == 0:
            music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
                music.PlaybackMode.LOOPING_IN_BACKGROUND)
            playing = 1
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
high_speed_turn = 60
low_speed_turn = 10
forward_left_speed = 50
forward_right_speed = 47
backward_speed = 40
backward_seconds = 0.2
status = 2
turn_perc = 60
turn_time = 0.3
repeat = 0
playing = 0

basic.forever(on_forever)
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

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
