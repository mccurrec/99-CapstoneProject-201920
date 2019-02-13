"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Loki Strain, Ezrie McCurry, Jack Franey.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame.grid_columnconfigure(1, weight=1)
    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation", font='bold')
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    #    Grid the labels:
    frame_label.grid(row=0, column=0, columnspan=3)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    #   Grid the entries:
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)
    #   Grid the buttons:
    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0, sticky='E')
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2, sticky='W')
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame.grid_columnconfigure(1, weight=1)

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw", font='bold')
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1, columnspan=3, sticky='W')
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_sound_frame(window, mqtt_sender):
    """
        Constructs and returns a frame on the given window, where the frame has
        Button objects and entry boxes containing sounds commands.
          :type  window:       ttk.Frame | ttk.Toplevel
          :type  mqtt_sender:  com.MqttClient
        """

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame.grid_columnconfigure(1, weight=1)

    # labels
    frame_label = ttk.Label(frame, text="Sound System", font='bold')
    tone_label = ttk.Label(frame, text="Tone Player")
    frequency_label = ttk.Label(frame, text="Frequency")
    duration_label = ttk.Label(frame, text="Duration")
    speak_phrase_label = ttk.Label(frame, text="Speak Phrase")
    speak_phrase_word_label = ttk.Label(frame, text="Phrase")
    beep_label = ttk.Label(frame, text="Beep")
    number_of_beeps_label = ttk.Label(frame, text='Number of Beeps')

    # entry boxes
    frequency_entry = ttk.Entry(frame, width=8)
    duration_entry = ttk.Entry(frame, width=8)
    speak_phrase_entry = ttk.Entry(frame, width=8)
    beep_entry = ttk.Entry(frame, width=8)

    # buttons
    tone_button = ttk.Button(frame, text="Tone")
    speak_phrase_button = ttk.Button(frame, text="Speak")
    beep_button = ttk.Button(frame, text='Beep')

    # grid stuff
    frame_label.grid(row=0, column=0, columnspan=3)
    tone_label.grid(row=1, column=1)
    frequency_label.grid(row=2, column=1)
    frequency_entry.grid(row=3, column=1)
    duration_label.grid(row=4, column=1)
    duration_entry.grid(row=5, column=1)
    tone_button.grid(row=6, column=1)
    speak_phrase_label.grid(row=1, column=0)
    speak_phrase_button.grid(row=6, column=0)
    speak_phrase_entry.grid(row=5, column=0)
    speak_phrase_word_label.grid(row=4, column=0)
    beep_label.grid(row=1, column=2)
    number_of_beeps_label.grid(row=4, column=2)
    beep_entry.grid(row=5, column=2)
    beep_button.grid(row=6, column=2)

    tone_button["command"] = lambda: handle_tone(frequency_entry, duration_entry, mqtt_sender)
    beep_button['command'] = lambda: handle_beep(beep_entry, mqtt_sender)
    speak_phrase_button['command'] = lambda: handle_speak_phrase(speak_phrase_entry, mqtt_sender)
    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame.grid_columnconfigure(1, weight=1)

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control", font='bold')
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=0, columnspan=3)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_drive_system_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    buttons and entry boxes containing drive system commands.
        :type  window:       ttk.Frame | ttk.Toplevel
        :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame.grid_columnconfigure(2, weight=1)

    # Construct the Widgets on the Frame:
    frame_label = ttk.Label(frame, text='Drive System', font='bold')
    inches_label = ttk.Label(frame, text='Inches: ')
    time_label = ttk.Label(frame, text='Time: ')
    intensity_label = ttk.Label(frame, text='Intensity: ')
    color_label = ttk.Label(frame, text='Color: ')
    area_label = ttk.Label(frame, text='Area: ')
    speed_label = ttk.Label(frame, text='Speed: ')
    distance_label = ttk.Label(frame, text='Distance: ')
    delta_label = ttk.Label(frame, text='Delta: ')

    # Constructs the entry boxes on the frame:
    speed_entry = ttk.Entry(frame, width=8)
    inches_entry = ttk.Entry(frame, width=8)
    time_entry = ttk.Entry(frame, width=8)
    intensity_entry = ttk.Entry(frame, width=8)
    color_entry = ttk.Entry(frame, width=8)
    area_entry = ttk.Entry(frame, width=8)
    distance_entry = ttk.Entry(frame, width=8)
    delta_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, '50')

    # Constructs the buttons on the frame:
    inches_using_time_button = ttk.Button(frame, text="Go Using Time")
    go_straight_using_encoder_button = ttk.Button(frame, text='Go Using Encoder')
    go_straight_for_seconds_button = ttk.Button(frame, text='Go For Seconds')
    go_straight_until_intensity_is_less_than_button = ttk.Button(frame, text='Go Until Less Than')
    go_straight_until_intensity_is_greater_than_button = ttk.Button(frame, text='Go Until Greater Than')
    go_straight_until_color_is_button = ttk.Button(frame, text='Go Until Color Is')
    go_straight_until_color_is_not_button = ttk.Button(frame, text='Go Until Color Is Not')
    m3_spin_clockwise_button = ttk.Button(frame, text="Spin Clockwise")
    m3_spin_counterclockwise_button = ttk.Button(frame, text="Spin Counter-Clockwise")
    m3_display_button = ttk.Button(frame, text="What The Camera Sees")
    ir_forward_until_button = ttk.Button(frame, text='Go Forward Until')
    ir_backward_until_button = ttk.Button(frame, text='Go Backward Until')
    ir_within_button = ttk.Button(frame, text='Go Until Within')

    #  Grids the Widgets:
    #   Grids the labels:
    frame_label.grid(row=0, column=0, columnspan=2)
    inches_label.grid(row=1, column=0, sticky='E')
    time_label.grid(row=3, column=0, sticky='E')
    intensity_label.grid(row=4, column=0, sticky='E')
    color_label.grid(row=6, column=0, sticky='E')
    area_label.grid(row=8, column=0, sticky='E')
    speed_label.grid(row=0, column=2, sticky='E')
    distance_label.grid(row=10, column=0, sticky='E')
    delta_label.grid(row=12, column=0, sticky='E')

    #   Grids the entry boxes:
    speed_entry.grid(row=0, column=3, sticky='W')
    inches_entry.grid(row=1, column=1)
    time_entry.grid(row=3, column=1)
    intensity_entry.grid(row=4, column=1)
    color_entry.grid(row=6, column=1)
    area_entry.grid(row=8, column=1)
    distance_entry.grid(row=10, column=1)
    delta_entry.grid(row=12, column=1)

    #   Grids the buttons:
    inches_using_time_button.grid(row=1, column=2, sticky='W', ipadx='26', columnspan=2)
    go_straight_using_encoder_button.grid(row=2, column=2, sticky='W', pady=(0, 8), ipadx='18', columnspan=2)
    go_straight_for_seconds_button.grid(row=3, column=2, sticky='W', pady=(0, 8), ipadx='23', columnspan=2)
    go_straight_until_intensity_is_less_than_button.grid(row=4, column=2, sticky='W', ipadx='15', columnspan=2)
    go_straight_until_intensity_is_greater_than_button.grid(row=5, column=2, sticky='W', pady=(0, 8), ipadx='7',
                                                            columnspan=2)
    go_straight_until_color_is_button.grid(row=6, column=2, sticky='W', ipadx='20', columnspan=2)
    go_straight_until_color_is_not_button.grid(row=7, column=2, sticky='W', pady=(0, 8), ipadx='9', columnspan=2)
    m3_spin_clockwise_button.grid(row=8, column=2, sticky='W', ipadx='24', columnspan=2)
    m3_spin_counterclockwise_button.grid(row=9, column=2, sticky='W', pady=(0, 8), columnspan=2)
    ir_forward_until_button.grid(row=10, column=2, sticky='W', ipadx='18', columnspan=2)
    ir_within_button.grid(row=11, column=2, sticky='W', pady=(0, 8), ipadx='22', columnspan=2)
    ir_backward_until_button.grid(row=12, column=2, sticky='W', pady=(0, 8), ipadx='14', columnspan=2)
    m3_display_button.grid(row=13, column=0, columnspan=3)

    # Sets the button callbacks:
    inches_using_time_button['command'] = lambda: handle_inches_using_time(inches_entry,
                                                                           speed_entry, mqtt_sender)
    go_straight_for_seconds_button['command'] = lambda: handle_go_straight_for_seconds(
        time_entry, speed_entry, mqtt_sender)
    go_straight_using_encoder_button['command'] = lambda: handle_go_straight_using_encoder(speed_entry, inches_entry, mqtt_sender)
    go_straight_until_intensity_is_less_than_button['command'] = lambda: handle_go_straight_until_intensity_is_less_than(
        intensity_entry, speed_entry, mqtt_sender)
    go_straight_until_intensity_is_greater_than_button['command'] = lambda: handle_go_straight_until_intensity_is_greater_than(
        intensity_entry, speed_entry, mqtt_sender)
    go_straight_until_color_is_button['command'] = lambda: handle_go_straight_until_color_is(
        color_entry, speed_entry, mqtt_sender)
    go_straight_until_color_is_not_button['command'] = lambda: handle_go_straight_until_color_is_not(
        color_entry, speed_entry, mqtt_sender)
    m3_display_button['command'] = lambda: handle_m3_display(mqtt_sender)
    m3_spin_clockwise_button['command'] = lambda: handle_m3_spin_clockwise(speed_entry, area_entry, mqtt_sender)
    m3_spin_counterclockwise_button['command'] = lambda: handle_m3_spin_counterclockwise(speed_entry, area_entry, mqtt_sender)
    ir_forward_until_button['command'] = lambda: handle_forward_until(distance_entry, speed_entry, mqtt_sender)
    ir_backward_until_button['command'] = lambda: handle_backward_until(distance_entry, speed_entry, mqtt_sender)
    ir_within_button['command'] = lambda: handle_within(distance_entry, distance_entry, delta_entry, mqtt_sender)

    return frame


