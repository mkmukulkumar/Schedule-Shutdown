import os 
import tkinter 
import time

def shut(event) : 
    s=txtbox.get()
    for i in range(len(s)) : 
        if s[i].isdigit() != True : 
            exit()
    print("started")
    time.sleep(int(s)*60)
    print("shutdown")	
   # os.system("shutdown -s -t " + str(tme))

def abort(event):
    os.system("shutdown /a")
    root.destroy()
    
#selection of min or second
root=tkinter.Tk()
root.title("Shutdown")
root.geometry("400x200")
root.configure(background="grey")

mylabel=tkinter.Label(root, text="Time to shutdown (min)", fg="white",bg="grey",font="Times 24",anchor="w")

mylabel.pack(pady=30)


txtbox=tkinter.Entry(root,width=20,fg="green",font="Arial 17",bd =5)
txtbox.bind("<Return>",shut)
txtbox.pack()

button=tkinter.Button(root, text="Shutdown",font="bold",border="5")
button.bind("<Button-1>",shut)
button.pack(padx=80, side="left")

butt=tkinter.Button(root, text="Abort",fg="red",font="bold",border="5")
butt.bind("<Button-1>",abort)
butt.pack( side="left")

root.mainloop()
