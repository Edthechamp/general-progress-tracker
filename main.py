import tkinter as tk

root = tk.Tk()
root.title("General Progress Tracker")
root.geometry("600x700")
root.resizable(False,True)

welcome = tk.Label(root,text="Welcome to the app \n select a trackable or create a new one!",font=("Arial",25))
welcome.place(x=300,y=40,anchor="center")

create_new = tk.Button(root,text="create new trackable")
create_new.place(x=450,y=600,anchor="center")


# Run the window
root.mainloop()
