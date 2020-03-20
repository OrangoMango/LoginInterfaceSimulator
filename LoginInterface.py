from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3, os

class App():
    def __init__(self):
        self.tk = Tk()
        self.tk.title("OrangoMango Password Interface")
        self.items = []
        self.texts = ["Insert name: ", "Insert password: "]
        for x in range(2):
            l = Label(self.tk, text=self.texts[x])
            l.grid(column=0, row=x, sticky="w")
            if x == 1:
                e = Entry(self.tk, show="*")
            else:
                e = Entry(self.tk)
            e.grid(column=1, row=x)
            self.items.append([l, e])
        def sh():
            if self.items[1][1]["show"] == "*":
               self.items[1][1]["show"] = ""
            else:
               self.items[1][1]["show"] = "*"
        sb = Checkbutton(self.tk, text="Mostra", command=sh)
        sb.grid(column=2, row=1)
        b = Button(self.tk, text="OK", command=self.ok)
        b.grid(column=2, row=4, sticky="e")
        b2 = Button(self.tk, text="Cancel", command=self.tk.destroy)
        b2.grid(column=3, row=4)
        b3 = Button(self.tk, text="SIGN-UP", command=self.signup)
        b3.grid(column=4, row=4)
        self.var = IntVar()
        self.var.set(0)
        c = Checkbutton(self.tk, variable=self.var, text="Accept privacy thermmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmms")
        c.grid(row=3)
    def ok(self):   
        a = filedialog.askopenfilename(filetypes = [("sqlite3 database (*.db)", ("*.db"))])
        connection = sqlite3.connect(a)
        cursor = connection.cursor()
        sql = "SELECT * FROM data"
        try:
            cursor.execute(sql)
        except:
            messagebox.showerror("Error", "An error occured")
            sys.exit()
        data = []
        for dt in cursor:
            data.append(dt)
        self.user = self.items[0][1].get()
        self.password = self.items[1][1].get()
        c, d = self.user == data[0][0], self.password == data[0][1]
        print(c, d)
        if (not c) and (not d):
            return
        if not self.var.get():
            messagebox.showerror("Errore", "Please accept privacy! PS: Is just fun :P")
            return
        if c and d:
            print("User: {0}, Password: {1}, Privacy: {2}".format(self.user, self.password, self.var.get()))
            messagebox.showinfo("Info", "Access succesfully done")
        else:
            messagebox.showinfo("Info", "Username or password incorrect")
    def mainloop(self):
        self.tk.mainloop()
    def signup(self):
        self.tk.destroy()
        self.tk = Tk()
        self.tk.title("OrangoMango Password Interface")
        introl = Label(self.tk, text="WELCOME")
        introl.grid(column=0, row=0)
        self.items2 = []
        self.texts = ["Insert name: ", "Insert password: "]
        for x in range(2):
            l = Label(self.tk, text=self.texts[x])
            l.grid(column=0, row=x+1, sticky="w")
            if x == 1:
                e = Entry(self.tk, show="*")
            else:
                e = Entry(self.tk)
            e.grid(column=1, row=x+1)
            self.items2.append([l, e])
        def save():
            a = filedialog.asksaveasfilename(filetypes=[("sqlite3 database (*.db)", ("*.db"))])
            #print(a)
            if os.path.exists(a):
                os.remove(a)
            connection = sqlite3.connect(a)
            cursor = connection.cursor()
            sql = "CREATE TABLE data(name TEXT, password TEXT)"
            cursor.execute(sql)
            sql = "INSERT INTO data VALUES(?, ?)"
            cursor.execute(sql, (self.items2[0][1].get(), self.items2[1][1].get()))
            connection.commit()
            sql = "SELECT * FROM data"
            cursor.execute(sql)
            connection.close()
        okb = Button(self.tk, text="OK", command=save)
        okb.grid(row=3, column=2)
        cancb = Button(self.tk, text="CANCEL", command=self.tk.destroy)
        cancb.grid(row=3, column=3)

try:
    app = App()
    app.mainloop()
except:
    messagebox.showerror("Error", "An error occured")
