"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Loki Strain, Ezrie McCurry, Jack Franey.
  Winter term, 2018-2019.
"""


class Receiver(object):

    def __init__(self,robot):
        self.robot = robot
        """:type  robot: rosebot.RoseBot"""
    def forward(self, lws, rws):
        print('Got forward ', lws, rws)
        self.robot.drive_system.go(int(lws), int(rws))

    def backward(self, lws, rws):
        print('Got backward', lws, rws)
        self.robot.drive_system.go(int(lws), int(rws))

    def raise_arm(self):
        print('Got raise_arm')
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print('Got lower_arm')
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        print('Got calibrate_arm')
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, arm_position_entry):
        print('Got move_arm_to_position')
        self.robot.arm_and_claw.move_arm_to_position(arm_position_entry)

