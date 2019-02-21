import mqtt_remote_method_calls as com
import time

def forward_press(base_speed,robot):
    robot.drive_system.go(base_speed,base_speed)

def backward_press(base_speed,robot):
    robot.drive_system.go(-base_speed,-base_speed)

def left_press(base_speed,robot):
    robot.drive_system.go(-base_speed,base_speed)

def right_press(base_speed,robot):
    robot.drive_system.go(base_speed,-base_speed)

def auto_race_lightning(base_speed,robot):
    racing_speed = int(base_speed) + 20
    turn_speed = int(base_speed)
    item_speed = int(racing_speed)
    robot.drive_system.go(racing_speed,racing_speed)
    robot.sensor_system.color_sensor.mode = 'COL-COLOR'
    while True:
        if robot.sensor_system.color_sensor.get_color() == 5:
            robot.drive_system.go(item_speed-20,item_speed-20)
            time.sleep(.1)
        if robot.sensor_system.color_sensor.get_color() == 3:
            robot.drive_system.go(item_speed+20,item_speed+20)
            time.sleep(.1)
        if robot.sensor_system.color_sensor.get_color() == 2:
            robot.drive_system.left_motor.turn_on(item_speed)
            robot.drive_system.right_motor.turn_on(-item_speed)
            time.sleep(4.3)
            robot.drive_system.left_motor.turn_off()
            robot.drive_system.right_motor.turn_off()
            robot.drive_system.left_motor.turn_on(racing_speed)
            robot.drive_system.right_motor.turn_on(racing_speed)
        if robot.sensor_system.color_sensor.get_color() == 1:
            robot.drive_system.stop()
            robot.drive_system.go(turn_speed, turn_speed)
            time.sleep(2.8)
            robot.drive_system.left_motor.turn_on(-turn_speed)
            robot.drive_system.right_motor.turn_on(turn_speed)
            time.sleep(1.55)
            robot.drive_system.go(turn_speed, turn_speed)
            time.sleep(4.65)
            robot.drive_system.left_motor.turn_on(-turn_speed)
            robot.drive_system.right_motor.turn_on(turn_speed)
            time.sleep(1.55)
            robot.drive_system.go(turn_speed, turn_speed)            # turns(turn_speed,robot)
            robot.drive_system.go(racing_speed,racing_speed)
        # if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
        #     time.sleep(.01)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
            robot.drive_system.stop()
            avoid_obstacle(turn_speed,robot)
            robot.drive_system.go(racing_speed,racing_speed)
        if robot.sensor_system.color_sensor.get_color() == 7:
            time.sleep(1)
            robot.drive_system.stop()
            celebrate_finish(robot)
            break
    print('Congratulations! You Win!')


def auto_race_sally(base_speed,robot):
    racing_speed = int(base_speed)
    turn_speed = int(base_speed)
    item_speed = int(racing_speed) + 20
    robot.drive_system.go(racing_speed, racing_speed)
    robot.sensor_system.color_sensor.mode = 'COL-COLOR'
    while True:
        if robot.sensor_system.color_sensor.get_color() == 5:
            robot.drive_system.go(item_speed - 20, item_speed - 20)
            time.sleep(.1)
        if robot.sensor_system.color_sensor.get_color() == 3:
            robot.drive_system.go(item_speed + 20, item_speed + 20)
            time.sleep(.1)
        if robot.sensor_system.color_sensor.get_color() == 2:
            robot.drive_system.left_motor.turn_on(item_speed)
            robot.drive_system.right_motor.turn_on(-item_speed)
            time.sleep(4.3)
            robot.drive_system.left_motor.turn_off()
            robot.drive_system.right_motor.turn_off()
            robot.drive_system.left_motor.turn_on(racing_speed)
            robot.drive_system.right_motor.turn_on(racing_speed)
        if robot.sensor_system.color_sensor.get_color() == 1:
            robot.drive_system.stop()
            robot.drive_system.go(turn_speed, turn_speed)
            time.sleep(2.8)
            robot.drive_system.left_motor.turn_on(-turn_speed)
            robot.drive_system.right_motor.turn_on(turn_speed)
            time.sleep(1.55)
            robot.drive_system.go(turn_speed, turn_speed)
            time.sleep(4.65)
            robot.drive_system.left_motor.turn_on(-turn_speed)
            robot.drive_system.right_motor.turn_on(turn_speed)
            time.sleep(1.55)
            robot.drive_system.go(turn_speed, turn_speed)  # turns(turn_speed,robot)
            robot.drive_system.go(racing_speed, racing_speed)
        # if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
        #     time.sleep(.01)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
            robot.drive_system.stop()
            avoid_obstacle(turn_speed, robot)
            robot.drive_system.go(racing_speed, racing_speed)
        if robot.sensor_system.color_sensor.get_color() == 7:
            time.sleep(1)
            robot.drive_system.stop()
            celebrate_finish(robot)
            break
    print('Congratulations! You Win!')

