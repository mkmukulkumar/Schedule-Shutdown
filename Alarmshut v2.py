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
    os.system("shutdown")	
  
# def po(event) :
# 	print("hi")
def abort(event):
	os.system("shutdown /a")
#selection of min or second
root=tkinter.Tk()
root.title("Shutdown")
root.geometry("400x200")
root.configure(background="grey")

mylabel=tkinter.Label(root, text="Time to shutdown (min)",
						fg="white",bg="grey",
						font="Times 24",
						anchor="w")
mylabel.pack()



txtbox=tkinter.Entry(root,width=20,fg="green",font="Arial 20")
txtbox.bind("<Return>",shut)
txtbox.pack()

# timer=tkinter.Label(root, text="00:00:00",bd=2, fg="green",anchor="s")
# timer.pack()

#button=tkinter.Button(root, text="Shutdown", command=shut(txtbox.get()))
button=tkinter.Button(root, text="Shutdown",font="bold",border="5")
button.bind("<Button-1>",shut)
button.pack()
#button.grid(row=3,column=0)

butt=tkinter.Button(root, text="Abort",fg="red",font="bold",border="5",)
butt.bind("<Button-1>",abort)
#butt.grid(row=3,column=1)
butt.pack()

# butt=Button(root, text-"Abort")



root.mainloop()
