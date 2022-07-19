# motion-controlled-relays
this is a project , where We can understand , how to implement a real life solution on motion detection


# components 

- Rasberry pi 3b (minimum version)
- thonny editor with python 3 
- pir sensor (HC SR 501)
- 2 single channel relay in order to work with big electricals

# working principle 

its generally detects the motion , with in the range 3cm - 7meters , and we can configure the sensor whether we to get output when it detects the motion or need the output when the motion stops , since the output we get will be digital , the program wont take much space 

### in order to work , connect BULB  PIN To GPIO 17 , FAN_PIN to GPIO 22 And connect pir sensor to GPIO 26

# PIN connnections
- BULB PIN  connects with  one of the relay In pin 
- THE FAN PIN connects with other single channel relay In pin
