import tkinter as tk

trackable_label = ""

def when_run():
    root2 = tk.Toplevel()
    root2.title("Create New Trackable")
    root2.geometry("320x150")

    trackable_name = tk.Entry(root2)
    def Submit(event):
        global trackable_label
        trackable_label = trackable_name.get()
        trackable_name.delete(0, tk.END)
        root2.quit()
        root2.destroy()


    trackable_entry_instruc = tk.Label(root2,text="Enter the name of the trackable!",font=("Arial",14))
    trackable_entry_instruc.place(x=160,y=20,anchor="center")

    trackable_name.place(x=160,y=43,anchor="center")
    root2.bind('<Return>', Submit)
    root2.mainloop()

