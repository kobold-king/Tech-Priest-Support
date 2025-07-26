from tkinter import Toplevel, Tk, Label, PhotoImage
import random


win = Tk()

win.attributes('-alpha', 0.0)
win.iconify()

window = Toplevel(win)
window.geometry("500x500+100+100")
window.overrideredirect(1)

photo = PhotoImage(file="images/mechanicus.png")

# Get current window dimensions
win.update_idletasks() # Ensure window dimensions are updated
window_width = win.winfo_width()
window_height = win.winfo_height()

# Calculate max x and y to ensure image is fully visible
max_x = window_width - resized_image.width
max_y = window_height - resized_image.height

# Generate random coordinates
random_x = random.randint(0, max_x)
random_y = random.randint(0, max_y)

label = Label(window, image=photo)
label.pack()
win.after(3000, win.destroy)
win.mainloop()