def get_m1_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')

    # LABELS:
    frame_label = ttk.Label(frame, text='Individual Features', font='bold')
    frame_label.grid(row=0, column=0, columnspan=2)
    initial_label = ttk.Label(frame, text='Initial Time Between Beeps: ')
    initial_label.grid(row=3, column=0, sticky='E')
    decrease_label = ttk.Label(frame, text='Decrease Time Between Beeps By: ')
    decrease_label.grid(row=4, column=0, sticky='E')

    # ENTRY BOXES:
    initial_entry = ttk.Entry(frame, width=8)
    initial_entry.grid(row=3, column=1)
    decrease_entry = ttk.Entry(frame, width=8)
    decrease_entry.grid(row=4, column=1)

    # BUTTONS:
    run_button = ttk.Button(frame, text='Go Straight')
    run_button.grid(row=5, column=0, columnspan=2, sticky='E'+'W')
    run_button['command'] = lambda: handle_m1_feature_9(initial_entry, decrease_entry, mqtt_sender)

    spin_cw_button = ttk.Button(frame, text='Spin Clockwise')
    spin_cw_button.grid(row=6, column=0, columnspan=2, sticky='E'+'W')
    spin_cw_button['command'] = lambda: handle_m1_spin_cw(initial_entry, decrease_entry, mqtt_sender)

    spin_ccw_button = ttk.Button(frame, text='Spin Counter-Clockwise')
    spin_ccw_button.grid(row=7, column=0, columnspan=2, sticky='E'+'W')
    spin_ccw_button['command'] = lambda: handle_m1_spin_ccw(initial_entry, decrease_entry, mqtt_sender)

    line_follow_button = ttk.Button(frame, text='Line Follower')
    line_follow_button.grid(row=8, column=0, columnspan=2, sticky='E'+'W')
    line_follow_button['command'] = lambda: handle_m1_line_follow(mqtt_sender)

    return frame


