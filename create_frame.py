import tkinter as tk


trackable_count=0

def frame_make():
    #resize window to fit
    global trackable_count
    trackable_count +=1
    root.geometry(f"600x{200+150*trackable_count}")

    #replace btn create_new
    create_new.place_configure(x=450,anchor="center",y=180+150*trackable_count)

    #create frame
    frame = tk.Frame(root,width=400,height=150, bg="blue")
    frame.place(x=300,anchor="center",y=180)
