from tkinter import *
from pathlib import Path
import re
import backend

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, Label, messagebox


BASE_PATH = Path(__file__).parent
ASSETS_PATH = BASE_PATH / 'assets'/ 'frame0'
id = None


# Functionss
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_mousewheel(event):
    scroll_amount = 0.1  
    table.yview_scroll(-1 * int(event.delta/120 * scroll_amount), "units")
 
 
def GetValue(event):
    global id
    
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    row_id = table.selection()[0]
    select = table.set(row_id)
    
    id = select["Id"]
    entry_1.insert(0,select['Username'])
    entry_2.insert(0,select['Password'])
    entry_3.insert(0,select['Category'])
    entry_4.insert(0,select['Comments'])
    
def Destroy():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_1.focus_set()
    
def Show():
    
    table.delete(*table.get_children())
    records = backend.Show()
    for i, (Id ,username, password, category, comments) in enumerate(records,start=1):
        table.insert("", "end", values=(Id , username, password, category, comments))

    
def Add():
    if entry_1.get() == "" or entry_2.get() == "" or entry_3.get() == "" or entry_4.get() == "":
        messagebox.showerror("ERROR", "It looks like you missed a spot! Please fill in all required fields.")
        
    else:
        backend.Add(entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get())
        Destroy()
        Show()

def Delete():
    backend.Delete(entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get())
    Destroy()
    Show()
    
def Update():
    global id
    
    backend.Update(id, entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get())
    Destroy()
    Show()
 
# Figma Tkinter Designer   
window = Tk()

window.geometry("1366x768")
window.configure(bg = "#0C4F5E")

canvas = Canvas(
    window,
    bg = "#0C4F5E",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    65.0,
    694.0,
    anchor="nw",
    text="Add",
    fill="#FFFFFF",
    font=("Lato Regular", 22 * -1)
)

canvas.create_text(
    170.0,
    694.0,
    anchor="nw",
    text="Update",
    fill="#FFFFFF",
    font=("Lato Regular", 22 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
Update_btn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Update(),
    relief="flat"
)
Update_btn.place(
    x=168.0,
    y=619.0,
    width=75.0,
    height=75.0
)

canvas.create_text(
    293.0,
    694.0,
    anchor="nw",
    text="Delete",
    fill="#FFFFFF",
    font=("Lato Regular", 22 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
Delete_btn = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Delete(),
    relief="flat"
)
Delete_btn.place(
    x=288.0,
    y=619.0,
    width=75.0,
    height=75.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
Destroy_btn = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Destroy(),
    relief="flat"
)
Destroy_btn.place(
    x=408.0,
    y=619.0,
    width=75.0,
    height=75.0
)

canvas.create_text(
    420.0,
    694.0,
    anchor="nw",
    text="Clear",
    fill="#FFFFFF",
    font=("Lato Regular", 22 * -1)
)

canvas.create_text(
    127.0,
    13.0,
    anchor="nw",
    text="BarkVault ",
    fill="#000000",
    font=("Lato Regular", 54 * -1)
)

canvas.create_text(
    130.0,
    73.0,
    anchor="nw",
    text="Guarding Your Accounts",
    fill="#000000",
    font=("Lato Regular", 30 * -1)
)

canvas.create_rectangle(
    29.0,
    119.51332092285156,
    167.0,
    139.8232479095459,
    fill="#0D505F",
    outline="")

canvas.create_text(
    28.0,
    118.0,
    anchor="nw",
    text="INFORMATION",
    fill="#000000",
    font=("Lato Regular", 20 * -1)
)

canvas.create_text(
    32.0,
    184.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Lato Regular", 22 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    323.0,
    201.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("@Microsoft JhengHei", 12)
    
)
entry_1.place(
    x=165.0,
    y=175.0,
    width=330.0,
    height=51.0
)

canvas.create_text(
    32.0,
    289.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Lato Regular", 22 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    323.0,
    306.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("@Microsoft JhengHei", 12)
)
entry_2.place(
    x=165.0,
    y=280.0,
    width=330.0,
    height=53.0
)

canvas.create_text(
    32.0,
    394.0,
    anchor="nw",
    text="Category",
    fill="#000000",
    font=("Lato Regular", 22 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    323.0,
    411.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("@Microsoft JhengHei", 12)
)
entry_3.place(
    x=165.0,
    y=385.0,
    width=330.0,
    height=53.0
)

canvas.create_text(
    32.0,
    499.0,
    anchor="nw",
    text="Comments",
    fill="#000000",
    font=("Lato Regular", 22 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    323.0,
    516.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("@Microsoft JhengHei", 12)
)
entry_4.place(
    x=165.0,
    y=490.0,
    width=330.0,
    height=53.0
)

canvas.create_rectangle(
    550.0,
    122.11199951171875,
    626.0,
    136.33599948883057,
    fill="#0D505F",
    outline="")

canvas.create_text(
    549.6427612304688,
    117.0,
    anchor="nw",
    text="SEARCH",
    fill="#000000",
    font=("Lato Regular", 20 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    66.0,
    57.0,
    image=image_image_1
)



button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
Add_btn = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Add(),
    relief="flat"
)
Add_btn.place(
    x=48.0,
    y=619.0,
    width=75.0,
    height=75.0
)

canvas.create_rectangle(
    632.0000026462928,
    129.2527618408203,
    1347.0003509521484,
    130.99722569140675,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    1345.0,
    130.0,
    1347.0,
    748.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    520.0,
    747.0,
    1347.0,
    749.0000000000001,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    520.0,
    129.0,
    522.0,
    748.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    522.0,
    129.0,
    548.5,
    131.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    166.0,
    129.0,
    514.9999389648438,
    131.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    513.0,
    130.0,
    515.0000000000001,
    580.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    16.0,
    579.0,
    515.0,
    581.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    16.0,
    747.0,
    515.0,
    749.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    16.0,
    586.0,
    515.0,
    588.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    16.0,
    129.0,
    18.0,
    580.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    16.0,
    129.0,
    28.0,
    131.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    16.0,
    586.0,
    18.0,
    748.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    513.0,
    586.0,
    515.0005049948254,
    748.0,
    fill="#FFFFFF",
    outline="")

# Table Creation
table_headings = ["Id", "Username", "Password", "Category", "Comments"]

style = ttk.Style()
style.theme_use("clam")  # Choose a ttk theme

table = ttk.Treeview(master=window, columns= table_headings, show = "headings")

for column in table_headings:
    if column == "Id":
        table.heading(column, text = column)
        table.column(column, width = 0, anchor ="center")
    elif column == "Category":
        table.heading(column, text = column)
        table.column(column, width = 25, anchor ="center")
    elif column == "Comments":
        table.heading(column, text = column)
        table.column(column, width = 75, anchor ="center")
    else:
        table.heading(column, text = column)
        table.column(column, width = 175, anchor ="center")

#Headding
style.configure("Treeview.Heading", background="#0A4755", fieldbackground="black", font=("@Malgun Gothic", 15))
style.map("Treeview.Heading", foreground=[("!active", "white"), ("active", "#0A4755")])       

#Rows
style.configure("Treeview", background = "#157E96", fieldbackground = "#116E83",font=("@Malgun Gothic Semilight", 11), rowheight=25)

style.map("Treeview", background=[('selected', '#0A4755')])


table.place(x=532.5, y=147.5, width=800,height=585)


table.bind('<Double-Button-1>',GetValue)
table.bind("<MouseWheel>", on_mousewheel)

Show()
window.resizable(False, False)
window.mainloop()
