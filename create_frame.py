import tkinter as tk
from tkinter.colorchooser import askcolor

trackable_label = ""
chosen_color = ""
label_got = False
hex_color = "#ADD8E6"
def when_run():
    global hex_color
    hex_color = "#ADD8E6"
    label_got = False
    root2 = tk.Toplevel()
    root2.title("Create New Trackable")
    root2.geometry("300x150")

    trackable_name = tk.Entry(root2)
    def Submit():
        global label_got
        global trackable_label
        if label_got == False:
            print("got label from submit")
            trackable_label = trackable_name.get()
        label_got = False
        root2.quit()
        root2.destroy()

    def label_chosen(event):
        global trackable_label
        global label_got
        label_got= False

        if label_got == False:
            print("got label from enter press")
            trackable_label = trackable_name.get()
            label_got=True

        name_label = tk.Label(root2,text=f"Trackable name:{trackable_name.get()}")
        name_label.place(x=160,y=60,anchor="center")
        trackable_name.delete(0, tk.END)

    trackable_entry_instruc = tk.Label(root2,text="Enter the name of the trackable!",font=("Arial",14))
    trackable_entry_instruc.place(x=160,y=20,anchor="center")

    def color_chooser():
        global hex_color
        rgb_color, hex_color = askcolor(title="Choose the color for this trackable!")

    activate = tk.Button(root2,text="choose a color for\nthis trackable!",command=color_chooser)
    activate.place(x=80,y=110,anchor="center")

    done =tk.Button(root2,text="Done",command=Submit)
    done.place(x=260,y=110,anchor="center")

    trackable_name.place(x=160,y=43,anchor="center")
    root2.bind('<Return>', label_chosen)
    root2.mainloop()

