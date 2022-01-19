from tkinter import*
win = Tk()
win.geometry("365x650")#dimensions of the main window
win.title("Andemoli Calculator")#title of the window
win.resizable(0,0) #keeps the window size permanent

#used to get the instance of the input field
expression =""

#method for % button
def percentage():
    global expression
    expression = str(eval(f"{expression} * 100"))
    input_text.set(expression)

#a method for the square btn
def square():
    global expression
    expression = str(eval(f"{expression}**2"))
    input_text.set(expression)
   
    

#a method for the sqrt btn
def sqrt():
    global expression
    expression= str(eval(f"{expression}**0.5"))
    input_text.set(expression)
    

#a function when clicking the buttons
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#a method to handle the functionality of the clear button
def clear_btn():
    global expression
    expression = ""
    input_text.set(expression)

#method to handle the functionality of the equals button
def equals():
    global expression
    result = str(eval(expression)) #evaluates the expression 
    input_text.set(result)

input_text = StringVar()
 



#create frame for the input field
input_frame=Frame(win, width= 312, height =50, highlightcolor="Navyblue", highlightthickness=2)
input_frame.pack(side= TOP )

#create an input field inside the input_frame
input_field = Entry(input_frame, font = ("Arial", 23, "bold"), bg ="white",textvariable=input_text, justify=RIGHT)
input_field.grid(row=0, column= 0,pady=8)
input_field.pack(ipady = 13, ipadx=8) #internal padding to increase the height of the input

#create another frame to handle the buttons
btnsFrame = Frame(win,bg = "white", )
btnsFrame.pack()

#first row
btnclear = Button(btnsFrame, text = "C", bg = "light gray", fg = "black",command=lambda:clear_btn(), font = ("arial", 15,"bold"), borderwidth=0, width=7, height = 4,cursor="hand2")
btnclear.grid(row = 0, column=0)
sqr = Button(btnsFrame, text = "x\u00b2",  bg = "light gray", fg ="black", command =lambda:square(), font = ("arial", 15,"bold"),bd = 0,width = 7, height = 4, cursor="hand2")
sqr.grid(row =0, column=1 )
sqt = Button(btnsFrame, text = "\u221ax", bg = "light gray", fg ="black", command =lambda:sqrt(), bd = 0,font = ("arial", 15,"bold"),width = 7, height = 4, cursor="hand2")
sqt.grid(row =0, column=2 )
divide= Button(btnsFrame, text = "\u00F7", bg = "light gray", fg ="black", command =lambda:btn_click("/"), font = ("arial", 15,"bold"),bd = 0,width = 7, height = 4,cursor="hand2")
divide.grid(row =0, column=3 )

#second row
seven= Button(btnsFrame, text = "7", bg = "white", fg ="black", command =lambda:btn_click(7), bd = 0,font = ("arial", 15,"bold"),width = 7, height = 4, cursor="hand2")
seven.grid(row =1, column=0 )
eight= Button(btnsFrame, text = "8", bg = "white", fg ="black", command =lambda:btn_click(8), bd = 0,font = ("arial", 15,"bold"),width = 7, height = 4, cursor="hand2")
eight.grid(row =1, column=1 )
nine= Button(btnsFrame, text = "9", bg = "white", fg ="black", command =lambda:btn_click(9), bd = 0,font = ("arial", 15,"bold"),width = 7, height = 4, cursor="hand2")
nine.grid(row =1, column=2 )
multi= Button(btnsFrame, text = "\u00D7", bg = "light gray", fg ="black", command =lambda:btn_click("*"), font = ("arial", 15,"bold"),bd = 0,width = 7, height = 4, cursor="hand2")
multi.grid(row =1, column=3 )

#third row
four= Button(btnsFrame, text = "4", bg = "white", fg ="black", command =lambda:btn_click(4), bd = 0,font = ("arial", 15,"bold"),width = 7, height = 4, cursor="hand2")
four.grid(row =2, column=0 )
five= Button(btnsFrame, text = "5", bg = "white", fg ="black", command =lambda:btn_click(5), bd = 0,font = ("arial", 15,"bold"),width = 7, height = 4, cursor="hand2")
five.grid(row =2, column=1 )
six= Button(btnsFrame, text = "6", bg = "white", fg ="black", command =lambda:btn_click(6), bd = 0,font = ("arial", 15,"bold"),width = 7, height = 4, cursor="hand2")
six.grid(row =2, column=2 )
minus= Button(btnsFrame, text = "-", bg = "light gray", fg ="black", command =lambda:btn_click("-"), bd = 0,font = ("arial", 15,"bold"),width = 7, height = 4, cursor="hand2")
minus.grid(row =2, column=3 )

#fourth row
one= Button(btnsFrame, text = "1", bg = "white", fg ="black", command =lambda:btn_click(1), bd = 0,width = 7,font = ("arial", 15,"bold"), height = 4, cursor="hand2")
one.grid(row =3, column=0 )
two= Button(btnsFrame, text = "2", bg = "white", fg ="black", command =lambda:btn_click(2), bd = 0,width = 7,font = ("arial", 15,"bold"), height = 4, cursor="hand2")
two.grid(row =3, column=1 )
three= Button(btnsFrame, text = "3", bg = "white", fg ="black", command =lambda:btn_click(3), bd = 0,width = 7, font = ("arial", 15,"bold"),height =4, cursor="hand2")
three.grid(row =3, column=2 )
plus= Button(btnsFrame, text = "+", bg = "light gray", fg ="black", command =lambda:btn_click("+"), bd = 0,width = 7, font = ("arial", 15,"bold"),height = 4, cursor="hand2")
plus.grid(row =3, column=3 )

#fifth row
dot= Button(btnsFrame, text = ".", bg = "white", fg ="black", command =lambda:btn_click("."), bd = 0,width = 7, font = ("arial", 15,"bold"),height = 4, cursor="hand2")
dot.grid(row =4, column=0 )
zero= Button(btnsFrame, text = "0", bg = "white", fg ="black", command =lambda:btn_click(0), bd = 0, width =7, font = ("arial", 15,"bold"),height = 4, cursor="hand2")
zero.grid(row =4, column=1, )
percent= Button(btnsFrame, text = "%", bg ="white", fg ="black", command = lambda:percentage(), bd =0, font = ("arial", 15,"bold"), cursor ="hand2", height = 4, width = 7)
percent.grid(row =4, column = 2)
equal= Button(btnsFrame, text = "=", bg = "teal", fg ="black", command =lambda: equals(), bd = 0,width = 7, font = ("arial", 15,"bold"),height = 5, cursor="hand2")
equal.grid(row =4, column=3)

win.mainloop()