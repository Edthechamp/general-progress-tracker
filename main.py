import tkinter as tk

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
    global trackable_count

    # create frame
    frame = tk.Frame(canvas, width=400, height=150, bg="blue")
    canvas.create_window(300,180+trackable_count*180,window=frame)

    trackable_count +=1
    if trackable_count <=4:
        # resize window to fit
        root.geometry(f"600x{200+170*trackable_count}")

    btn_height= 180+170*trackable_count
    print(btn_height)
    canvas.moveto("create_new",450,btn_height)


create_new = tk.Button(canvas,text="create new trackable",command=frame_make)
canvas.create_window(450,180,window=create_new)
# Run the window
root.mainloop()
