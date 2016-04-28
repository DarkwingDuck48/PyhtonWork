import random
import tkinter


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
count = 0
def game_yes():
    count = 0
    koloda = random.shuffle(cards)
    k=koloda.pop()
    result.configure()
    if count>21:
        result.configure(text="У вас " + count + " очков и это ПЕРЕБОР!!!")


root = tkinter.Tk()
root.title("BlackJack")
# root.geometry('600x400')
frame = tkinter.Frame(root)
frame.pack()

label_1 = tkinter.Label(frame, text='Добро пожаловать в игру "Очко"! ')
label_1.grid(row=0, column=0)
label_2 = tkinter.Label(frame, text='Начать игру?')
label_2.grid(row=2, column=0)

but1=tkinter.Button(frame,text="YES!!",command=game_yes)
but1.grid(row=3,column=0)
result = tkinter.Label(frame,text="")
root.mainloop()