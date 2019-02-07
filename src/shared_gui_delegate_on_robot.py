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

    def raise_arm(self):
        print('Got raise_arm')
        self.robot.arm_and_claw.raise_arm()
