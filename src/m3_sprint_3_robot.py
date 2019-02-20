import mqtt_remote_method_calls as com
import time

def forward_press(base_speed,robot):
    robot.drivesystem.go(base_speed,base_speed)

def backward_press(base_speed,robot):
    robot.drivesystem.go(-base_speed,-base_speed)

def left_press(base_speed,robot):
    robot.drivesystem.go(-base_speed,base_speed)

def right_press(base_speed,robot):
    robot.drivesystem.go(base_speed,-base_speed)

def auto_race_lightning(base_speed,robot):
    racing_speed = base_speed + 100
    turn_speed = base_speed
    item_speed = racing_speed
    stop = 5
    robot.drivesystem.go(racing_speed)
    robot.sensor_system.color_sensor.mode = 'COL-COLOR'
    while True:
        if robot.sensor_system.color_sensor.get_color_as_name() == 'red':
            robot.drivesystem.go(item_speed-100)
            time.sleep(4)
        if robot.sensor_system.color_sensor.get_color_as_name() == 'green':
            robot.drivesystem.go(item_speed+100)
            time.sleep(4)
        if robot.sensor_system.color_sensor.get_color_as_name() == 'yellow':
            robot.drivesystem.left_motor.turn_on(item_speed)
            robot.drivesystem.right_motor.turn_on(-item_speed)
        if robot.sensor_system.color_sensor.get_color_as_name() == 'blue':
            turns(robot,stop)

# def auto_race_sally(base_speed,robot):
#
# def auto_race_doc(base_speed,robot):

def turns(robot,stop):
    white = 94
    black = 23
    k = 0.6
    c = 7
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        print(c * (white - current) + c, k * (current - black) + c)
        robot.drive_system.go(k * (white - current) + c, k * (current - black) + c)
        print(robot.sensor_system.color_sensor.get_color_as_name())
        if robot.sensor_system.color_sensor.get_color() == stop:
            time.sleep(0.1)
            if robot.sensor_system.color_sensor.get_color() == stop:
                robot.drive_system.stop()
                break