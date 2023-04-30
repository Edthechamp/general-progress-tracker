import tkinter as tk

root = tk.Tk()
trackable_count = 0
root.title("General Progress Tracker")
root.geometry("600x200")
root.resizable(False,False)

welcome = tk.Label(root,text="Welcome to the app \n select a trackable or create a new one!",font=("Arial",25))
welcome.place(x=300,y=40,anchor="center")



def frame_make():
    #resize window to fit
    global trackable_count

    # create frame
    frame = tk.Frame(root, width=400, height=150, bg="blue")
    frame.place(x=300, anchor="center", y=180 + trackable_count*180)

    trackable_count +=1
    root.geometry(f"600x{200+170*trackable_count}")

    #replace btn create_new
    create_new.place_configure(x=450,anchor="center",y=180+170*trackable_count)



create_new = tk.Button(root,text="create new trackable",command=frame_make)
create_new.place(x=450,y=180,anchor="center")

# Run the window
root.mainloop()
