import tkinter as tk
from PIL import Image, Imagetk
root=tk.TK()
root.title("Move with arrows")
root.geometry("800x600")
rooot.config(bg="#800080")

x_pos=350
y_pos=250

image_path="U:\Downloads\iron_man_standing_png_image_by_ongpng_dgy0taj-375w-2x-removebg-preview.png"
img_data=Image.open(image_path)
small_img=img_data.resize((100,100))
render=ImageTk.PhotoImage(small_img)

img_label= tk.Label(root,image=render)
img_label.iamge=render

img_label.place(x=x_pos,y=y_pos)

def move_image(event):
    global x_pos, y_pos

    if event.keysym == 'Up':
        y_pos -= 10
    elif event.keysym == 'Down':
        y_pos += 10
    elif event.keysym == 'Left':
        x_pos -= 10
    elif event.keysym == 'Right':
        x_pos += 10


    img_label.place(x=x_pos,y=y_pos)

root.bind("<KeyPress>", move_image)

root.mainloop()
