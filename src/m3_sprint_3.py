import time
import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk

def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    root = tkinter.Tk()
    root.title('Cars Racing Game')

    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()

    header_frame, race_frame = get_frames(main_frame,mqtt_sender)

    header_frame.grid(row=0,column=0)
    race_frame.grid(row=1,column=0)

    root.mainloop()

def get_frames(main_frame,mqtt_sender):
    header_frame = get_header_frame(main_frame,mqtt_sender)
    race_frame = get_race_frame(main_frame,mqtt_sender)

    return header_frame, race_frame

def get_header_frame(window,mqtt_sender):
    """
    :type  window:       ttk.Frame | ttk.Toplevel
    :type  mqtt_sender:  com.MqttClient
    """
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')

    #Labels
    frame_label = ttk.Label(frame, text='Welcome to Cars Racing Game',font="bold")
    frame_label.grid(row=0, column=0)

    return frame

def get_race_frame(window,mqtt_sender):
    """
    :type  window:       ttk.Frame | ttk.Toplevel
    :type  mqtt_sender:  com.MqttClient
    """
    frame = ttk.Frame(window, padding=10, borderwidth=5,relief='ridge')

    #Labels
    frame_label = ttk.Label(frame, text='Select your racer')
    frame_label.grid(row=0,column=1)
    lightning_label = ttk.Label(frame,text='Lightning McQueen')
    lightning_label.grid(row=2,column=0)
    doc_label = ttk.Label(frame,text='Doc Hudson')
    doc_label.grid(row=2,column=1)
    sally_label = ttk.Label(frame,text='Sally Carrera')
    sally_label.grid(row=2,column=2)
    lightning_special_label = ttk.Label(frame,text='Specialty: Speed')
    lightning_special_label.grid(row=3,column=0)
    doc_special_label = ttk.Label(frame,text='Specialty: Handling')
    doc_special_label.grid(row=3,column=1)
    sally_special_label = ttk.Label(frame,text='Specialty: Items')
    sally_special_label.grid(row=3,column=2)
    your_name_label = ttk.Label(frame,text='Your Name:')
    your_name_label.grid(row=5,column=0)
    auto_race_label = ttk.Label(frame,text='Automatic Race')
    auto_race_label.grid(row=6,column=0)
    manual_race_label = ttk.Label(frame,text='Manual Race')
    manual_race_label.grid(row=6,column=2)
    turn_choice_label = ttk.Label(frame,text='Turn Choice (left or right):')
    turn_choice_label.grid(row=7,column=0)
    base_speed_label = ttk.Label(frame,text='Base Speed:')
    base_speed_label.grid(row=7,column=2)


    #Check Boxes
    lightning_check = ttk.Checkbutton()
    lightning_check.grid(row=4,column=0)
    doc_check = ttk.Checkbutton()
    doc_check.grid(row=4,column=1)
    sally_check = ttk.Checkbutton()
    sally_check.grid(row=4,column=2)

    #Entry Boxes
    turn_choice_entry = ttk.Entry(frame,width=8)
    turn_choice_entry.grid(row=8,column=0)
    base_speed_entry = ttk.Entry(frame,width=8)
    base_speed_entry.grid(row=8,column=2)
    your_name_entry = ttk.Entry(frame,width=8)
    your_name_entry.grid(row=5,column=1)

    #Buttons
    auto_race_button = ttk.Button(frame,text='GO!')
    auto_race_button.grid(row=8,column=0)
    manual_race_button = ttk.Button(frame,text='GO!')
    manual_race_button.grid(row=8,column=0)

    # Set the Button callbacks:
    auto_race_button["command"] = lambda: handle_auto_go(mqtt_sender,your_name_entry,turn_choice_entry,base_speed_entry,lightning_check,doc_check,sally_check)
    manual_race_button["command"] = lambda: handle_manual_go(mqtt_sender,base_speed_entry,lightning_check,doc_check,sally_check)

    return frame

def handle_auto_go(mqtt_sender,your_name_entry,turn_choice_entry,base_speed_entry,lightning_check,doc_check,sally_check):
    """
    :type  mqtt_sender:  com.MqttClient
    :type  your_name_entry: ttk.Entry
    :type turn_choice_entry: ttk.Entry
    :type base_speed_entry: ttk.Entry
    :type lightning_check: ttk.Checkbutton
    :type doc_check: ttk.Checkbutton
    :type sally_check: ttk.Checkbutton
    """
    print("Auto Go")
    mqtt_sender.send_message('automatic_go', [your_name_entry.get(),turn_choice_entry.get(),base_speed_entry.get(),lightning_check,doc_check,sally_check])

def handle_manual_go(mqtt_sender,base_speed_entry,lightning_check,doc_check,sally_check):
    """
    :type  mqtt_sender:  com.MqttClient
    :type base_speed_entry: ttk.Entry
    :type lightning_check: ttk.Checkbutton
    :type doc_check: ttk.Checkbutton
    :type sally_check: ttk.Checkbutton
    """
    print("Auto Go")
    mqtt_sender.send_message('manual_go', [base_speed_entry.get(),lightning_check,doc_check,sally_check])

main()