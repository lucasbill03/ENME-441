import RPi.GPIO as GPIO
import time
import random
from Lab6Shifter import Shifter

class Bug:
    def __init__(self, timestep=0.1, x=3, isWrapOn=False):
        self.timestep = timestep
        self.x = x
        self.isWrapOn = isWrapOn
        self.__running = False
        self.__shifter = Shifter(serialPin=23, clockPin=25, latchPin=24)

    def __display(self):
        pattern = 1 << self.x
        self.__shifter.shiftByte(pattern)

    def start(self):
        self.__running = True
        try:
            while self.__running:
                self.__display()
                self.x += random.choice([-1, 1])
                if self.isWrapOn:
                    self.x %= 8
                else:
                    if self.x < 0: self.x = 0
                    if self.x > 7: self.x = 7
                time.sleep(self.timestep)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.__running = False
        self.__shifter.shiftByte(0)
        GPIO.cleanup()


if __name__ == "__main__":
    s1 = 17
    s2 = 27
    s3 = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(s3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    bug = Bug()
    prev_s2 = False

    try:
        while True:
            if GPIO.input(s1):
                bug.start()
            else:
                bug.stop()
            s2_state = GPIO.input(s2)
            if s2_state and not prev_s2:
                bug.isWrapOn = not bug.isWrapOn
            prev_s2 = s2_state

            # adjust speed
            if GPIO.input(s3):
                bug.timestep = 0.03
            else:
                bug.timestep = 0.1

            time.sleep(0.05)

    finally:
        GPIO.cleanup()