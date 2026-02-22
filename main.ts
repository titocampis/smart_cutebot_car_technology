//  # --- Faces (LEDs screen) --- CANNOT GO HERE OVERLOAD AND FAIL
//  --> Needs to go into another forever
//  if status == 0:
//      basic.show_icon(IconNames.SAD)
//  else:
//      basic.show_icon(IconNames.HAPPY)
//  Foreer faces to avoid overload
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
let repeat = 0
let playing = false
let status = 1
basic.forever(function on_forever() {
    
    //  --- CONTROLLER ---
    let distance = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
    if (distance < stop_distance) {
        if (repeat < 10) {
            status = 0
            repeat = repeat + 1
        } else {
            status = 5
            repeat = 0
        }
        
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_R_line)) {
        status = 1
        repeat = 0
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_line_R_unline)) {
        status = 2
        repeat = 0
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_unline_R_line)) {
        status = 3
        repeat = 0
    } else {
        status = 4
        repeat = 0
    }
    
    //  --- ACT (movement) ---
    if (status == 0) {
        cuteBot.stopcar()
    } else if (status == 1) {
        cuteBot.motors(forward_left_speed, forward_right_speed)
    } else if (status == 2) {
        cuteBot.motors(low_speed_turn, high_speed_turn)
    } else if (status == 3) {
        cuteBot.motors(high_speed_turn, low_speed_turn)
    } else if (status == 4) {
        cuteBot.moveTime(cuteBot.Direction.backward, backward_speed, backward_seconds)
    } else if (status == 5) {
        cuteBot.moveTime(cuteBot.Direction.right, turn_perc, turn_time)
    }
    
    //  --- ACT (sound) ---
    if (status == 0) {
        music.stopAllSounds()
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        playing = false
    } else if (!playing) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Prelude), music.PlaybackMode.LoopingInBackground)
        playing = true
    }
    
})
basic.forever(function on_forever_faces() {
    if (status == 0) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    
})
