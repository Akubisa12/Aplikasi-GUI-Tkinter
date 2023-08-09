from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from PIL import ImageGrab

app = Tk()
# menentukan judul aplikasi
app.title('Kanvas Gambar')
# menentukan ukuran jendela aplikasi
app.geometry("600x400")
# menentukan warna pena
pena = "black"

# membuat kanvas 
canvas = Canvas(app,bg="white") # membuat awal background nya putih
canvas.pack(fill="both", expand=1) # membuat canvas menjadi full 1 jendela windows

# membuat fungsi garis 
def get_x_and_y(event): # menggunakan event karena kita akan melakukan binding 
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy, pena 
    x = canvas.create_line((lasx, lasy, event.x, event.y),fill=pena,width=4)
    lasx,lasy = event.x, event.y

# melakukan binding
canvas.bind("<Button-1>",get_x_and_y)
canvas.bind("<B1-Motion>",draw_smth)
    
# membuat fungsi untuk memilih warna background 
def pilih_bg():
    hasil = askcolor(title="Pilih warnanya")
    RGB, HEX = hasil 
    # agar bisa mewarnai 1 canvas
    canvas.config(bg=HEX)

# membuat fungsi warna pena
def pilih_pena():
    global pena 
    hasil = askcolor(title="Pilih warnanya")
    RGB, HEX = hasil 
    pena = HEX

# membuat logic tombol reset
def hapus():
    canvas.delete("all")

# membuat logic simpan
def simpan():
    data = filedialog.asksaveasfilename(defaultextension=".png")
    if data :
        x = app.winfo_rootx() + canvas.winfo_x()
        y = app.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(data)

#membuat menu bar 
# yang terdiri dari :
# A. save 
# B. reset 
# C. warna
menubar = Menu(app,tearoff=False) # submenu dalam menu menubar yang kalian buat tidak dapat dilepas menjadi jendela terpisah 
app.config(menu=menubar)
menubar.add_command(label="Save",command=simpan) 
menubar.add_command(label="Reset",command=hapus) 

file_warna = Menu(menubar)
menubar.add_cascade(label="Warna", menu=file_warna)
# membuat drop down
file_warna.add_command(label="Pena", command=pilih_pena)
file_warna.add_command(label="Background",command=pilih_bg)

app.mainloop()