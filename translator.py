from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import asyncio

def change(text ="type", src='English', dest='Hindi'):
    text1 = text.lower()
    src = src.lower()
    dest = dest.lower()
    for key, value in LANGUAGES.items():
        if src == value:
            src = key
        if dest == value:
            dest = key

    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    if asyncio.iscoroutine(trans1):
        trans1 = asyncio.run(trans1)
    return trans1.text

def data():
    s = combo_source.get()
    d = combo_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    Dest_txt.delete(1.0, END)
    Dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='black')

lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg='black', fg='white')
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root, bg='black')
frame.place(x=10, y=500, height=80, width=480)

lab_source = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), bg='black', fg='white')
lab_source.place(x=100, y=100, height=20, width=300)

Sor_txt = Text(root, font=("Times New Roman", 14), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

list_lang = ['English', 'Hindi', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Russian', 'Italian']

combo_source = ttk.Combobox(root, values=list_lang, font=("Times New Roman", 14), state='readonly')
combo_source.place(x=10, y=300, height=30, width=200)
combo_source.set('Select Language')
combo_dest = ttk.Combobox(root, values=list_lang, font=("Times New Roman", 14), state='readonly')
combo_dest.place(x=290, y=300, height=30, width=200)
combo_dest.set('Select Language')

btn_translate = Button(root, text="Translate", relief=RAISED, command = data, font=("Times New Roman", 20, "bold"), bg='blue', fg='white')
btn_translate.place(x=150, y=350, height=50, width=200)

lab_dest = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), bg='black', fg='white')
lab_dest.place(x=100, y=420, height=20, width=300)

Dest_txt = Text(root, font=("Times New Roman", 14), wrap=WORD)
Dest_txt.place(x=10, y=450, height=150, width=480)

root.mainloop()