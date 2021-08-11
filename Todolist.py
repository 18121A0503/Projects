from tkinter import *
from tkinter import messagebox
tl=[]
c=1
def inputError():
    if e1.get()=="":
        messagebox.showerror("Input Error")
        return 0
    return 1
def clear():
    taskNumberField.delete(0.0,END)
def clearfield():
    e1.delete(0,END)
def insertTask():
    global c
     

    value = inputError()
 
    
    if value == 0 :
        return
 
    
    content = e1.get() + "\n"
 
    
    tl.append(content)
 
    
    TextArea.insert('end -1 chars', "[ " + str(c) + " ] " + content)
 
    
    c += 1
 

    clearfield()

def delete() :
     
    global c
     

    if len(tl) == 0 :
        messagebox.showerror("No task")
        return
 
    number = taskNumberField.get(1.0, END)
 
    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)
 
    clearfield()
     
    tl.pop(task_no - 1)
 
    c -= 1
     
    TextArea.delete(1.0, END)
 
    for i in range(len(tl)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tl[i])
     

r=Tk()
r.configure(background="light green")
r.title("Todo list")
r.geometry("500x600")
e=Label(r,text="Enter the task",bg="green")
e1=Entry(r)
Submit=Button(r,text="Submit",fg="Black",bg="Red",command=insertTask)
TextArea=Text(r,height=5,width=25,font="lucida 13")
taskNumber = Label(r, text = "Delete Task Number", bg = "blue")
taskNumberField = Text(r, height = 1, width = 2, font = "lucida 13")
delete=Button(r,text="Delete",fg="Black",bg="Red",command=delete)
Exit=Button(r,text="Exit",fg="Black",bg="Red",command=exit)
e.grid(row=0,column=2)
e1.grid(row=1,column=2,ipadx=50)
Submit.grid(row=2,column=2)
TextArea.grid(row=3,column=2,padx=10,sticky=W)
taskNumber.grid(row=4,column=2,pady=5)
taskNumberField.grid(row = 5, column = 2)
delete.grid(row = 6, column = 2, pady = 5)
Exit.grid(row = 7, column = 2)
r.mainloop()
