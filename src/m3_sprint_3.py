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



main()