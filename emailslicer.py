import tkinter as tk
from tkinter import *

window = tk.Tk()

window.geometry("650x650")
window.config(bg="blue")
window.resizable(width=False, height=False)
window.title("Simple Email Slicer")


def result():
    try:
        email = entry.get()
        inp_email = email.strip()
        username = inp_email[0:inp_email.index("@")]
        domain = inp_email[inp_email.index("@")+1:]
        text_box.delete("1.0", tk.END)
        msg = "Email entered was: {}\nYour email username is {}\nAnd your email domain server is {}"
        msg_formatted = msg.format(email, username, domain)
        text_box.insert(tk.END, msg_formatted)
        entry.delete(0, "end")
    except:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, "ERROR!")


def reset_all():
    text_box.delete("1.0", tk.END)
    entry.delete(0, "end")


start = Label(text="Welcome to our Email Slicer", font=12, foreground="white", background="black")
Info = Label(text="Enter your email ID click the done button!\n The application will extract your username and domain "
                  "name.", foreground="white", background="blue", font=10)
emailId = Label(foreground="white", font=10, background="black", text="Enter Your Email Id: ")
result_label = Label(font=10, foreground="white", background="black", text="The results are as follows: ")
empty_label = Label(background="blue")
empty_label1 = Label(background="blue")
empty_label2 = Label(background="blue")
empty_label3 = Label(background="blue")
empty_label4 = Label(background="blue")
empty_label5 = Label(background="blue")

e1 = StringVar()
entry = Entry(font=11, width=50, justify="center", textvariable=e1)

btn = Button(text="Slice", font=11, bg="red", command=result)
reset = Button(text="Reset", font=11, bg="red", command=reset_all)

text_box = Text(height=5, width=40)

empty_label.pack()
start.pack()
Info.pack()
empty_label1.pack()
emailId.pack()
empty_label4.pack()
entry.pack()
empty_label2.pack()
btn.pack()
empty_label5.pack()
reset.pack()
empty_label3.pack()
result_label.pack()
text_box.pack()

window.mainloop()
