from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

# Initialize the main window
win = Tk()
win.title("TO DO LIST")
win.geometry("512x530+450+50")
win.resizable(False, False)
win.config(bg="#FEF8DD")

# ADD FUNCTION
def add_task():
    task = task_entry.get()
    selected_date = cal.get_date()
    if task != "":
        task_with_date = f"{task} (Date: {selected_date})"
        listbox.insert(END, task_with_date)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning!!", "You must enter a task")

# DELETE FUNCTION
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning!!", "Select a task to delete")

# Set the icon image
icon_image = PhotoImage(file=r"C:\Users\dell\Desktop\Tuition\logo.png")
win.iconphoto(False, icon_image)

# Navigation bar
TopImage = PhotoImage(file=r"C:\Users\dell\Desktop\Tuition\top.png")
Label(win, image=TopImage).place(x=3, y=10)

# Logo
logo1 = PhotoImage(file=r"C:\Users\dell\Desktop\Tuition\logo1.png")
Label(win, image=logo1, bg="black").place(x=100, y=25)

# Heading
Label(win, text="TASK", font=("Courier", 27, "bold"), fg="white", bg="black").place(x=215, y=20)

# Task List Label
Label(win, text="TO DO LIST", font=("Courier", 20, "bold"), bg="#FEF8DD").place(x=180, y=100)

# Frame for the listbox
frame1 = Frame(win, width=460, height=200, bg="black")
frame1.place(x=45, y=150)

# Listbox for tasks with scrollbar
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox = Listbox(frame1, font=("arial", 12), width=43, height=11, bg="black", fg="white", yscrollcommand=scrollbar.set)
listbox.pack(padx=10, pady=10, side=LEFT)

scrollbar.config(command=listbox.yview)

# Entry label
Label(win, text="TO DO", font=("Courier", 20, "bold"), bg="#FEF8DD").place(x=215, y=387)

# Frame for the entry
frame2 = Frame(win, width=375, height=36, borderwidth=1, relief="solid")
frame2.place(x=35, y=424)

# Task entry field
task_entry = Entry(frame2, width=25, font="arial 20", bd=0)
task_entry.place(x=0, y=0)

# Calendar
cal = DateEntry(frame2, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.place(x=260, y=8)

# Add Button
Add_button = Button(win,text="ADD",font="arial 14 bold", width=5, bg="#0b4485", fg="#fff", bd=0,borderwidth=1, relief="raised", command=add_task)
Add_button.place(x=408, y=423)

# Delete Button
Del_button = Button(win, text="DELETE",font="arial 14 bold" ,width=8, fg="#fff", bg="red", bd=0,borderwidth=1, relief="raised",command=delete_task)
Del_button.place(x=210, y=475)

win.mainloop()
