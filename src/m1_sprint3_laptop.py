import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk


def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title('Amazon Delivery')
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='flat')
    main_frame.grid()
    teleop_frame, auton_frame = get_frames(main_frame, mqtt_sender)
    grid_frames(teleop_frame, auton_frame)
    root.mainloop()


def get_frames(main_frame, mqtt_sender):
    teleop_frame = get_teleop_frame(main_frame, mqtt_sender)
    auton_frame = get_auton_frame(main_frame, mqtt_sender)
    return teleop_frame, auton_frame


def grid_frames(teleop_frame, auton_frame):
    teleop_frame.grid(row=0, column=0)
    auton_frame.grid(row=0, column=1)


def get_teleop_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')

    # LABELS:
    frame_label = ttk.Label(frame, text='Teleoperation', font='bold')
    frame_label.grid(row=0, column=0)

    # BUTTONS:
    return_to_start_button = ttk.Button(frame, text='Return To Start')
    return_to_start_button.grid(row=1, column=0, sticky='E'+'W', pady=(10, 2))
    return_to_start_button['command'] = lambda: handle_return_to_start(mqtt_sender)

    go_to_end_button = ttk.Button(frame, text='Go To End')
    go_to_end_button.grid(row=2, column=0, sticky='E'+'W', pady=(0, 10))
    go_to_end_button['command'] = lambda: handle_go_to_end(mqtt_sender)

    retrieve_package_button = ttk.Button(frame, text='Retrieve Package')
    retrieve_package_button.grid(row=3, column=0, sticky='E'+'W', pady=(0, 2))
    retrieve_package_button['command'] = lambda: handle_retrieve_package(mqtt_sender)

    deliver_package_button = ttk.Button(frame, text='Deliver Package')
    deliver_package_button.grid(row=4, column=0, sticky='E'+'W')
    deliver_package_button['command'] = lambda: handle_deliver_package(mqtt_sender)

    return frame


def get_auton_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')

    # LABELS:
    frame_label = ttk.Label(frame, text='Autonomous', font='bold')
    frame_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    number_of_package_label = ttk.Label(frame, text='Number of Packages: ')
    number_of_package_label.grid(row=1, column=0)

    # ENTRIES:
    number_of_package_entry = ttk.Entry(frame, width=5)
    number_of_package_entry.grid(row=1, column=1)

    # BUTTONS:
    sort_packages_button = ttk.Button(frame, text='Sort Packages')
    sort_packages_button.grid(row=2, column=0, columnspan=2, sticky='E'+'W', pady=(2, 0))
    sort_packages_button['command'] = lambda: handle_sort_packages(number_of_package_entry, mqtt_sender)

    return frame


def handle_return_to_start(mqtt_sender):
    """
    :type mqtt_sender: com.MqttClient
    """
    print('sending return to start')
    mqtt_sender.send_message('return_to_start')


def handle_go_to_end(mqtt_sender):
    """
    :type mqtt_sender: com.MqttClient
    """
    print('sending go to end')
    mqtt_sender.send_message('go_to_end')


def handle_retrieve_package(mqtt_sender):
    """
    :type mqtt_sender: com.MqttClient
    """
    print('sending retrieve package')
    mqtt_sender.send_message('retrieve_package')


def handle_deliver_package(mqtt_sender):
    """
    :type mqtt_sender: com.MqttClient
    """
    print('sending deliver package')
    mqtt_sender.send_message('deliver_package')


def handle_sort_packages(number_of_packages_entry, mqtt_sender):
    """
    :type number_of_packages_entry: ttk.Entry
    :type mqtt_sender: com.MqttClient
    """
    print('sending sort packages')
    mqtt_sender.send_message('sort_packages', [int(number_of_packages_entry.get())])


main()

