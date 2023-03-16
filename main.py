def clignote_droite():
    droite.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(100)
    droite.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.pause(100)
def clignote_gauche():
    gauche.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(100)
    gauche.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.pause(100)

def on_button_pressed_a():
    for index in range(11):
        clignote_gauche()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    stop.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(500)
    strip.clear()
    strip.show()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index2 in range(11):
        clignote_droite()
input.on_button_pressed(Button.B, on_button_pressed_b)

droite: neopixel.Strip = None
stop: neopixel.Strip = None
gauche: neopixel.Strip = None
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
gauche = strip.range(0, 2)
stop = strip.range(0, 5)
droite = strip.range(3, 2)

def on_forever():
    pass
basic.forever(on_forever)
