#Do not touch

import tkinter as tk
from tkinter import ttk
import mqtt_remote_method_calls as com

ir_label = ttk.Label(frame, text='Proximity')
ir_distance_label = ttk.Label(frame, text='Distance')
ir_speed_label = ttk.Label(frame, text='Speed')
ir_delta_label = ttk.Label(frame, text='Delta')

ir_distance_entry = ttk.Entry(frame, width=8)
ir_speed_entry = ttk.Entry(frame, width=8)
ir_delta_entry = ttk.Entry(frame, width=8)


ir_forward_until_button = ttk.Entry(frame, text='Go forward until')
ir_backward_until_button = ttk.Entry(frame, text='Go backward until')
ir_within_button = ttk.Entry(frame, text='Go until within')

ir_label.grid(row=0, column=8)
ir_forward_until_button.grid(row=2, column=8)
ir_backward_until_button.grid(row=3, column=8)
ir_within_button.grid(row=4, column=8)
ir_distance_label.grid(row=2, column=9)
ir_speed_label.grid(row=3, column=9)
ir_delta_label.grid(row=4, column=9)
ir_distance_entry.grid(row=2, column=10)
ir_speed_entry.grid(row=3, column=10)
ir_delta_entry.grid(row=4, column=10)


















