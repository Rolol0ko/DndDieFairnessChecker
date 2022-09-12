from tkinter import *
import dice

root = Tk()
root.geometry("450x300")

# the label for user_name
user_name = Label(root, text = "How many rolls?").place(x = 40, y = 60)
# the label for user_password
user_password = Label(root,text = "What die?").place(x = 40,y = 100)

#Fields
user_name_input_area = Entry(root,width = 30).place(x = 150,y = 60)
user_password_input_area = Entry(root,width = 30).place(x = 150,y = 100)

#sumbit button
submit_button = Button(root,text = "Submit").place(x = 40,y = 130)

root.mainloop()