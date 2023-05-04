import tkinter as tk

import create_frame

root = tk.Tk()
trackable_count = 0
root.title("General Progress Tracker")
root.geometry("600x200")
root.resizable(False,False)

canvas=tk.Canvas(root,bg="white",scrollregion=(0,0,20000,50000))
canvas.pack(expand= True, fill= 'both')

welcome = tk.Label(canvas,text="Welcome to the app \n select a trackable or create a new one!",font=("Arial",25))
canvas.create_window(300,40,window=welcome)

canvas.bind('<MouseWheel>',lambda event:canvas.yview_scroll(-int(event.delta/60),"units"))

def frame_make():
    global btn_id
    global trackable_count

    create_frame.when_run()
    frame_label = create_frame.trackable_label

    # create frame
    frame_bg = create_frame.hex_color
    frame = tk.LabelFrame(canvas,text=f"{frame_label}",labelanchor="n",font=("Arial",13), width=400, height=150, bg=frame_bg)
    entrybox_instruc = tk.Label(frame,font=("Arial",9),text="Enter the data for this trackable!",bg=frame_bg)
    entrybox_instruc.place(x=250,y=25,anchor="center")
    entrybox = tk.Entry(frame)
    entrybox.place(x=250,y=50,anchor="center")
    canvas.create_window(300,180+trackable_count*160,window=frame)

    trackable_count += 1
    if trackable_count <=3:
        # resize window to fit
        root.geometry(f"600x{180+160*trackable_count}")

    btn_height= 140+160*trackable_count
    canvas.moveto(btn_id,450,btn_height)


create_new = tk.Button(canvas,text="create new trackable",command=frame_make,)
btn_id=canvas.create_window(500,180,window=create_new)
# Run the window
root.mainloop()
