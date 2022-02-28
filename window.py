"""Header Files That We Are Using"""
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import cv2
import pyzbar.pyzbar as pyzbar
import qrcode
import PIL.Image
import pyqrcode


"""Opening the logo image for the QR code"""
logo = PIL.Image.open('logo.png')



"""Function to Decode the QR"""
def scanQR():
   i = 0
   vid = cv2.VideoCapture(0) #Access The Webcam
   while i<2: #Infinite Loop until Valid QR code is found
       _,f = vid.read()
       decoded = pyzbar.decode(f)
       for obj in decoded:
           lbl.config(text=f'{obj.data}',font =("Impact font", 10,"bold italic",),bg='#EE8305')
           i += 1
       cv2.imshow('QRCode',f)
       cv2.waitKey(5)
       cv2.destroyAllWindows


"""Main Function to Desgin and Generate the QRcode"""
def generate_QR():
    if len(user_input.get())!=0 : #Making Sure Input was taken in Entry Box 
        global qr,img
        qr = pyqrcode.create(user_input.get()) #Generating QRcode Using Built-in Function
        img = BitmapImage(data = qr.xbm(scale=14)) #Scaling it to show it in the GUI Window
        qr.png(f'{file_name.get()}.png',scale = 8,module_color= modulecolor, background= bgcolor) #Saving The QR code with custom background and module color
        Label(window, text='File Saved!', fg='red').pack()
        if logo_button.get() == 1: 
            addLogo()
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass


def addLogo(): #Function for the addition of the logo image
    global logo
    basic = 100
    width_percentage = (basic/float(logo.size[0]))
    height_size = int((float(logo.size[1])*float(width_percentage)))
    logo = logo.resize((basic, height_size), PIL.Image.ANTIALIAS)
    qrc = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qrc.add_data(user_input.get())
    qrc.make()
    gen_img = qrc.make_image(
        fill_color=modulecolor, 
        bg_color=bgcolor,
        ).convert('RGBA')

    position = ((gen_img.size[0] - logo.size[0]) // 2, (gen_img.size[1] - logo.size[1]) // 2)

    gen_img.paste(logo, position)
    gen_img.save(file_name.get()+'_logo.png')



def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of " + user_input.get(),font=('times', 20))


"""GUI CREATION"""

window = Tk()
window.title("QRious")
window.geometry("1200x700")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 700,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)



background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    597.0, 424.5,
    image=background_img)



img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = scanQR,
    relief = "flat")

b0.place(
    x = 573, y = 163,
    width = 294,
    height = 48)



img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = generate_QR,
    relief = "flat")

b1.place(
    x = 737, y = 600,
    width = 294,
    height = 48)



img2 = PhotoImage(file = f"img2.png")

def color1(): #Function to choose the module color
    global modulecolor
    modulecolor = colorchooser.askcolor()[1]

b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = color1,
    relief = "flat")

b2.place(
    x = 900, y = 383,
    width = 210,
    height = 48)



def color(): #Function to choose the background color
    global bgcolor
    bgcolor = colorchooser.askcolor()[1]

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = color,
    relief = "flat")

b3.place(
    x = 635, y = 383,
    width = 232,
    height = 48)



img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = generate_QR,
    relief = "flat")

b4.place(
    x = 894, y = 163,
    width = 294,
    height = 48)



entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    878.0, 517.0,
    image = entry0_img)

file_name = StringVar()

entry0 = Entry(
    bd = 0,
    bg = "#e8e8e8",
    textvariable = file_name,
    highlightthickness = 0)

entry0.place(
    x = 789.0, y = 493,
    width = 178.0,
    height = 46)



entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    884.0, 297.0,
    image = entry1_img)

user_input = StringVar()

entry1 = Entry(
    bd = 0,
    bg = "#e8e8e8",
    textvariable = user_input,
    highlightthickness = 0)
entry1.place(
    x = 683.0, y = 273,
    width = 402.0,
    height = 46)



logo_button = IntVar()

a = Checkbutton(window, text = "Logo",
                      bg='#EE8305',
                      variable = logo_button,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      font =("Impact font", 15,"bold italic",),
)
a.place(x = 200, y = 573,)

lbl = Label(window, font=('times', 20),bg='#EE8305')
lbl.place(x = 400,y = 573)


img_lbl = Label(
    window,
    bg='#F25252')
img_lbl.place(
    x = 50, y = 100,
)

output = Label(
    window,
    text="",
    bg='#F25252'
    )
output.place(
    x = 175, y = 500,

)


window.resizable(False, False)
window.mainloop()
