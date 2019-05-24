import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.mainframe=tk.Canvas(width=480,height=320,bg='green')
        self.mainframe.place(x=10,y=10)
        self.mainselect=tk.Listbox(width=12,height=29)
        self.all=tk.Listbox(width=12,height=29)
        self.mainselect.insert(1,'first')
        self.mainselect.insert(2, 'second')
        self.mainselect.place(x=500,y=10)
        self.all.place(x=640,y=10)
        self.leftbutt=tk.Button(text='<<',width=1,height=1)
        self.rightbutt=tk.Button(text='>>',width=1,height=1)
        self.leftbutt.place(x=602,rely=0.45)
        self.rightbutt.place(x=602,rely=0.55)
    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
root.resizable(False,False)
root.geometry('750x480')
app = Application(master=root)
app.mainloop()
