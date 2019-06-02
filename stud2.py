import tkinter as tk
import stud as st

root = tk.Tk()
root.title("Student Management")

heading_label = tk.Label(root,font = ('arial',20,'bold'),text = "  STUDENT MANAGEMENT SYSTEM  ",
                         pady = 20,padx = 20)
heading_label.grid(row=0, column=1)


heading_label1 = tk.Label(root,font = ('arial',20,'bold'),text = "Enter student name",pady = (20),padx = (20))
heading_label1.grid(row=1, column=0)

name_field = tk.Entry(root,font = ('arial',20,'bold'))
name_field.grid(row=1, column=1)


heading_label2 = tk.Label(root,font = ('arial',20,'bold'),text = "Enter student college",pady = (20),padx = (20))
heading_label2.grid(row=2, column=0)

college_field = tk.Entry(root,font = ('arial',20,'bold'))
college_field.grid(row=2, column=1)


heading_label3 = tk.Label(root,font = ('arial',20,'bold'),text = "Enter student address",pady = (20),padx = (20))
heading_label3.grid(row=3, column=0)

address_field = tk.Entry(root,font = ('arial',20,'bold'))
address_field.grid(row=3, column=1)



heading_label4 = tk.Label(root,font = ('arial',20,'bold'),text = "Enter student phone",pady = (20),padx = (20))
heading_label4.grid(row=4, column=0)

phone_field = tk.Entry(root,font = ('arial',20,'bold'))
phone_field.grid(row=4, column=1)

def create_data():
    print("table created")
    st.create_table()

def ValueInput():
    name = name_field.get()
    college = college_field.get()
    address = address_field.get()
    phone = phone_field.get()

    st.insert_record(name,college,address,phone)
    print("data input successful")

def retrieve_record():
    print("record reviewed")
    st.display_record()


button1 = tk.Button(root, font = ('arial',20,'bold'),bd =10,text = "Create Table", command = lambda: create_data())
button1.grid(row=5, column=0,padx =50,pady= 50)

button2  = tk.Button(root,font = ('arial',20,'bold'),bd = 10, text ="Save Record",command = lambda: ValueInput() )
button2.grid(row=5, column=1)

button3 = tk.Button(root ,font = ('arial',20,'bold'),bd =10, text ="Display Record",command = lambda: retrieve_record() )
button3.grid(row=5, column=2,padx =50,pady= 50)



root.mainloop()

