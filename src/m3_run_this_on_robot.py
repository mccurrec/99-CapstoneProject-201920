"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jack Franey.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_thing()


def real_thing():
    robot = rosebot.RoseBot()
    receiver = rec.Receiver(robot)
    mqtt_receiver = com.MqttClient(receiver)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(.01) #wait 1/100 to let the "background loop" see if anything gets sent
        if receiver.is_time_to_stop() == True:
            break

# class Receiver(object):
#     def __init__(self, robot):
#         """:type robot: rosebot.RoseBot """
#         self.robot = robot
#
#     def forward(self,  left_wheel_speed, right_wheel_speed):
#         print("Got forward", left_wheel_speed, right_wheel_speed)
#         self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()