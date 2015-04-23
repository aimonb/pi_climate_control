import pprint
import time
import yaml
from AdafruitDHT import AdafruitDHT
import Adafruit_DHT
import datetime
import curses
import signal
import sys
from decimal import *


# TBD: Get these from yaml
desired_hum = 45
desired_temp = 24.5

# Handle Ctrl-C etc
def signal_handler(signal, frame):
	exit_clean()
signal.signal(signal.SIGINT, signal_handler)

# Clean up and release screen
def exit_clean():	
	# Release terminal
        curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
	sys.exit(1)

# Turn fogger relay on
def fogger_on(on):
	if on is True:
		# Fogger on
		pass
	else:
		# Foger off
		pass
	return

# Turn Heater relay on
def heater_on(on):
	if on is True:
		# Heater on
		pass
	else:
		# Heater off
		pass
	return

# Trigger some relay
def relay_on(pin):
	pass

# instantiate HM2302 sensor 
o =  AdafruitDHT()

# Initialize Screen
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(False)


# Main loop to check temp and Humidity
while True:
	# Get data
	temp, hum = o.get_reading(Adafruit_DHT.AM2302, 4)
	temp = float("{0:.2f}".format(temp))
	ftemp = float("{0:.2f}".format((temp*9/5+32)))
	hum = float("{0:.2f}".format(hum))
	stdscr.addstr(1, 1, "Relative Humidity: %s%%\n" % hum)
	stdscr.addstr(2, 1, "Current Temperature: %s*C | %s*F\n" % (temp, ftemp))
	# Turn on fogger if needed
	if hum < desired_hum:
		now_time = datetime.datetime.now()
		# switch the relay on
        	fogger_on(True)
		stdscr.addstr(3, 1, "Fogger Status: On \n")
		stdscr.refresh()
		time.sleep(1)
	else:
		# switch the relay off
        	fogger_on(False)
        	stdscr.addstr(3, 1, "Fogger Status: Off \n")
		stdscr.refresh()
	# Turn on Heater if needed
	if temp < desired_temp:
		now_time = datetime.datetime.now()
		# switch the relay on
        	heater_on(True)
		stdscr.addstr(4, 1, "Heater Status: On \n")
		stdscr.refresh()
		time.sleep(1)
	else:
		# switch the relay off
        	heater_on(False)
        	stdscr.addstr(4, 1, "Heater Status: Off \n")
		stdscr.refresh()
	time.sleep(1)


# Release terminal
exit_clean()

