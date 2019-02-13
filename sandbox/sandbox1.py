def m1_line_follow(self):
    error = 7  # adjust to make the run smoother
    speed = 50  # add an entry for this
    sleep_time = 0.2  # adjust to make robot turn longer
    original = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
    while True:
        current = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
        if original - error < current < original + error:
            self.robot.drive_system.go(speed, speed)
        else:
            self.robot.drive_system.left_motor.turn_on(50)
            self.robot.drive_system.right_motor.turn_on(-50)
            time.sleep(0.2)
            left_value = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
            self.robot.drive_system.right_motor.turn_on(50)
            self.robot.drive_system.left_motor.turn_on(-50)
            time.sleep(0.2)
            right_value = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
            self.robot.drive_system.go(50, 50)
            if original - error < left_value < original + error:
                self.robot.drive_system.left_motor.turn_on(50)
                self.robot.drive_system.right_motor.turn_on(-50)
                time.sleep(sleep_time)
            if original - error < right_value < original + error:
                self.robot.drive_system.right_motor.turn_on(50)
                self.robot.drive_system.left_motor.turn_on(-50)
                time.sleep(sleep_time)
        #     if time.time() - prev_time > 0.25:
        #         self.robot.drive_system.left_motor.turn_on(-50)
        #         self.robot.drive_system.right_motor.turn_on(50)


