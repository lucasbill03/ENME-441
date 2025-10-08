import RPi.GPIO as GPIO
import math
import time

GPIO.setmode(GPIO.BCM)

# output(s)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

# variables
f = 0.2
BF = 500
t_initial = time.time()
pwm = GPIO.PWM(17, BF)
pwm.start(0)

try:
	while True:
		t_actual = time.time() - t_initial
		B = (math.sin(2 * math.pi * f * t_actual))
		duty_cycle = B * 100
		pwm.ChangeDutyCycle(duty_cycle)

except KeyboardInterrupt:
	pass
finally:
	pwm.stop()
	GPIO.cleanup()


