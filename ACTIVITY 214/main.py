#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.wm_title("Authorization")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")
lbl_username = tk.Label(frame_login, text='Username:', font="{Comic Sans MS}")
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_passwd = tk.Label(frame_login, text='Password:', font="{Comic Sans MS}")
lbl_passwd.pack()

ent_passwd = tk.Entry(frame_login, show="*", bd=3)
ent_passwd.pack(pady=5)

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

def testbutton():
    frame_auth.tkraise()

btn_login = tk.Button(frame_login, text="Login", font="{Comic Sans MS}", command=testbutton)
btn_login.pack(pady=5)

frame_login.tkraise()

root.mainloop()