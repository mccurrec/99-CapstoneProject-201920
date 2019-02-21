"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Ezrie McCurry.
  Winter term, 2018-2019.
"""

import rosebot
import m1_sprint3
import mqtt_remote_method_calls as com
import time
import m1_gui_delegate_on_robot as rec


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    demonstration()


def demonstration():
    robot = rosebot.RoseBot()
    receiver = rec.Receiver(robot)
    mqtt_receiver = com.MqttClient(receiver)
    receiver.mqtt = mqtt_receiver
    mqtt_receiver.connect_to_pc()
    # while True:
    #     previous_progress = receiver.update_progress()
    #     time.sleep(0.01)
    #     if receiver.update_progress() > previous_progress:
    #         mqtt_receiver.send_message('update_progress', [float(receiver.update_progress())])
    while True:
        time.sleep(0.01)
        if receiver.is_time_to_stop:
            break
        if receiver.time_to_sort_packages:
            m1_sprint3.sort_packages(robot, receiver.number_of_packages, mqtt_receiver)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

