from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class ToDo:
    def __init__(self, master):
        self.nrOfCheckbuttons = 0
        self.containerCheckbuttons = {}

        self.master = master

        self.master.bind('<Return>', lambda e: self.addItem(self.entryItem.get()))

        

        # Setting a title and background to the master window
        self.master.title('ToDo')
        self.master.configure(background='beige')
        self.master.geometry('800x300')
        self.master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('TFrame', background='beige')
        self.style.configure('TCanvas', background='beige')
        self.style.configure('TLabel', background='beige')
        self.style.configure('TButton', background='beige')
        self.style.configure('TCheckbutton', background='beige')

        # Creating a frame for the header
        self.frameHeader = ttk.Frame(self.master)
        #self.frameHeader.configure(width=800, height=50, padx=15)
        self.frameHeader.pack()

        # Configures the title
        self.title = ttk.Label(self.frameHeader, text='ToDo-List', font=('Times New Roman', 24, 'bold'))
        self.title.grid(row=0, column=0, rowspan=4, pady=30)
        
        # Configure a frame for the buttons and the Entry
        self.frameManage = ttk.Frame(self.master)#, borderwidth=2, relief=RIDGE)
        self.frameManage.pack(pady=5)
        
        ttk.Label(self.frameManage, text='Describe new item:', font=('Times New Roman', 14)).grid(row=0, column=0, sticky=SW)
        self.entryItem = ttk.Entry(self.frameManage, width=50, font=('Times New Roman', 14))
        self.entryItem.grid(row=1, column=0, padx=5)

        ttk.Button(self.frameManage, text='Add new item', command=lambda: self.addItem(self.entryItem.get())).grid(row=1, column=3, padx=5)
        ttk.Button(self.frameManage, text='Delete completed items', command=self.deleteFinished).grid(row=1, column=4, padx=5)
        ttk.Button(self.frameManage, text='Delete All', command=self.deletaAll).grid(row=1, column=5, padx=5)


        

        # Scrollbar
        self.canvasContent = Canvas(self.master, width=300, height=300, scrollregion = (0, 0, 500, 500), 
                                    background='beige')
        self.verticalScrollbar = Scrollbar(self.master, orient=VERTICAL)#, command=self.canvasContent.yview)
        self.verticalScrollbar.pack(side=RIGHT, fill=Y)
        self.verticalScrollbar.configure(command=self.canvasContent.yview)

        # Creating a frame for the content
        #self.canvasContent = Canvas(self.master, yscrollcommand=self.verticalScrollbar.set)
        self.canvasContent.configure(yscrollcommand=self.verticalScrollbar.set, width=300, height=300)
        self.canvasContent.pack(side=LEFT, expand=True, fill=BOTH, anchor=W, padx=15)
        

        # self.frameContent = ttk.Frame(self.canvasContent)
        # self.frameContent.pack(side=TOP, anchor=W, padx=15 )

        

        # Menu bar
        self.master.option_add('*tearOff', False)
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.file.add_separator()
        self.file.add_command(label='Change title', command=self.changeTitle)

        

        
        



    def addItem(self, item):
        if self.entryItem.get() == "":
            messagebox.showinfo('Missing input' ,"You have to insert an item!")
            return
        for entry in self.containerCheckbuttons.values():
            if item == entry.cget('text'):
                messagebox.showinfo('Already exists' ,"The item already exists!")
                self.entryItem.delete(0, END)  
                return
        
        self.checkbutton = ttk.Checkbutton(self.canvasContent, text=item, onvalue=1, offvalue=0)
        self.containerCheckbuttons[self.nrOfCheckbuttons] = self.checkbutton
        self.nrOfCheckbuttons = self.nrOfCheckbuttons + 1
        # This will make sure that the checkbuttons are not selected when created
        self.checkbutton.state(['!alternate'])
        self.checkbutton.pack(side=TOP, anchor=W, padx=15, pady=5)
        self.entryItem.delete(0, END)

    def deleteFinished(self):
        deletedItems = []
        for key, entry in self.containerCheckbuttons.items():
            if entry.state():
                #print(entry.cget('text'))
                entry.destroy()
                deletedItems.append(key)
        for item in deletedItems:
            if item in self.containerCheckbuttons:
                self.containerCheckbuttons.pop(item)

    def deletaAll(self):
        if len(self.containerCheckbuttons) == 0:
            messagebox.showinfo('No entries' ,"There are no entries to delete")
        for entry in self.containerCheckbuttons.values():
            entry.destroy()
        self.containerCheckbuttons.clear()

    def changeTitle(self):
        userInput = simpledialog.askstring(title='Enter new title', prompt='Enter the desired title', parent=self.master)
        self.title.configure(text=userInput)
        self.master.title(userInput)




def main():
    root = Tk()
    toDo = ToDo(root)
    root.mainloop()

if __name__ == "__main__": main()