def get_m2_frame(window, mqtt_sender):
    """
          :type  window:       ttk.Frame | ttk.Toplevel
          :type  mqtt_sender:  com.MqttClient
        """
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    m2_label = ttk.Label(frame, text="M2 Frame")
    m2_label.grid(row=0, column=0)
    m2_entry1_label = ttk.Label(text="Init Frequency")
    m2_entry1 = ttk.Entry(frame, width=8)
    m2_entry1.grid(row=2, column=0)
    m2_entry1_label.grid(row=1, column=0)
    m2_entry2_label = ttk.Label(frame, text="Iteration")
    m2_entry2 = ttk.Entry(frame, width=8)
    m2_entry2_label.grid(row=3, column=0)
    m2_entry2.grid(row=4, column=0)
    m2_button = ttk.Button(frame, text="Wild Thang")
    m2_button.grid(row=5, column=0)
    m2_button['command'] = lambda: handle_m2(m2_entry1, m2_entry2, mqtt_sender)

    return frame


def get_m3_frame(window, mqtt_sender):
    """
    :type  window:       ttk.Frame | ttk.Toplevel
    :type  mqtt_sender:  com.MqttClient
    """
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')

    # LABELS:
    frame_label = ttk.Label(frame, text='m3 Feature 9')
    frame_label.grid(row=0, column=0)
    # speed_label = ttk.Label(frame, text='Speed: ')
    # speed_label.grid(row=1, column=0)
    initial_label = ttk.Label(frame, text='Initial Time Between Light Cycles: ')
    initial_label.grid(row=2, column=0)
    decrease_label = ttk.Label(frame, text='Decrease Time Between Cycles By: ')
    decrease_label.grid(row=3, column=0)

    # ENTRY BOXES:
    # speed_entry = ttk.Entry(frame, width=8)
    # speed_entry.grid(row=1, column=1)
    initial_entry = ttk.Entry(frame, width=8)
    initial_entry.grid(row=2, column=1)
    decrease_entry = ttk.Entry(frame, width=8)
    decrease_entry.grid(row=3, column=1)

    # BUTTONS:
    run_button = ttk.Button(frame, text='RUN')
    run_button.grid(row=4, column=1)
    run_button['command'] = lambda: handle_m3_feature_9(initial_entry, decrease_entry, mqtt_sender)

    return frame


