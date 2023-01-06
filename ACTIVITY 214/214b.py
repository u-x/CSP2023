import tkinter as tk

root = tk.Tk()

rootw = 300
rooth = 300

root.wm_geometry(str(rootw) + "x" + str(rooth))

root.title("color four square")

bluew = rootw * (2/3)
blueh = rooth * (1/2)
greenw = rootw * (1/3)
greenh = rooth * (1/2)
redw = rootw * (2/3)
redh = rooth * (1/2)
yelloww = rootw * (1/3)
yellowh = rooth * (1/2)

blue_frame = tk.Frame(root, background="#1332FF", width=bluew, height=blueh)
blue_frame.grid(row=0, column=0, sticky="news")

green_frame = tk.Frame(root, background="#0EFA00", width=greenw, height=greenh)
green_frame.grid(row=0, column=1, sticky="news")

red_frame = tk.Frame(root, background="#FE2F00", width=redw, height=redh)
red_frame.grid(row=1, column=0, sticky="news")

yellow_frame = tk.Frame(root, background="#FEFB00", width=yelloww, height=yellowh)
yellow_frame.grid(row=1, column=1, sticky="news")

scalevar = tk.IntVar()
firstwidg = tk.Scale(root, orient='horizontal', variable=scalevar)
firstwidg.grid(row=0, column=0)

scalelabel = tk.Label(text=str(scalevar.get()))
scalelabel.grid(row=0, column=0, sticky=tk.S)

def updatescale(a,b,c):
    scalelabel.config(text=str(scalevar.get()))

secondwidg = tk.Label(root, text="insert extremely original widget here")
secondwidg.grid(row=1, column=0)

thirdwidg = tk.Radiobutton(root, text="horizontal")
thirdwidg.grid(row=0, column=1)

ok = tk.StringVar()
fourthwidg = tk.Entry(root, textvariable=ok)
fourthwidg.grid(row=1, column=1)

scalevar.trace("w", updatescale)

root.mainloop()