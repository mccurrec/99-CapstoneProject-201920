def m1_line_follow(self):
    error = 7   # adjust to make the run smoother
    speed = 50  # add an entry for this
    original = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
    while True:
        self.robot.drive_system.go(speed, speed)
        time.sleep(0.2)
        current = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
        while original - error < current < original + error:
            current = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
            if original - error >= current or current >= original + error:
                break
        self.robot.drive_system.left_motor.turn_on(-50)
        self.robot.drive_system.right_motor.turn_on(50)
        time.sleep(0.05)
        left_value = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
        while original - error < left_value < original + error:
            left_value = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
            if original - error >= left_value or left_value >= original + error:
                break
        self.robot.drive_system.right_motor.turn_on(-50)
        self.robot.drive_system.left_motor.turn_on(50)
        time.sleep(0.05)
        right_value = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
        while original - error < right_value < original + error:
            right_value = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
            if original - error >= right_value or right_value >= original + error:
                break
