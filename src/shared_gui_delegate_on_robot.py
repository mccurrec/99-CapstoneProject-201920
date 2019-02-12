"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Loki Strain, Ezrie McCurry, Jack Franey.
  Winter term, 2018-2019.
"""


class Receiver(object):

    def __init__(self, robot):
        """:type  robot: rosebot.RoseBot"""
        self.robot = robot
        self.is_time_to_stop = False

    ###############################################################################
    # Drive System Methods
    ###############################################################################
    def forward(self, lws, rws):
        print('Got forward ', lws, rws)
        self.robot.drive_system.go(int(lws), int(rws))

    def backward(self, lws, rws):
        print('Got backward', lws, rws)
        self.robot.drive_system.go(- int(lws), - int(rws))

    def stop(self):
        print('Got stop')
        self.robot.drive_system.stop()

    def go_straight_for_seconds(self, seconds, speed):
        print('Got go_straight_for_seconds', int(seconds), int(speed))
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        print('Got go_straight_for_inches_using_encoder', int(inches), int(speed))
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    def inches_using_time(self, inches_using_time_entry, left_entry_box):
        print('Moving ', int(inches_using_time_entry), " inches")
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches_using_time_entry), int(left_entry_box))

    def left(self, lws, rws):
        print('Got left', int(lws), int(rws))
        self.robot.drive_system.go(int(lws), int(rws))

    def right(self, lws, rws):
        print('Got right', int(lws), int(rws))
        self.robot.drive_system.go(int(lws), int(rws))

    def go_straight_until_intensity_is_less_than(self, intensity_entry, speed_entry):
        print('Got go_straight_until_intensity_is_less_than', intensity_entry)
        self.robot.drive_system.go_straight_until_intensity_is_less_than(float(intensity_entry), int(speed_entry))

    def go_straight_until_intensity_is_greater_than(self, intensity_entry, speed_entry):
        print('Got go_straight_until_intensity_is_greater_than', intensity_entry)
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(float(intensity_entry), int(speed_entry))

    def go_straight_until_color_is(self, color_entry, speed_entry):
        print('Got go_straight_until_color_is', color_entry)
        self.robot.drive_system.go_straight_until_color_is(color_entry, int(speed_entry))

    def go_straight_until_color_is_not(self, color_entry, speed_entry):
        print('Got go_straight_until_color_is_not', color_entry)
        self.robot.drive_system.go_straight_until_color_is_not(color_entry, int(speed_entry))

    def display_camera_data(self):
        print("Got display_camera_data")
        self.robot.drive_system.display_camera_data()

    def spin_clockwise_until_sees_object(self,speed_entry,area_entry):
        print("Got spin_clockwise_until_sees_object, Speed: {}, Area: {}".format(int(speed_entry),int(area_entry)))
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed_entry), int(area_entry))

    def spin_counterclockwise_until_sees_object(self, speed_entry, area_entry):
        print("Got spin_counterclockwise_until_sees_object, Speed: {}, Area: {}".format(int(speed_entry), int(area_entry)))
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed_entry), int(area_entry))

    def forward_until(self, distance_entry, speed_entry):
        print("got it")
        self.robot.drive_system.go_forward_until_distance_is_less_than(float(distance_entry), int(speed_entry))

    def backward_until(self, distance_entry, speed_entry):
        print("got it")
        self.robot.drive_system.go_backward_until_distance_is_greater_than(float(distance_entry), int(speed_entry))

    def within(self, distance_entry, speed_entry, delta_entry):
        print('got it')
        self.robot.drive_system.go_until_distance_is_within(distance_entry,speed_entry,distance_entry)

    ###############################################################################
    # Arm and Claw Methods
    ###############################################################################
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
        self.robot.arm_and_claw.move_arm_to_position(int(arm_position_entry))

    ###############################################################################
    # Sound Methods
    ###############################################################################
    def beep(self, times):
        print('I will beep {} times'.format(times))
        for _ in range(int(times)):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, frequency_entry, duration_entry):
        print("Playing tone at ", frequency_entry, " for ", duration_entry)
        # self.robot.sound_system.tone(frequency_entry, duration_entry)
        self.robot.sound_system.tone_maker.play_tone(int(frequency_entry), int(duration_entry)).wait()

    def speak_phrase(self, phrase):
        print("Speaking phrase:", str(phrase))
        self.robot.sound_system.speech_maker.speak(str(phrase)).wait()

    ###############################################################################
    # Controls Methods
    ###############################################################################
    def quit(self):
        print('got quit')
        self.is_time_to_stop = True

    def exit(self):
        print('got exit')

    ###############################################################################
    # Methods for Sprint 2
    ###############################################################################

    def m2(self, freq, iteration):

        self.robot.drive_system.go(100, 100)
        self.robot.drive_system.left_motor.reset_position()
        start = self.robot.drive_system.left_motor.get_position()

        while True:
            if self.robot.drive_system.left_motor.get_position() - start >= 90:
                self.robot.sound_system.tone_maker.play_tone(freq, 500)
                freq = int(freq) + int(iteration)
                start = self.robot.drive_system.left_motor.get_position()

            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
                #if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 0.25:
                    #if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 0.25:

                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()

                break