def auto_race_doc(base_speed,robot):
    racing_speed = int(base_speed)
    turn_speed = int(base_speed) + 20
    item_speed = int(racing_speed)
    robot.drive_system.go(racing_speed, racing_speed)
    robot.sensor_system.color_sensor.mode = 'COL-COLOR'
    while True:
        if robot.sensor_system.color_sensor.get_color() == 5:
            robot.drive_system.go(item_speed - 20, item_speed - 20)
            time.sleep(.1)
        if robot.sensor_system.color_sensor.get_color() == 3:
            robot.drive_system.go(item_speed + 20, item_speed + 20)
            time.sleep(.1)
        if robot.sensor_system.color_sensor.get_color() == 2:
            robot.drive_system.left_motor.turn_on(item_speed)
            robot.drive_system.right_motor.turn_on(-item_speed)
            time.sleep(4.3)
            robot.drive_system.left_motor.turn_off()
            robot.drive_system.right_motor.turn_off()
            robot.drive_system.left_motor.turn_on(racing_speed)
            robot.drive_system.right_motor.turn_on(racing_speed)
        if robot.sensor_system.color_sensor.get_color() == 1:
            robot.drive_system.stop()
            robot.drive_system.go(turn_speed, turn_speed)
            time.sleep(2.8)
            robot.drive_system.left_motor.turn_on(-turn_speed)
            robot.drive_system.right_motor.turn_on(turn_speed)
            time.sleep(1.55)
            robot.drive_system.go(turn_speed, turn_speed)
            time.sleep(4.65)
            robot.drive_system.left_motor.turn_on(-turn_speed)
            robot.drive_system.right_motor.turn_on(turn_speed)
            time.sleep(1.55)
            robot.drive_system.go(turn_speed, turn_speed)  # turns(turn_speed,robot)
            robot.drive_system.go(racing_speed, racing_speed)
        # if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
        #     time.sleep(.01)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
            robot.drive_system.stop()
            avoid_obstacle(turn_speed, robot)
            robot.drive_system.go(racing_speed, racing_speed)
        if robot.sensor_system.color_sensor.get_color() == 7:
            time.sleep(1)
            robot.drive_system.stop()
            celebrate_finish(robot)
            break
    print('Congratulations! You Win!')

def force_turn(turn_speed,robot):
    robot.drive_system.stop()
    robot.drive_system.go(turn_speed,turn_speed)
    time.sleep(2.5)
    robot.drive_system.left_motor.turn_on(-turn_speed)
    robot.drive_system.right_motor.turn_on(turn_speed)
    time.sleep(1.4)
    robot.drive_system.go(turn_speed,turn_speed)
    time.sleep(4.7)
    robot.drive_system.left_motor.turn_on(-turn_speed)
    robot.drive_system.right_motor.turn_on(turn_speed)
    time.sleep(1.4)
    robot.drive_system.go(turn_speed,turn_speed)


def turns(turn_speed,robot):
    error = 7  # adjust to make the run smoother
    original = robot.sensor_system.color_sensor.get_reflected_light_intensity()
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        if original - error < current < original + error:
            robot.drive_system.go(turn_speed, turn_speed)
        if current >= original + error or current <= original - error:
            robot.drive_system.left_motor.turn_on(-30)
            robot.drive_system.right_motor.turn_on(30)
        if robot.sensor_system.color_sensor.get_color() == 4:
            robot.drive_system.left_motor.turn_off()
            robot.drive_system.right_motor.turn_off()
            robot.drive_system.left_motor.turn_on(-50)
            robot.drive_system.right_motor.turn_on(50)
            time.sleep(.03)
            robot.drive_system.left_motor.turn_off()
            robot.drive_system.right_motor.turn_off()
            break
        if robot.sensor_system.color_sensor.get_color() == 7:
            break

# def turns(robot):
#     white = 94
#     black = 23
#     k = 0.6
#     c = 7
#     while True:
#         current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
#         print(c * (white - current) + c, k * (current - black) + c)
#         robot.drive_system.go(k * (white - current) + c, k * (current - black) + c)
#         print(robot.sensor_system.color_sensor.get_color_as_name())
#         if robot.sensor_system.color_sensor.get_color() == 2:
#             time.sleep(0.1)
#             if robot.sensor_system.color_sensor.get_color() == 2:
#                 robot.drive_system.stop()
#                 break

def avoid_obstacle(turn_speed,robot):
    robot.drive_system.go(turn_speed,turn_speed)
    if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
        robot.drive_system.stop()
        robot.arm_and_claw.raise_arm()
        robot.drive_system.right_motor.turn_on(turn_speed)
        robot.drive_system.left_motor.turn_on(-turn_speed)
        time.sleep(.8)
        robot.drive_system.stop()
        robot.drive_system.right_motor.turn_on(turn_speed)
        robot.drive_system.left_motor.turn_on(turn_speed)
        time.sleep(.3)
        robot.drive_system.stop()
        robot.arm_and_claw.lower_arm()
        robot.drive_system.right_motor.turn_on(-turn_speed)
        robot.drive_system.left_motor.turn_on(-turn_speed)
        time.sleep(.3)
        robot.drive_system.stop()
        robot.drive_system.right_motor.turn_on(-turn_speed)
        robot.drive_system.left_motor.turn_on(turn_speed)
        time.sleep(.8)

def celebrate_finish(robot):
    robot.sound_system.speech_maker.speak('yay we won').wait()
    robot.sound_system.speech_maker.speak('good job').wait()
    robot.sound_system.speech_maker.speak('now watch me dance').wait()
    for _ in range(7):
        robot.drive_system.right_motor.turn_on(100)
        robot.drive_system.left_motor.turn_on(-100)
        time.sleep(.2)
        robot.drive_system.right_motor.turn_on(-100)
        robot.drive_system.left_motor.turn_on(100)
        time.sleep(.2)
    robot.drive_system.left_motor.turn_off()
    robot.drive_system.right_motor.turn_off()




