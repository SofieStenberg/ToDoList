from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("A to-do list")

# A frame widget to hold the listbox and scrollbar
frameTask = Frame(window)
frameTask.pack()

# To hold items in a listbox
listboxTask = Listbox(frameTask, bg="black", fg="white", height=15, width=50, font="Times New Roman")
listboxTask.pack(side=tkinter.LEFT)

#Scrolldown in case the total list exceeds the size of the given window
scrollbarTask = Scrollbar(frameTask)
scrollbarTask.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listboxTask.config(yscrollcommand=scrollbarTask.set)
scrollbarTask.config(command=listboxTask.yview)

#Button widget 
entryButton=Button(window,text="Add task",width=50,command=entertask)
entryButton.pack(pady=3)
deleteButton=Button(window,text="Delete selected task",width=50,command=deletetask)
deleteButton.pack(pady=3)
markButton=Button(window,text="Mark as completed ",width=50,command=markcompleted)
markButton.pack(pady=3)




window.mainloop()