def m3_feature_10(window,mqtt_sender):
    """
    :type  window:       ttk.Frame | ttk.Toplevel
    :type  mqtt_sender:  com.MqttClient
    """
    frame = ttk.Frame(window,padding=10,borderwidth=5,relief='ridge')

    # LABELS:
    frame_label = ttk.Label(frame, text='m3 Feature 10')
    frame_label.grid(row=0, column=0)
    speed_label = ttk.Label(frame, text='Speed: ')
    speed_label.grid(row=1, column=0)
    direction_label = ttk.Label(frame, text='Direction (clockwise or counterclockwise)')
    direction_label.grid(row=2, column=0)
    # decrease_label = ttk.Label(frame, text='Decrease Time Between Cycles By: ')
    # decrease_label.grid(row=3, column=0)

    # ENTRY BOXES:
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid(row=1, column=1)
    direction_entry = ttk.Entry(frame, width=8)
    direction_entry.grid(row=2, column=1)
    # decrease_entry = ttk.Entry(frame, width=8)
    # decrease_entry.grid(row=3, column=1)

    # BUTTONS:
    run_button = ttk.Button(frame, text='RUN')
    run_button.grid(row=3, column=1)
    run_button['command'] = lambda: handle_m3_feature_10(speed_entry, direction_entry, mqtt_sender)

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################


