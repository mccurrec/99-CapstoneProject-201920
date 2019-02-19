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

    cars_game_window(main_frame,mqtt_sender)

    root.mainloop()

# def get_frames(main_frame,mqtt_sender):
#     header_frame = get_header_frame(main_frame,mqtt_sender)
#     race_frame = get_race_frame(main_frame,mqtt_sender)
#
#     return header_frame, race_frame

def cars_game_window(window,mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='groove')
    frame.grid()

    #make widgets
    title_label = ttk.Label(frame,text='Welcome to Cars Racing Game',font='Arial 13 bold')
    select_label = ttk.Label(frame,text='Select your Racer',font='Arial 10')
    lightning_image = lightning_picture(frame)
    sally_image = sally_picture(frame)
    doc_image = doc_picture(frame)
    l_specialty_label = ttk.Label(frame,text='Specialty: Speed',font='Arial 8')
    s_specialty_label = ttk.Label(frame,text='Specialty: Items',font='Arial 8')
    d_specialty_label = ttk.Label(frame,text='Specialty: Handling',font='Arial 8')
    l_select_button = ttk.Button(frame,text='Select',font='Arial 8')
    s_select_button = ttk.Button(frame,text='Select',font='Arial 8')
    d_select_button = ttk.Button(frame,text='Select',font='Arial 8')

    grid_widgets(title_label,select_label,lightning_image,sally_image,doc_image,l_specialty_label,s_specialty_label,d_specialty_label,l_select_button,s_select_button,d_select_button)

    l_select_button["command"] = lambda: lightning_race(frame,window,mqtt_sender)
    s_select_button["command"] = lambda: sally_race(frame,window,mqtt_sender)
    d_select_button["command"] = lambda: doc_race(frame,window,mqtt_sender)


    return frame

def grid_widgets(title_label,select_label,lightning_image,sally_image,doc_image,l_specialty_label,s_specialty_label,d_specialty_label,l_select_button,s_select_button,d_select_button):
    title_label.grid(row=0,column=1,columnspan=3)
    select_label.grid(row=1,column=1,columnspan=3)
    lightning_image.grid(row=2,column=0)
    sally_image.grid(row=2,column=1)
    doc_image.grid(row=2,column=2)
    l_specialty_label.grid(row=3,column=0)
    s_specialty_label.grid(row=3,column=1)
    d_specialty_label.grid(row=3,column=2)
    l_select_button.grid(row=4,column=0)
    s_select_button.grid(row=4,column=1)
    d_select_button.grid(row=4,column=2)

def lightning_picture(window):
    path = 'lightning_image.gif'
    img = tkinter.PhotoImage(file=path)
    panel = ttk.Label(window, image=img)
    panel.image = img
    return panel

def sally_picture(window):
    path = 'sally_image.gif'
    img = tkinter.PhotoImage(file=path)
    panel = ttk.Label(window, image=img)
    panel.image = img
    return panel

def doc_picture(window):
    path = 'doc_image.gif'
    img = tkinter.PhotoImage(file=path)
    panel = ttk.Label(window, image=img)
    panel.image = img
    return panel

def lightning_race(last_frame,window,mqtt_sender):
    last_frame.destroy()
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    base_speed_label = ttk.Label(frame,text='Base Speed:',font='Arial 8')
    base_speed_entry = ttk.Entry(frame,width=8)
    auto_race_label = ttk.Label(frame,text='Automatice Race',font='Arial 13 bold')
    manual_race_label = ttk.Label(frame,text='Manual Race',font='Arial 13 bold')
    turn_choice_label = ttk.Label(frame,text='Turn Choice (left or right):',font='Arial 8')
    turn_choice_entry = ttk.Entry(frame,width=8)
    auto_go_button = ttk.Button(frame,text='GO!',font='Arial 10')
    manual_go_button = ttk.Button(frame,text='GO!',font='Arial 10')

    grid_race_widgets(base_speed_label,base_speed_entry,auto_race_label,manual_race_label,turn_choice_label,turn_choice_entry,auto_go_button,manual_go_button)

    auto_go_button["command"] = lambda: handle_lightning_race_auto(base_speed_entry,turn_choice_entry,mqtt_sender)
    # manual_go_button["command"] = lambda: handle_lightning_race_manual(base_speed_entry,mqtt_sender)
    manual_go_button["command"] = lambda: manual_race(base_speed_entry,frame,window,mqtt_sender)

    return frame

def handle_lightning_race_auto(base_speed,turn_choice,mqtt_sender):
    print('Automatice race with Lightning. Base speed is {} and turn choice is {}'.format(base_speed,turn_choice))
    mqtt_sender.send_message('auto_race_lightning', [base_speed.get(),turn_choice.get()])

def handle_lightning_race_manual(base_speed,mqtt_sender):
    print('Manual race with Lightning. Base speed is', base_speed)
    mqtt_sender.send_message('manual_race_lightning', [base_speed.get()])

def sally_race(last_frame, window, mqtt_sender):
    last_frame.destroy()
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

def doc_race(last_frame, window, mqtt_sender):
    last_frame.destroy()
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

def grid_race_widgets(base_speed_label,base_speed_entry,auto_race_label,manual_race_label,turn_choice_label,turn_choice_entry,auto_go_button,manual_go_button):
    base_speed_label.grid(row=0,column=0)
    base_speed_entry.grid(row=0,column=1)
    auto_race_label.grid(row=1,column=0)
    manual_race_label.grid(row=1,column=1)
    turn_choice_label.grid(row=2,column=0)
    turn_choice_entry.grid(row=3,column=0)
    auto_go_button.grid(row=4,column=0)
    manual_go_button.grid(row=4,column=1)

def manual_race(base_speed,last_frame,window,mqtt_sender):
    root = tkinter.Tk()
    last_frame.destroy()
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    explain_label = ttk.Label(frame,text='Use the arrow keys to control your robot',font='Arial 10')
    base_speed_label = ttk.Label(frame,text='Your base speed is {}'.format(base_speed),font='Arial 10')

    explain_label.grid(row=0,column=0)
    base_speed_label.grid(row=1,column=0)

    root.bind_all('<KeyPress>', lambda event: pressed_a_key(event))
    root.bind_all('<KeyRelease>', lambda event: released_a_key(event))

    root.bind_all('<Key-w>', lambda event: go_forward(event,base_speed,mqtt_sender))
    root.bind_all('<Key-s>', lambda event: go_backward(event,base_speed,mqtt_sender))
    root.bind_all('<Key-a>', lambda event: go_left(event,base_speed,mqtt_sender))
    root.bind_all('<Key-d>', lambda event: go_right(event,base_speed,mqtt_sender))

    return frame

def pressed_a_key(event):
    print('You pressed the', event.keysym, 'key')

def released_a_key(event):
    print('You released the', event.keysym, 'key')

def go_forward(event,base_speed,mqtt_sender):
    print('go forward')
    mqtt_sender.send_message('forward_press', [base_speed.get()])

def go_backward(event,base_speed,mqtt_sender):
    print('go backward')
    mqtt_sender.send_message('backward_press', [base_speed.get()])

def go_left(event,base_speed,mqtt_sender):
    print('go left')
    mqtt_sender.send_message('left_press', [base_speed.get()])

def go_right(event,base_speed,mqtt_sender):
    print('go right')
    mqtt_sender.send_message('right_press', [base_speed.get()])

def auto_race_lightning(base_speed,turn_choice,robot):

def auto_race_sally(base_speed, turn_choice, robot):

def auto_race_doc(base_speed, turn_choice, robot):

main()