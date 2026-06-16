"""Sample Webots controller for the pit escape benchmark."""

from controller import Robot
import numpy as np
robot = Robot()

timestep = int(robot.getBasicTimeStep())

# Max possible speed for the motor of the robot.
maxSpeed = 8.72

# Configuration of the main motor of the robot.
pitchMotor = robot.getDevice("body pitch motor")
pitchMotor.setPosition(float('inf'))
pitchMotor.setVelocity(0.0)
gyro = robot.getDevice("body gyro")
gyro.enable(timestep)

# This is the time interval between direction switches.
# The robot will start by going forward and will go backward after
# this time interval, and so on.
timeInterval = 1.5

# At first we go forward.
pitchMotor.setVelocity(maxSpeed)
forward = True
lastTime = 0
limiar=0.05
values_old=gyro.getValues()
while robot.step(timestep) != -1:
    now = robot.getTime()
    #print(values)
    # We check if enough time has elapsed.
    if now - lastTime > timeInterval:
        # If yes, then we switch directions.
        values_new=gyro.getValues()
        delta =values_new[1]-values_old[1]
        print(delta) 
        if delta>limiar:
            #aceleracao positiva
            pitchMotor.setVelocity(maxSpeed)
        elif delta<-limiar:
            #aceleracao negativa
            pitchMotor.setVelocity(-maxSpeed)
        else:
            #aceleracao proxima de zero
            pitchMotor.setVelocity(0.0)
        lastTime = now
        values_old=gyro.getValues()
    #print(values_old)
