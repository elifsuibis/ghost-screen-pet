# by Elif Su İbiş 17.12.2025
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.config(bg='#ffcbdb')
root.wm_attributes('-transparentcolor', '#ffcbdb')


img_normal = ImageTk.PhotoImage(Image.open("duz.png").resize((150, 150)))
img_left = ImageTk.PhotoImage(Image.open("sola.png").resize((150, 150)))
img_right = ImageTk.PhotoImage(Image.open("saga.png").resize((150, 150)))

label = tk.Label(root, image=img_normal, bg='#ffcbdb', bd=0)
label.pack()

def start(event):
    root.start_x = event.x
    root.start_y = event.y
    root.orig_x = root.winfo_x()  
    root.orig_y = root.winfo_y()  
def drag(event):
    deltax = event.x - root.start_x
    deltay = event.y - root.start_y
    new_x = root.winfo_x() + deltax
    new_y = root.winfo_y() + deltay
    root.geometry(f"+{new_x}+{new_y}")
    
    if new_x > root.orig_x:
        label.config(image=img_right) 
    elif new_x < root.orig_x:
        label.config(image=img_left) 

def drop(event):
    label.config(image=img_normal)

def stop(event):
    root.destroy()

label.bind("<Button-1>", start)
label.bind("<B1-Motion>", drag)
label.bind("<ButtonRelease-1>", drop)
label.bind("<Button-3>", stop)

root.geometry("+1000+600")
root.mainloop()
