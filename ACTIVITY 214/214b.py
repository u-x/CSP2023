import tkinter as tk

root = tk.Tk()

root.wm_geometry("200x200")

blue_frame = tk.Frame(root, background="#0000FF", width=125, height=100)
blue_frame.grid(row=0, column=0, sticky="news")

green_frame = tk.Frame(root, background="#00FF00", width=125, height=100)
green_frame.grid(row=0, column=1, sticky="news")

red_frame = tk.Frame(root, background="#FF0000", width=125, height=100)
red_frame.grid(row=1, column=0, sticky="news")

yellow_frame = tk.Frame(root, background="#FFFF00", width=100, height=150)
yellow_frame.grid(row=1, column=1, sticky="news")

root.mainloop()