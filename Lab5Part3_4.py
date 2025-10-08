import RPi.GPIO as GPIO
import math
import time

GPIO.setmode(GPIO.BCM)

# output(s)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


phi_sign = 1
def phi_check(channel):
    global phi_sign
    phi_sign *= -1

GPIO.add_event_detect(4, GPIO.RISING, callback=phi_check, bouncetime=200)

# variables
f = 0.2
phi = math.pi/11
BF = 500
t_initial = time.time()
pwm1 = GPIO.PWM(17, BF)
pwm2 = GPIO.PWM(27, BF)
pwm3 = GPIO.PWM(22,BF)
pwm4 = GPIO.PWM(23, BF)
pwm5 = GPIO.PWM(24, BF)
pwm6 = GPIO.PWM(25,BF)
pwm7 = GPIO.PWM(16, BF)
pwm8 = GPIO.PWM(20, BF)
pwm9 = GPIO.PWM(21,BF)
pwm10 = GPIO.PWM(26, BF)

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)
pwm5.start(0)
pwm6.start(0)
pwm7.start(0)
pwm8.start(0)
pwm9.start(0)
pwm10.start(0)

# try-catch statement
try:

	while True:
		t_actual = time.time() - t_initial
		phi_use = phi * phi_sign


		# Pin 1 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual)**2)
		duty_cycle = B * 100.0

		# Pin 2 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual - phi_use)**2)
		duty_cycle2 = B * 100.0

		# Pin 3 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual - 2*phi_use)**2)
		duty_cycle3 = B * 100.0

		# Pin 4 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual - 3*phi_use)**2)
		duty_cycle4 = B * 100.0

		# Pin 5 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual - 4*phi_use)**2)
		duty_cycle5 = B * 100.0

		# Pin 6 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual - 5*phi_use)**2)
		duty_cycle6 = B * 100.0

		# Pin 7 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual - 6*phi_use)**2)
		duty_cycle7 = B * 100.0

		# Pin 8 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual - 7*phi_use)**2)
		duty_cycle8 = B * 100.0

		# Pin 9 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual - 8*phi_use)**2)
		duty_cycle9 = B * 100.0

		# Pin 10 duty cycle changing
		B = (math.sin(2 * math.pi * f * t_actual - 9*phi_use)**2)
		duty_cycle10 = B * 100.0



		pwm1.ChangeDutyCycle(duty_cycle)
		pwm2.ChangeDutyCycle(duty_cycle2)
		pwm3.ChangeDutyCycle(duty_cycle3)
		pwm4.ChangeDutyCycle(duty_cycle4)
		pwm5.ChangeDutyCycle(duty_cycle5)
		pwm6.ChangeDutyCycle(duty_cycle6)
		pwm7.ChangeDutyCycle(duty_cycle7)
		pwm8.ChangeDutyCycle(duty_cycle8)
		pwm9.ChangeDutyCycle(duty_cycle9)
		pwm10.ChangeDutyCycle(duty_cycle10)


except KeyboardInterrupt:
	pass
finally:
	GPIO.remove_event_detect(4)
	pwm1.stop()
	pwm2.stop()
	pwm3.stop()
	pwm4.stop()
	pwm5.stop()
	pwm6.stop()
	pwm7.stop()
	pwm8.stop()
	pwm9.stop()
	pwm10.stop()
	GPIO.cleanup()
