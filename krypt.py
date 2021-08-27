from cryptography.fernet import Fernet, InvalidToken
from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter import ttk

def launch():

    def gen_key():

        def back():
            b2.destroy()
            b3.destroy()
            t1.destroy()
            lbl2.destroy()
            lbl3.destroy()
            launch()

        def copy():
            window.clipboard_clear()
            window.clipboard_append(key)
            window.update()

        key = Fernet.generate_key()
        file = open('key.key', 'wb')
        file.write(key)
        file.close()

        lbl1.destroy()
        listeCombo.destroy()
        b1.destroy()
        lbl2=Label(text='Your key', font=("bold", 25))
        lbl2.place(x=210, y=75)
        lbl3=Label(text="(A text file containing it has also been created)", font=("italic", 10))
        lbl3.place(x=140, y=115)
        tb = font.Font(size=20)
        b2=Button(text='Back', command=back)
        b2.place(x=145, y=290)
        b2['font'] = tb
        b3=Button(text='Copy', command=copy)
        b3.place(x=285, y=290)
        b3['font'] = tb
        t1=Entry(bd=2, width=55)
        t1.place(x=110, y=170)
        t1.insert(0, key)
        t1.configure(state="readonly")

    def encrypt():

        lbl1.destroy()
        listeCombo.destroy()
        b1.destroy()

        lbl4=Label(text='Encrypt', font=("bold", 25))
        lbl4.place(x=210, y=75)
        lbl5=Label(text="Enter the text you want to encrypt here", font=("italic", 10))
        lbl5.place(x=155, y=120)
        t2=Entry(bd=2, width=55)
        t2.place(x=110, y=170)
        tb = font.Font(size=18)
        b3=Button(text='Copy')
        b3.place(x=295, y=300)
        b3['font'] = tb

        def convert():
            recup = t2.get()
            input_text = recup.encode()
            file = open('key.key', 'rb')
            key = file.read()
            file.close()
            fernet = Fernet(key)

            try:
                encrypted = fernet.encrypt(input_text)
                t3=Entry(bd=2, width=55)
                t3.place(x=110, y=245)
                t3.configure(state="normal")
                t3.insert(0, encrypted)
                t3.configure(state="readonly")
                lbl6=Label(text="Result:", font=("bold", 15))
                lbl6.place(x=238, y=205)
                window.clipboard_clear()
                window.clipboard_append(encrypted)
                window.update()
            except InvalidToken as e:
                print("\nInvalid Key - Unsuccessfully encrypted")

        b2=Button(text='Convert', command=convert)
        b2.place(x=155, y=300)
        b2['font'] = tb

    def decrypt():

        lbl1.destroy()
        listeCombo.destroy()
        b1.destroy()

        lbl4=Label(text='Decrypt', font=("bold", 25))
        lbl4.place(x=210, y=75)
        lbl5=Label(text="Enter the text you want to decrypt here", font=("italic", 10))
        lbl5.place(x=155, y=120)
        t2=Entry(bd=2, width=55)
        t2.place(x=110, y=170)
        tb = font.Font(size=18)
        b3=Button(text='Copy')
        b3.place(x=285, y=300)
        b3['font'] = tb

        def convert():
            recup = t2.get()
            input_text = recup.encode()
            file = open('key.key', 'rb')
            key = file.read()
            file.close()
            fernet = Fernet(key)

            try:
                decrypted = fernet.decrypt(input_text)
                t3=Entry(bd=2, width=55)
                t3.place(x=110, y=245)
                t3.configure(state="normal")
                t3.insert(0, decrypted)
                t3.configure(state="readonly")
                lbl6=Label(text="Result:", font=("bold", 15))
                lbl6.place(x=238, y=205)
                window.clipboard_clear()
                window.clipboard_append(decrypted)
                window.update()
            except InvalidToken as e:
                print("\nInvalid Key - Unsuccessfully encrypted")

        b2=Button(text='Convert', command=convert)
        b2.place(x=145, y=300)
        b2['font'] = tb

    def action():
        listeCombo.bind("<<ComboboxSelected>>", action)
        select = listeCombo.get()
        if select == "Generate a key":
            gen_key()
        elif select == "Encrypt a text":
            encrypt()
        elif select == "Decrypt a text":
            decrypt()
        else:
            return

    tb = font.Font(size=20)
    b1=Button(text='Confirm', command=action)
    b1.place(x=215, y=290)
    b1['font'] = tb

    lbl1=Label(text='What do you want to do ?', font=("bold", 25))
    lbl1.place(x=90, y=90)

    listeActions=["Select here", "Generate a key", "Encrypt a text", "Decrypt a text"]

    listeCombo = ttk.Combobox(values=listeActions, font=(25), height = 10, width = 20)
    listeCombo.place(x=170, y=160)
    listeCombo.current(0)

window=Tk()
mywin=launch()
window.title("Krypt by Astraa")
window.geometry('550x390')
window.mainloop()