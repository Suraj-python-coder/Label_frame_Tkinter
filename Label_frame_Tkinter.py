# label frame widget:
# ===================

import tkinter as tk       
from tkinter import ttk  
win = tk.Tk() 
win.title('LOOP')

label_frame = ttk.LabelFrame(win, text='Enter your details below')
label_frame.grid(row=0,column=0, padx=20,pady=20)


# create label :
# =================

labels = ['What is your name : ', 'what is your Age : ', 'what is your Gender : ', 'Country : ', 'State : ', 'City : ']

for i in range(len(labels)):
    cur_label = 'label' + str(i) # label0,label1-----etc.
    cur_label = ttk.Label(label_frame, text=labels[i])
    # cur_label.grid(row=i,column=0,sticky=tk.W, padx=3,pady=3) 
    cur_label.grid(row=i,column=0,sticky=tk.W) 


# entry box:
# ===========
name_var = tk.StringVar()
user_info = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()

}
counter=0
for i in user_info:
    cur_entrybox = 'entry_' + i   # entry_name, entry_age----etc.
    cur_enterybox = ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    # cur_enterybox.grid(row=counter,column=1, padx=3,pady=3)
    cur_enterybox.grid(row=counter,column=1)

    counter += 1

# submit button:
#===============

def submit():
    print(user_info['name'].get())      # here we use the tkinter's get methode
    print(user_info.get('age').get())   # here we use the dictionaries's get methode
    print(user_info.get('gender').get())  # here we use the dictionaries's get methode
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())


submit_btn = ttk.Button(win, text='Submit',command=submit)
submit_btn.grid(row=1,columnspan=2)


# methode for padding: here we give padding to our labels,entrybox,buttons etc.
for child in label_frame.winfo_children():      # this winfo_children function give us list of widget and after that we can apply padding to hole windo widgets.
    child.grid_configure(padx=6,pady=6)

win.mainloop()  