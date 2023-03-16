input.onSound(DetectedSound.Loud, function () {
    clignote_gauche()
})
function clignote_droite () {
    droite.showColor(neopixel.colors(NeoPixelColors.Orange))
    basic.pause(100)
    droite.showColor(neopixel.colors(NeoPixelColors.Black))
    basic.pause(100)
}
function clignote_gauche () {
    gauche.showColor(neopixel.colors(NeoPixelColors.Orange))
    basic.pause(100)
    gauche.showColor(neopixel.colors(NeoPixelColors.Black))
    basic.pause(100)
}
input.onButtonPressed(Button.A, function () {
    for (let index = 0; index <= 10; index++) {
        clignote_gauche()
    }
})
input.onButtonPressed(Button.AB, function () {
    stop.showColor(neopixel.colors(NeoPixelColors.Red))
    basic.pause(500)
    strip.clear()
    strip.show()
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index <= 10; index++) {
        clignote_droite()
    }
})
let droite: neopixel.Strip = null
let stop: neopixel.Strip = null
let gauche: neopixel.Strip = null
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
gauche = strip.range(0, 2)
stop = strip.range(0, 5)
droite = strip.range(3, 2)
basic.forever(function () {
	
})
