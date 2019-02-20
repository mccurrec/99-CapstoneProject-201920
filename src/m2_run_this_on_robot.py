"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Loki Strain.
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
    #run_test_arm()
    real_thing()

def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.calibrate_arm()
    robot.arm_and_claw.move_arm_to_position(2556)
    robot.arm_and_claw.move_arm_to_position(1500)
    robot.arm_and_claw.move_arm_to_position(4000)
    robot.arm_and_claw.move_arm_to_position(0)
    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.lower_arm()

def real_thing():
    robot = rosebot.RoseBot()
    robot_receiver = rec.Receiver(robot)
    mqtt_robot = com.MqttClient(robot_receiver)

    mqtt_robot.connect_to_pc()


    while True:
        time.sleep(0.01)
        if robot_receiver.is_time_to_stop:
            break






# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()