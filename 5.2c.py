from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)
red_led = LED(7)
green_led = LED(15)
blue_led = LED(11)

window = Tk()
window.title("LED Toggler")
normalFont = tkinter.font.Font(size=14, weight="bold")


def Toggle_red():
    if red_led.is_lit:
        red_led.off()
        redButton["text"] = "Turn on Red LED"
    else:
        red_led.on()
        blue_led.off()
        blueButton["text"] = "Blue LED"
        green_led.off()
        greenButton["text"] = "Green LED"
        redButton["text"] = "Turn off"


def Toggle_green():
    if green_led.is_lit:
        green_led.off()
        greenButton["text"] = "Turn on Green LED"
    else:
        green_led.on()
        greenButton["text"] = "Turn off"
        blue_led.off()
        red_led.off()
        blueButton["text"] = "Blue LED"
        redButton["text"] = "Red LED"


def Toggle_blue():
    if blue_led.is_lit:
        blue_led.off()
        blueButton["text"] = "Blue LED"
    else:
        blue_led.on()
        green_led.off()
        greenButton["text"] = "Green LED"
        red_led.off()
        redButton["text"] = "Red LED"
        blueButton["text"] = "Turn off"


def close():
    RPi.GPIO.cleanup()
    window.destroy()


redButton = Button(window, font=normalFont, command=Toggle_red, text='red led', bg='red', height=1, width=20)
redButton.grid(row=0, column=0)

greenButton = Button(window, text='Turn on Green LED', font=normalFont, command=Toggle_green, bg='green', height=1,
                     width=24)
greenButton.grid(row=1, column=0)

blueButton = Button(window, text='Turn on Blue LED', font=normalFont, command=Toggle_blue, bg='blue', height=1,
                    width=24)
blueButton.grid(row=2, column=0)

exitButton = Button(window, text='Exit', font=normalFont, command=close, bg='bisque2', height=1, width=24)
exitButton.grid(row=3, column=0)

window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()