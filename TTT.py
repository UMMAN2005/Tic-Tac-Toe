from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
players = ['X','O']

def quitt():
    quit()
    
check = 0
def new_turn(row,col):
    global check
    if buttons[row][col]['text'] == '':
        check+=1
    global players
    if check%2==1:
        player = players[0]
    else:
        player = players[1]
    if buttons[row][col]['text'] == '':
        buttons[row][col].config(text=player)
    elif buttons[row][col]['text'] != '':
        messagebox.showwarning('ERROR',message='This area is not free')


    window.update()
    if check_winner() != None:
        if messagebox.askretrycancel('WINNER',message=check_winner(),icon='info'):
            new_game()
        else:
            quitt()




def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] and buttons[row][0]['text'] != '':
            buttons[row][0]['bg'] = buttons[row][1]['bg'] = buttons[row][2]['bg'] = '#00FF00'
            return f"{buttons[row][0]['text']} is winner"
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] and buttons[0][col]['text'] != '':
            buttons[0][col]['bg'] = buttons[1][col]['bg'] = buttons[2][col]['bg'] = '#00FF00'
            return f"{buttons[0][col]['text']} is winner"
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] and buttons[0][0]['text'] != '':
        buttons[0][0]['bg'] = buttons[1][1]['bg'] = buttons[2][2]['bg'] = '#00FF00'
        return  f"{buttons[0][0]['text']} is winner"
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] and buttons[0][2]['text'] != '':
        buttons[0][2]['bg'] = buttons[1][1]['bg'] = buttons[2][0]['bg'] = '#00FF00'
        return f"{buttons[0][2]['text']} is winner"
    elif empty_spaces() == True:
        return 'Tie!'

def empty_spaces():
    empty_spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] !='':
                empty_spaces-=1
    if empty_spaces == 0:
        return True
    return False

def new_game():
    global check
    check = 0
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='',bg='white')

def choose_color():
    window.config(bg=colorchooser.askcolor()[1])




window = Tk()

window.geometry('500x500')
window.title('XO game')
window.config(background='yellow')


menubar = Menu(window)
window.config(menu=menubar)
FileMenu = Menu(menubar,tearoff=0,bg='#00FF00')
menubar.add_cascade(menu=FileMenu, label='File')
FileMenu.add_command(label='Reset',command=new_game)
FileMenu.add_command(label='Change color',command=choose_color)
FileMenu.add_separator()
FileMenu.add_command(label='Exit',command=quitt)

frame = Frame(window)
frame.pack()

label = Label(frame,text='XO game', bg='black',fg='white',font=('Arial',40,'bold'))
label.grid(row=0, column=0,columnspan=3)

buttons = [[0,0,0],[0,0,0],[0,0,0]]
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame,text='',bg='white',width=3,fg='black',font=('Arial',30),command=lambda row = row, col = col : new_turn(row, col))
        buttons[row][col].grid(row = row+1, column = col)




window.mainloop()
