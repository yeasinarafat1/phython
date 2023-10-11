from tkinter import *
from PIL import Image, ImageTk
mahmudul_root = Tk()
mahmudul_root.geometry("1024x750")
image = Image.open("tk.jpg")
photo = ImageTk.PhotoImage(image)
varun_label = Label(image=photo)
varun_label.pack()
mahmudul_root.mainloop()