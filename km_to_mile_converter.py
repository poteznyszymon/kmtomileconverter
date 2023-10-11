import tkinter as tk
import ttkbootstrap as ttk

def convert():
    km_input = entry_int.get()
    mile_output = km_input * 0.62
    output_string.set(mile_output)
    window.geometry("450x200")

    
#window 
window = ttk.Window(themename='pulse')
window.title("SimpleConverter")
window.geometry("450x120")

#icon
icon = tk.PhotoImage(file="icon.png")
window.iconphoto(False, icon)

#title
title_label = ttk.Label(master= window, text="Kilometers to Miles", font="Calibri 24 bold")
title_label.pack()

#input_field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command = convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady='10') 

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text="Output",
    font="Calibri 24",
    textvariable=output_string)
output_label.pack(pady='10')

#run
window.mainloop()
