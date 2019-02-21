import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk


def main():
    pc_receiver = PcReceiver(None)
    mqtt_sender = com.MqttClient(pc_receiver)
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title('Amazon Delivery')
    main_frame = tkinter.Frame(root, borderwidth=5, relief='flat', bg='turquoise4')
    main_frame.grid()
    teleop_frame, auton_frame = get_frames(main_frame, mqtt_sender, pc_receiver)
    grid_frames(teleop_frame, auton_frame)
    root.mainloop()


def get_frames(main_frame, mqtt_sender, pc_receiver):
    teleop_frame = get_teleop_frame(main_frame, mqtt_sender)
    auton_frame = get_auton_frame(main_frame, mqtt_sender, pc_receiver)
    return teleop_frame, auton_frame


def grid_frames(teleop_frame, auton_frame):
    teleop_frame.grid(row=0, column=0)
    auton_frame.grid(row=0, column=1, sticky='N' + 'S')


def get_teleop_frame(window, mqtt_sender):
    frame = tkinter.Frame(window, borderwidth=5, relief='groove', bg='turquoise4')

    # LABELS:
    frame_label = ttk.Label(frame, text='Teleoperation', font='bold', background='turquoise4')
    frame_label.grid(row=0, column=0)

    # BUTTONS:
    return_to_start_button = tkinter.Button(frame, text='Go To Delivery Zone', bg='PaleTurquoise3',
                                            activebackground='PaleTurquoise3')
    return_to_start_button.grid(row=1, column=0, sticky='E' + 'W', pady=(10, 2))
    return_to_start_button['command'] = lambda: handle_go_to_target(mqtt_sender)

    go_to_end_button = tkinter.Button(frame, text='Return To Retrieval Zone', bg='PaleTurquoise3',
                                      activebackground='PaleTurquoise3')
    go_to_end_button.grid(row=2, column=0, sticky='E' + 'W', pady=(0, 10))
    go_to_end_button['command'] = lambda: handle_return_to_target(mqtt_sender)

    retrieve_package_button = tkinter.Button(frame, text='Retrieve Package', bg='PaleTurquoise3',
                                             activebackground='PaleTurquoise3')
    retrieve_package_button.grid(row=3, column=0, sticky='E' + 'W', pady=(0, 2))
    retrieve_package_button['command'] = lambda: handle_retrieve_package(mqtt_sender)

    deliver_package_button = tkinter.Button(frame, text='Deliver Package', bg='PaleTurquoise3',
                                            activebackground='PaleTurquoise3')
    deliver_package_button.grid(row=4, column=0, sticky='E' + 'W')
    deliver_package_button['command'] = lambda: handle_deliver_package(mqtt_sender)

    return frame


def get_auton_frame(window, mqtt_sender, pc_receiver):
    frame = tkinter.Frame(window, borderwidth=5, relief='groove', bg='turquoise4')

    # LABELS:
    frame_label = ttk.Label(frame, text='Autonomous', font='bold', background='turquoise4')
    frame_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    number_of_package_label = ttk.Label(frame, text='Number of Packages: ', background='turquoise4')
    number_of_package_label.grid(row=1, column=0)

    # ENTRIES:
    number_of_package_entry = tkinter.Entry(frame, width=5, background='DarkSlateGray1')
    number_of_package_entry.grid(row=1, column=1)

    # BUTTONS:
    sort_packages_button = tkinter.Button(frame, text='Sort Packages', bg='PaleTurquoise3',
                                          activebackground='PaleTurquoise3')
    sort_packages_button.grid(row=2, column=0, columnspan=2, sticky='E' + 'W', pady=(2, 0))
    sort_packages_button['command'] = lambda: handle_sort_packages(number_of_package_entry, mqtt_sender)
    # get_value_button = ttk.Button(frame, text='Get Current Light Value')
    # get_value_button.grid(row=4, column=0)
    # get_value_button['command'] = lambda: handle_get_value(mqtt_sender)

    # PROGRESS BAR:
    # value = tkinter.IntVar()
    # value.set(0)
    # mqtt_sender.connect_to_ev3()
    progress_bar = ttk.Progressbar(frame, orient='horizontal', mode='determinate')
    progress_bar.grid(row=3, column=0, columnspan=2, sticky='E' + 'W', pady=(8, 0))
    # pc_receiver.progress_bar = progress_bar

    return frame


def handle_go_to_target(mqtt_sender):
    """
    :type mqtt_sender: com.MqttClient
    """
    print('sending go to target')
    mqtt_sender.send_message('go_to_target')


def handle_return_to_target(mqtt_sender):
    """
    :type mqtt_sender: com.MqttClient
    """
    print('sending return to target')
    mqtt_sender.send_message('return_to_target')


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


def handle_get_value(mqtt_sender):
    """
    :type mqtt_sender: com.MqttClient
    """
    mqtt_sender.send_message('get_value')


class PcReceiver(object):

    def __init__(self, progress_bar):
        self.progress_bar = progress_bar

    def update_progress(self, progress_value):
        # self.progress_bar['value'] = progress_value
        print('attempted to update the progress', progress_value)


main()

