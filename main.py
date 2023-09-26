from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont


global i
global image


def add_watermark():
    global image
    global i
    width, height = image.size
    draw = ImageDraw.Draw(image)
    text = "sample watermark"
    font = ImageFont.truetype('arial.ttf', 14)
    draw.text((220, 300), text, font=font)
    i = ImageTk.PhotoImage(image)
    canvas.itemconfig(p_image, image=i)


def upload_image():
    global i
    global image
    file = askopenfilename(filetypes=[('PNG files', '*.png'), ('JPG files', '*.jpg')])
    image = Image.open(file)
    image = image.resize((round(image.size[0]*0.5), round(image.size[1]*0.5)))
    i = ImageTk.PhotoImage(image)
    canvas.itemconfig(p_image, image=i)


window = Tk()
window.configure(width=800, height=800, background='black')
canvas = Canvas(width=640, height=540)

canvas.grid(row=0, column=1, columnspan=2)
prototype = PhotoImage(file='kanye.png')
p_image = canvas.create_image(320, 270,image=prototype)
upload_button = Button(text='Upload Image', command=upload_image, width=40)
watermark_button = Button(text='add watermark',width=40, command=add_watermark)
upload_button.grid(row=1, column=0, columnspan=2)
watermark_button.grid(row=1, column=2, columnspan=2)


window.mainloop()
