import mqtt_remote_method_calls as com
import time

def forward_press(base_speed,robot):
    robot.drivesystem.go(base_speed,base_speed)

def go_backward(event,base_speed,mqtt_sender):
    print('go backward')
    mqtt_sender.send_message('backward_press', [base_speed])

def backward_press(base_speed,robot):
    robot.drivesystem.go(-base_speed,-base_speed)

def go_left(event,base_speed,mqtt_sender):
    print('go left')
    mqtt_sender.send_message('left_press', [base_speed])

def left_press(base_speed,robot):
    robot.drivesystem.go(-base_speed,base_speed)

def go_right(event,base_speed,mqtt_sender):
    print('go right')
    mqtt_sender.send_message('right_press', [base_speed])

def right_press(base_speed,robot):
    robot.drivesystem.go(base_speed,-base_speed)

# def auto_race_lightning(base_speed,turn_choice,robot):
#     robot.drivesystem.go((base_speed+100))
# def auto_race_sally(base_speed, turn_choice, robot):
#
# def auto_race_doc(base_speed, turn_choice, robot):