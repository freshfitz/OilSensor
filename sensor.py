#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import json
try:
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 7
      PIN_ECHO = 11
    
      #Distance from sensor to top of fluid this will calculate the 100% and gallons when full
      SenDisMin = 7.87
      #Distance from sensor to bottom of tank or fluid level when empty, this will calculate the 0% and galllons left when empty
      SenDisMax = 37.63
      #Tank siz in US gallons
      TankSize = 250

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print "Waiting for sensor to settle"

      time.sleep(2)

      print "Calculating distance"
      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      pulse_duration = pulse_end_time - pulse_start_time
      
      #get distance in cm
      distanceCM = round(pulse_duration * 17150, 2)

      #get distance in inches
      distanceIN = round(pulse_duration * 17150, 2)/2.54

      #((input - max) * 100) / (min - max) get % from distance

      # Calculate percentage by getting liquid distance from sensor full and empty
      percentagecalc = ((distanceIN - SenDisMax) * 100) / (SenDisMin - SenDisMax)

      #Calculate gallons based off of size of tank in gals
      gals = ((distanceIN - SenDisMax) * TankSize) / (SenDisMin - SenDisMax)

      data = {}
      data['in'] = distanceIN
      data['name'] = "OilSensor"
      data['cm'] = distanceCM
      data['gals'] = gals
      data['percentage'] = percentagecalc
      with open('/var/www/html/index.php', 'w') as outfile:
          json.dump(data,outfile)

      print "Distance:",distanceCM,"cm"
      print "Distance:",distanceIN,"in"
      print "Gallons:",gals, "US"
      print "Percentage:",percentagecalc,"%"


finally:
      GPIO.cleanup()
