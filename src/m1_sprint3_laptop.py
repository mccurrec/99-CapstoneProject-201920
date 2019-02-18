import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk


def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title('Amazon Delivery')
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='flat')
    # main_frame.config()
    main_frame.grid()
    teleop_frame, auton_frame = get_frames(main_frame, mqtt_sender)
    grid_frames(teleop_frame, auton_frame)
    root.mainloop()


def get_frames(main_frame, mqtt_sender):
    teleop_frame = get_teleop_frame(main_frame, mqtt_sender)
    auton_frame = get_auton_frame(main_frame, mqtt_sender)
    return teleop_frame, auton_frame


def get_teleop_frame(main_frame, mqtt_sender):
    frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief='ridge')
    frame.grid()
    # LABELS:
    teleop_label = ttk.Label(text='Teleoperation')

    # BUTTONS:
    back_to_start_button = ttk.Button(frame, text='Return To Start')
    go_to_end_label = ttk.Button(frame, text='Go To End')
    retrieve_package = ttk.Button(frame, text='Retrieve Package')
    deliver_package = ttk.Button(frame, text='Deliver Package')

    #GRID:
    teleop_label.grid(row=0, column=0)
    back_to_start_button.grid(row=2, column=0, pady=(0, 10))
    go_to_end_label.grid(row=3, column=0, pady=(0, 10))
    retrieve_package.grid(row=4, column=0, pady=(0, 10))
    deliver_package.grid(row=5, column=0)
    return frame


def get_auton_frame(main_frame, mqtt_sender):
    frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief='ridge')
    frame.grid()
    # LABELS:
    auton_label = ttk.Label(text='Autonomous')
    number_of_packages_label = ttk.Label(text='Number of Packages: ')

    # ENTRIES:
    number_of_packages_entry = ttk.Entry(frame, width=5)

    # BUTTONS:
    sort_packages_button = ttk.Button(frame, text='Sort Packages')

    # GRID:
    auton_label.grid(row=0, column=0, columnspan=2)
    number_of_packages_label.grid(row=1, column=0)
    number_of_packages_entry.grid(row=1, column=1)
    sort_packages_button.grid(row=2, column=0, columnspan=2)

    return frame


def grid_frames(teleop_frame, auton_frame):
    teleop_frame.grid(row=0, column=0)
    auton_frame.grid(row=0, column=1)


main()

