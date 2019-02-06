# Engineering 4 Notebook
This is where all of my stuff will go!
## Assignments
### Auto Dice Roll Out
#### Lessons Learned
Basic understanding of python and general problem with code caused by little knowledge of Python
#### Code
https://github.com/sliving03/Engineering_4_Notebook/blob/master/Python/Auto%20Dice%20Roll%20Out.py
### Python Calculator Trial One and Two
#### Lessons Learned
We learned about functions and we also learned how to use said functions to make our code smaller and more usable.
#### Code
https://github.com/sliving03/Engineering_4_Notebook/blob/master/Python/PythonCalcTrial1.py and https://github.com/sliving03/Engineering_4_Notebook/blob/master/Python/PythonCalcTrial2.py
### Python Quadratic Solver
#### Lessons Learned
We learned how to solve and use more complicated math formulas in python.
#### Code
https://github.com/sliving03/Engineering_4_Notebook/blob/master/Python/PythonQuadraticSolver.py
### Hangman
#### Lessons Learned
we gained knowledge about how to do multi line commenting, How to use the time import, how to extend lists and how to create them, and we leaned how to creat our own imports from out files.
#### Code
https://github.com/sliving03/Engineering_4_Notebook/blob/master/Python/Hang%20Man
### GPIO Pins - Python/Bash LED
#### Lessons Learned
We learned how to import the gpio pins, how to wire up an LED to a T Cobbler which is connected to our Raspberry pi, and we finnaly pushed to git hub by ourselves.
#### Code
Bash : https://github.com/sliving03/Engineering_4_Notebook/blob/master/Scripts/helloled.sh 

Python : https://github.com/sliving03/Engineering_4_Notebook/blob/master/Python/pythonhelloled.py

LOL SAM ITS HERE DUMB SANS GEEETTTTTTT DUNKED ON
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 23
Motor2B = 21
Motor2E = 19
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
 
print "Going forwards"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)
 
sleep(2)
 
print "Going backwards"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
 
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)
 
sleep(2)
 
print "Now stop"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
 
GPIO.cleanup()
