def m1_feature_9(self, initial_rate, rate_of_increase):
    # starts the robot at the given speed:
    self.robot.drive_system.go(100, 100)
    # stores the distance to the cube as previous distance:
    previous_distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    # stores the current time as the previous time:
    previous_time = time.time()
    # set the rate between beeps as the initial rate given by the user:
    rate = initial_rate
    # delta is the distance needed to travel for the beeping to increase in speed by the given increment:
    delta = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() / ((
                                                                                             self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() - 0.05) / rate_of_increase)
    # loops until the cube is reached and picked up:
    while True:
        # checks to see if the change in distance to the cube is greater than delta:
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() - previous_distance >= delta:
            # checks to see if enough time has passed from the last beep:
            if time.time() - previous_time >= rate:
                previous_time, rate = self.m1_feature_9_beep_and_time_faster(rate, rate_of_increase)
        # checks to see if the change in distance to the cube is less than negative delta:
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() - previous_distance <= - delta:
            # checks to see if enough time has passed from the last beep:
            if time.time() - previous_time >= rate:
                previous_time, rate = self.m1_feature_9_beep_and_time_slower(rate, rate_of_increase)
        # stops the robot once it is within 1 inch of the cube, and picks it up:
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1.5:
            self.robot.drive_system.stop()
            self.robot.arm_and_claw.raise_arm()
            break
        previous_distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()


def m1_feature_9_beep_and_time_faster(self, rate, rate_of_increase):
    self.robot.sound_system.beeper.beep()
    # the time from last beep is reset:
    return time.time(), rate - rate_of_increase


def m1_feature_9_beep_and_time_slower(self, rate, rate_of_increase):
    self.robot.sound_system.beeper.beep()
    # the time from last beep is reset:
    return time.time(), rate + rate_of_increase
