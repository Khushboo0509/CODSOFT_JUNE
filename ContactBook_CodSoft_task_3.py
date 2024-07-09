from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter import ttk
contacts = {}

# Function to add contact
def add_contact():
    name = name_entry.get()
    phone = phone_num_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    # Check if name and phone number are provided
    if name and phone:
        # Check if phone number contains only digits
        if phone.isdigit():
            # Check if email contains "@gmail"
            if "@gmail" in email:
                contacts[name] = {'phone': phone, 'email': email, 'address': address}
                update_listbox()
                clear_entries()
            else:
                messagebox.showwarning("Invalid Email", "Email must contain '@gmail'")
        else:
            messagebox.showwarning("Invalid Phone Number", "Phone number must contain only digits")
    else:
        messagebox.showwarning("Input Error", "Name and Phone Number are required")

# Function to update contact listbox
def update_listbox():
    for item in listbox.get_children():
        listbox.delete(item)
    for name, info in contacts.items():
        listbox.insert("", "end", values=(name, info['phone'], info['email'], info['address']))

# Function to clear entry boxes
def clear_entries():
    name_entry.delete(0, END)
    phone_num_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

# Function for search contact
def search_contact():
    search_term = entry_search.get().lower().strip()
    if not search_term:
        messagebox.showwarning("Warning", "Please enter Phone number or Name")
        return
    for item in listbox.get_children():
        listbox.delete(item)
    found = False
    for name, info in contacts.items():
        display_values = (name, info['phone'], info['email'], info['address'])

        # Check if the search term matches the name or phone number
        if search_term in name.lower() or search_term in info['phone'].lower():
            listbox.insert("", "end", values=display_values, tags=('found',))
            found = True
        else:
            listbox.insert("", "end", values=display_values)
    if not found:
        messagebox.showwarning("Warning", "Contact not found")
    listbox.tag_configure('found', background='green')

# Function for update contacts
def update_contact():
    # Ask the user which contact to update
    contact_name = simpledialog.askstring("Select Contact", "Which contact would you like to update?")
    
    if contact_name in contacts:
        confirm = messagebox.askyesno("Confirm Update", f"Do you want to update the contact: {contact_name}?")
        
        if confirm:
            name_entry.delete(0, END)
            phone_num_entry.delete(0,END)
            email_entry.delete(0,END)
            address_entry.delete(0,END)
            
            name_entry.insert(END, contact_name)
            phone_num_entry.insert(END, contacts[contact_name]['phone'])
            email_entry.insert(END, contacts[contact_name]['email'])
            address_entry.insert(END, contacts[contact_name]['address'])
            
            del contacts[contact_name]
    else:
        messagebox.showerror("Error","Contact not found")

# Function to delete contact
def delete_contact():
    selected_task = listbox.selection()
    if selected_task:
        selected_contact = listbox.item(selected_task)
        name = selected_contact['values'][0]
        del contacts[name]
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning!!", "Select a contact to delete")

# Create Window
win = Tk()
win.title("CONTACT LIST")
win.geometry("605x600+400+30")
win.resizable(False, False)

# Navigation bar
frame1 = Frame(win, width=620, height=100, bg="#004AAD")
frame1.grid(row=0, column=0, padx=0, pady=0)

# Heading
Label(frame1, text="CONTACT BOOK", font=("Courier", 27, "bold"), bg="#004AAD").place(x=175, y=20)

# Contact list label
Label(win, text="Contact List", font=("Courier", 20, "bold")).place(x=200, y=100)

# Frame for the listbox
frame2 = Frame(win, width=550, height=200, bg="#004AAD")
frame2.place(x=30, y=135)

# Scrollbar for the listbox
scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=Y)

# heading for listbox contacts
columns = ("name", "phone", "email", "address")
listbox = ttk.Treeview(frame2, columns=columns, show='headings', yscrollcommand=scrollbar.set)

# Define headings
listbox.heading("name", text="Name")
listbox.heading("phone", text="Phone Number")
listbox.heading("email", text="Email")
listbox.heading("address", text="Address")

# Adjust column widths
listbox.column("name", width=150)
listbox.column("phone", width=100)
listbox.column("email", width=150)
listbox.column("address", width=150)

# Pack the treeview widget
listbox.pack(fill=BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Entry Box labels
name_label = Label(win, text="Name", font=("Courier", 15, "bold")).place(x=50, y=385)
phone_num_label = Label(win, text="Phone Number", font=("Courier", 15, "bold")).place(x=50, y=415)
email_label = Label(win, text="Email", font=("Courier", 15, "bold")).place(x=50, y=445)
address_label = Label(win, text="Address", font=("Courier", 15, "bold")).place(x=50, y=475)

# Entry boxes
name_entry = Entry(win, borderwidth=1, relief="solid")
name_entry.place(x=200, y=390)
phone_num_entry = Entry(win, borderwidth=1, relief="solid")
phone_num_entry.place(x=200, y=420)
email_entry = Entry(win, borderwidth=1, relief="solid")
email_entry.place(x=200, y=450)
address_entry = Entry(win, borderwidth=1, relief="solid")
address_entry.place(x=200, y=480)

# Add button
btn_add = Button(win, text="Add Contact", font="arial 14 bold", width=10, bg="#0b4485", fg="#fff", bd=0, borderwidth=1, relief="raised", command=add_contact)
btn_add.place(x=415, y=390)

# Frame for Searching Contact
frame_search = Frame(win).place(x=370, y=440)
label_search = Label(frame_search, text="Search by Name or Phone", font="arial 12 bold", width=22)
label_search.place(x=370, y=440)
entry_search = Entry(frame_search, width=25)
entry_search.place(x=410, y=470)

# Search button
btn_search = Button(frame_search, text="Search", font="arial 14 bold", width=7, bg="#0b4485", fg="#fff", bd=0, borderwidth=1, relief="raised", command=search_contact)
btn_search.place(x=440, y=500)

# Update Button
btn_update = Button(win, text="Update", font="arial 14 bold", width=10, bg="#0b4485", fg="#fff", bd=0, borderwidth=1, relief="raised", command=update_contact)
btn_update.place(x=420, y=550)

# Delete button
btn_delete = Button(win, text="Delete", font="arial 14 bold", width=10, bg="red", fg="#fff", bd=0, borderwidth=1, relief="raised", command=delete_contact)
btn_delete.place(x=200, y=550)

win.mainloop()