def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("forward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('backward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('backward', [left_entry_box.get(), right_entry_box.get()])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('left', - int(left_entry_box.get()), right_entry_box.get())
    mqtt_sender.send_message('left', [- int(left_entry_box.get()), int(right_entry_box.get())])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('right', left_entry_box.get(), - int(right_entry_box.get()))
    mqtt_sender.send_message('right', [int(left_entry_box.get()), - int(right_entry_box.get())])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('stop')
    mqtt_sender.send_message('stop')


###############################################################################
# Handlers for Buttons in the DriveSystem frame.
###############################################################################
def handle_inches_using_time(inches_entry, speed_entry, mqtt_sender):
    """Tells robot to move for an amount of inches based on time conversion
    :type inches_entry:  ttk.Entry
    :type speed_entry:  ttk.Entry
    :type  mqtt_sender:      com.MqttClient"""

    print("Moving ", inches_entry.get(), " inches")
    mqtt_sender.send_message('inches_using_time', [int(inches_entry.get()), int(speed_entry.get())])


def handle_go_straight_using_encoder(speed_entry, inches_entry, mqtt_sender):
    """
    Tells robot to move forward at a given speed for a given amount of inches using the motor's encoder to determine
    the inches traveled
    :type speed_entry:  ttk.Entry
    :type inches_entry: ttk.Entry
    :type mqtt_sender:  com.MqttClient
    """
    print('Moving at speed:', speed_entry, 'for', inches_entry, 'inches')
    mqtt_sender.send_message('go_straight_for_inches_using_encoder', [inches_entry.get(), speed_entry.get()])


def handle_go_straight_for_seconds(time_entry, speed_entry, mqtt_sender):
    """
        Tells the robot to move forward at a given speed for a given number of seconds
          :type  speed_entry:   ttk.Entry
          :type  time_entry:  ttk.Entry
          :type  mqtt_sender:      com.MqttClient
        """
    print('Moving at speed:', speed_entry, 'for', time_entry, 'seconds.')
    mqtt_sender.send_message('go_straight_for_seconds', [speed_entry.get(), time_entry.get()])


def handle_go_straight_until_intensity_is_less_than(intensity_entry, speed_entry, mqtt_sender):
    """
    Tells robot to move forward at a given speed for a given amount of inches using the motor's encoder to determine the inches traveled
    :type intensity_entry:  ttk.Entry
    :type speed_entry:  ttk.Entry
    :type mqtt_sender:  com.MqttClient
    """
    print('Go straight until intensity is less than', intensity_entry.get())
    mqtt_sender.send_message('go_straight_until_intensity_is_less_than', [intensity_entry.get(), speed_entry.get()])


def handle_go_straight_until_intensity_is_greater_than(intensity_entry, speed_entry, mqtt_sender):
    """
    Tells robot to move forward at a given speed for a given amount of inches using the motor's encoder to determine the inches traveled
    :type intensity_entry:  ttk.Entry
    :type speed_entry:  ttk.Entry
    :type mqtt_sender:  com.MqttClient
    """
    print('Go straight until intensity is greater than', intensity_entry.get())
    mqtt_sender.send_message('go_straight_until_intensity_is_greater_than', [intensity_entry.get(), speed_entry.get()])


def handle_go_straight_until_color_is(color_entry, speed_entry, mqtt_sender):
    """
    Tells robot to move forward at a given speed for a given amount of inches using the motor's encoder to determine the inches traveled
    :type color_entry:  ttk.Entry
    :type speed_entry:  ttk.Entry
    :type mqtt_sender:  com.MqttClient
    """
    print('Go straight until color is', color_entry.get())
    mqtt_sender.send_message('go_straight_until_color_is', [color_entry.get(), speed_entry.get()])


def handle_go_straight_until_color_is_not(color_entry, speed_entry, mqtt_sender):
    """
    Tells robot to move forward at a given speed for a given amount of inches using the motor's encoder to determine the inches traveled
    :type color_entry:  ttk.Entry
    :type speed_entry:  ttk.Entry
    :type mqtt_sender:  com.MqttClient
    """
    print('Go straight until color is not', color_entry.get())
    mqtt_sender.send_message('go_straight_until_color_is_not', [color_entry.get(), speed_entry.get()])


def handle_m3_spin_clockwise(speed_entry, area_entry, mqtt_sender):
    """
    :type speed_entry:  ttk.Entry
    :type area_entry:    ttk.Entry
    :type mqtt_sender:  com.MqttClient
    """
    print("Spin Clockwise until color is big enough, Speed: {}, Area: {}".format(speed_entry.get(), area_entry.get()))
    mqtt_sender.send_message('spin_clockwise_until_sees_object', [speed_entry.get(), area_entry.get()])


def handle_m3_spin_counterclockwise(speed_entry, area_entry, mqtt_sender):
    """
    :type speed_entry:  ttk.Entry
    :type area_entry:    ttk.Entry
    :type mqtt_sender:  com.MqttClient
    """
    print("Spin Counterclockwise until color is big enough. Speed: {}, Area: {}".format(speed_entry.get(),
                                                                                        area_entry.get()))
    mqtt_sender.send_message('spin_counterclockwise_until_sees_object', [speed_entry.get(), area_entry.get()])


def handle_forward_until(ir_distance_entry, speed_entry, mqtt_sender):
    print('Forward until ', ir_distance_entry.get(), ' away')
    mqtt_sender.send_message('forward_until', [ir_distance_entry.get(), speed_entry.get()])


def handle_backward_until(ir_distance_entry, speed_entry, mqtt_sender):
    print('Backward until ', ir_distance_entry.get(), ' away')
    mqtt_sender.send_message('backward_until', [ir_distance_entry.get(), speed_entry.get()])


def handle_within(ir_distance_entry, speed_entry, ir_delta_entry, mqtt_sender):
    print('Move until ', ir_distance_entry, ' away')
    mqtt_sender.send_message('within', [ir_distance_entry.get(), speed_entry.get(), ir_delta_entry.get()])


def handle_m3_display(mqtt_sender):
    print("Camera data")
    mqtt_sender.send_message('display_camera_data')

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Raise Arm')
    mqtt_sender.send_message('raise_arm')


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Lower Arm')
    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Calibrate Arm')
    mqtt_sender.send_message('calibrate_arm')


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """

    print('Move arm to position', arm_position_entry.get())
    mqtt_sender.send_message('move_arm_to_position', [arm_position_entry.get()])

###############################################################################
# Handlers for Buttons in the Sound frame.
###############################################################################
def handle_tone(frequency_entry, duration_entry, mqtt_sender):
    """
    :type frequency_entry:  ttk.Entry
    :type duration_entry: ttk.Entry
    :type mqtt_sender: com.MqttClient
    """
    print("Playing tone at ", frequency_entry.get(), " for ", duration_entry.get())
    mqtt_sender.send_message('tone', [frequency_entry.get(), duration_entry.get()])


def handle_speak_phrase(phrase_entry, mqtt_sender):
    """
    :type phrase_entry: ttk.Entry
    :type mqtt_sender: com.MqttClient
    """
    print('Speaking the phrase: {}'.format(phrase_entry.get()))
    mqtt_sender.send_message('speak_phrase', [str(phrase_entry.get())])


def handle_beep(beep_entry, mqtt_sender):
    """
    :type beep_entry:  ttk.Entry
    :type mqtt_sender: com.MqttClient
    """
    print('I will beep {} times.'.format(beep_entry.get()))
    mqtt_sender.send_message('beep', [beep_entry.get()])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print("quit the robot's program")
    mqtt_sender.send_message("quit")


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print("quit the robot's program and exit this")
    handle_quit(mqtt_sender)
    exit()

##############################################################################
# Handles for Sprint 2 Feature 8 and 9:
##############################################################################
def handle_m1_feature_9(initial_rate_entry, rate_of_increase_entry, mqtt_sender):
    """
    :type initial_rate_entry:  ttk.Entry
    :type rate_of_increase_entry:  ttk.Entry
    :type mqtt_sender: com.MqttClient
    """
    print('sending m1_feature9')
    mqtt_sender.send_message('m1_feature_9', [float(initial_rate_entry.get()), float(rate_of_increase_entry.get())])


def handle_m1_spin_cw(initial_rate_entry, rate_of_increase_entry, mqtt_sender):
    """
    :type initial_rate_entry:  ttk.Entry
    :type rate_of_increase_entry:  ttk.Entry
    :type mqtt_sender: com.MqttClient
    """
    print('sending m1 spin clockwise to find cube')
    mqtt_sender.send_message('m1_spin_cw', [float(initial_rate_entry.get()), float(rate_of_increase_entry.get())])


def handle_m1_spin_ccw(initial_rate_entry, rate_of_increase_entry, mqtt_sender):
    """
    :type initial_rate_entry:  ttk.Entry
    :type rate_of_increase_entry:  ttk.Entry
    :type mqtt_sender: com.MqttClient
    """
    print('sending m1 spin counter-clockwise to find cube')
    mqtt_sender.send_message('m1_spin_ccw', [float(initial_rate_entry.get()), float(rate_of_increase_entry.get())])


def handle_m2(m2_entry1, m2_entry2, mqtt_sender):
    """:type mqtt_sender: com.MqttClient"""
    print('got')
    mqtt_sender.send_message("m2", [m2_entry1.get(), m2_entry2.get()])


def handle_m3_feature_9(initial_rate_entry, rate_of_increase_entry, mqtt_sender):
    """
    :type initial_rate_entry:  ttk.Entry
    :type rate_of_increase_entry:  ttk.Entry
    :type mqtt_sender: com.MqttClient
    """
    print('sending m3_feature9')
    mqtt_sender.send_message('m3_feature_9', [float(initial_rate_entry.get()), float(rate_of_increase_entry.get())])


def handle_m3_feature_10(speed_entry, direction_entry, mqtt_sender):
    """
   :type speed_entry: ttk.Entry
   :type direction_entry: ttk.Entry
   :type mqtt_sender: com.MqttClient
    """
    print("sending m3_feature_10")
    mqtt_sender.send_message('m3_feature_10', [int(speed_entry.get()),str(direction_entry.get())])


##############################################################################
# Handles for Sprint 2 Feature 11:
##############################################################################

def handle_m1_line_follow(mqtt_sender):
    """"
    :type mqtt_sender: com.MqttClient
    """
    print('sending m1_line_follow')
    mqtt_sender.send_message('m1_line_follow')


