from tkinter import *
import math

def whereapoint ():
    try:
        x_f=float(x.get())
        y_f=float(y.get())
        if (x_f<0 and y_f<0):
            ans = "III"
        elif (x_f<0 and y_f>0):
            ans = "II"
        elif (x_f>0 and y_f>0):
            ans = "I"
        elif (x_f>0 and y_f<0):
            ans = "IV"
        canv=Canvas(root,width=100,height=100,bg='white')
        canv.create_line([0,50],[100,50])
        canv.create_line([50,0],[50,100])
        canv.create_line([50+x_f,50-y_f],[50,50],fill="red")
        canv.create_line([50+x_f,50-y_f],[50+x_f,50], fill="blue")
        canv.create_line([50+x_f,50-y_f],[50,50-y_f], fill="blue")
        canv.create_text (90,10,text = "I", font="Verdina 8", anchor='w',justify=CENTER,fill="red")
        canv.create_text (10,10,text = "II", font="Verdina 8", anchor='w',justify=CENTER,fill="red")
        canv.create_text (10,90,text = "III", font="Verdina 8", anchor='w',justify=CENTER,fill="red")
        canv.create_text (90,90,text = "IV", font="Verdina 8", anchor='w',justify=CENTER,fill="red")
        canv.pack()
    except ValueError:
        ans="Error"
    except:
        ans = "?"
    ans_label.configure(text=ans)
root = Tk()
root.title("Where a point?")
frame = Frame (root)
frame.pack()

x_label = Label(frame,text="X")
x_label.grid (row=0,column=0)
x = Entry (frame,width=10)
x.grid (row=0,column=1)

y_label = Label(frame,text="Y")
y_label.grid (row=1,column=0)
y = Entry (frame,width=10)
y.grid (row=1,column=1)

button1 = Button (frame,text="Point",width=10,command=whereapoint)
button1.grid (row=2,column=1)

button2 = Button (frame,text="Clear",width = 10,command=root.destroy)
button2.grid (row=2,column=3)
ans_label = Label(frame,text = "?")
ans_label.grid (row=3,column=0)
root.mainloop()


