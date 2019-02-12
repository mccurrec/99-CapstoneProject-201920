# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
#Jack's Sandbox
m3 = ttk.Frame(main_frame, padding=10, borderwidth=5, relief="ridge")

m3_label = ttk.Label(m3, text="M3 Frame")
m3_display_button = ttk.Button(frame, text="What the camera sees:")#

m3_label.grid(row=0, column=1)
m3_display_button.grid(row=6, column=1)#

m3_spin_clockwise_button = ttk.Button(frame,text="Spin Clockwise")#
m3_spin_clockwise_speed_entry = ttk.Entry(frame, width= 8)#
m3_spin_clockwise_area_entry = ttk.Entry(frame, width= 8)#
m3_spin_clockwise_speed_label = ttk.Label(frame,text= "Speed")#
m3_spin_clockwise_area_label = ttk.Label(frame,text= "Area")#

m3_spin_clockwise_button.grid(row=6,column=0)#
m3_spin_clockwise_speed_label.grid(row=2,column=0)
m3_spin_clockwise_speed_entry.grid(row=3,column=0)
m3_spin_clockwise_area_label.grid(row=4,column=0)
m3_spin_clockwise_area_entry.grid(row=5,column=0)

m3_spin_counterclockwise_button = ttk.Button(frame,text="Spin Counter-Clockwise")
m3_spin_counterclockwise_speed_entry = ttk.Entry(frame, width= 8)#
m3_spin_counterclockwise_area_entry = ttk.Entry(frame, width= 8)#
m3_spin_counterclockwise_speed_label = ttk.Label(frame,text= "Speed")#
m3_spin_counterclockwise_area_label = ttk.Label(frame,text= "Area")#

m3_spin_counterclockwise_button.grid(row=6,column=2)
m3_spin_counterclockwise_speed_label.grid(row=2,column=2)
m3_spin_counterclockwise_speed_entry.grid(row=3,column=2)
m3_spin_counterclockwise_area_label.grid(row=4,column=2)
m3_spin_counterclockwise_area_entry.grid(row=5,column=2)


m3.grid(row=0, column=1)