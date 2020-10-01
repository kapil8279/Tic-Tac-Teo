#this is contribution
from tkinter import *
from tkinter import  messagebox
prev = ''
value = ''
play_1 : list
play_2 :list
def func(x):
    global prev
    global value
    color = ''
    if prev == '' or prev == 'O':
        value = 'X'
        prev = 'X'
        color = 'red'
    else:
        value = 'O'
        prev = 'O'
        color = 'blue'
    
    if x['text'] == '':
        x.config(text = value,background = color,state = 'disable',fg = 'green')
    result()
def update():
    global value
    value = ''
    btn= 0
    for x in range(3):
        for y in range(3):
            button[btn].config(text = value,background = 'SystemButtonFace',state = 'normal')
            btn+=1
def result():
    button = [[btn1,btn2,btn3],[btn4,btn5,btn6],[btn7,btn8,btn9]]
    for x in range(3):
        if button[x][0]['text'] == button[x][1]['text'] and button[x][0]['text'] == button[x][2]['text'] and button[x][0]['text'] != '':
            messagebox.showinfo(message='Match found!')
            update()
    for x in range(3):
        if button[0][x]['text'] == button[1][x]['text'] and button[0][x]['text'] == button[2][x]['text'] and button[0][x]['text'] != '':
            messagebox.showinfo(message='Match found!')
            update()
    if button[0][0]['text'] == button[1][1]['text'] and button[0][0]['text'] == button[2][2]['text'] and button[0][0]['text'] != '':
        messagebox.showinfo(message='Match found!')
        update()
    if button[0][2]['text'] == button[1][1]['text'] and button[0][2]['text'] == button[2][0]['text'] and button[0][2]['text'] != '':
        messagebox.showinfo(message='Match found!')
        update()
root = Tk()
root.title('Tic Tac game')
frame = Frame(root)
btn1 = Button(frame,text = value,font = ('normal',15),height= 4,width = 8,command =lambda:func(btn1))
btn2 = Button(frame,text = value,font = ('normal',15),height= 4,width = 8,command =lambda:func(btn2))
btn3 = Button(frame,text = value,font = ('normal',15),height= 4,width = 8,command =lambda:func(btn3))
btn4 = Button(frame,text = value,font = ('normal',15),height= 4,width = 8,command =lambda:func(btn4))
btn5 = Button(frame,text = value,font = ('normal',15),height= 4,width = 8,command =lambda:func(btn5))
btn6 = Button(frame,text = value,font = ('normal',15),height= 4,width = 8,command =lambda:func(btn6))
btn7 = Button(frame,text = value,font = ('normal',15),height= 4,width = 8,command =lambda:func(btn7))
btn8 = Button(frame,text = value,font = ('normal',15),height= 4,width = 8,command =lambda:func(btn8))
btn9 = Button(frame,text = value,font = ('normal',15),height= 4,width = 8,command =lambda:func(btn9))
refresh = Button(frame,text = 'Refresh',font = ('normal',15),height= 4,width = 8,command =lambda:update())
ext = Button(frame,text = 'Exit',font = ('normal',15),height= 4,width = 8,command =lambda:root.destroy())
button = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
btn = 0
for x in range(3):
    for y in range(3):
         button[btn].grid(row = x,column = y)
         btn+=1
frame.pack()
refresh.grid(row = 3,column = 1)
ext.grid(row = 3,column = 2)
root.mainloop()
