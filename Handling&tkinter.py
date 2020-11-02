from tkinter import *
import os

window = Tk()
window.geometry("700x400")
window.title("Temperature Conversion")
window.configure(bg="red")

def create_text():
    file = open('/home/user/Desktop/Myactivities.txt', 'w+')
    file.write("I am crazy\n")
    file.writelines("Beer Friday\n")
    file.write("Vodka Friday\n")
    file.write("Gin and Tonic")
    file.close()


def display_function():
    file = open('/home/user/Desktop/Myactivities.txt', 'r')
    text_display = file.read()
    output.insert(END,text_display)
    file.close()

def clear():
     output.delete("1.0", END)

def appending():
    file=open('/home/user/Desktop/Myactivities.txt', "a")
    file.write(output.get("1.0","end-1c")+"\n")



label1 = Label(window, text="My weekend Activies", bg="pink", font=("arial", 20, "bold"))
label1.place(x=30,y=1)


#Label is for output
output = Text(window, width=20, height=3, bg="white",font=("arial", 20, "bold"))
output.place(x=30,y=50)

#Create textfile button
create_button = Button(window, text="CreateTextFile", bg="yellow", width=12, activeforeground="grey", font=("arial", 15, "bold"),command=create_text)
create_button.place(x=10,y=150)

#Display button
display_button = Button(window, text="Display", bg="blue", width=7, activeforeground="grey", font=("arial", 15, "bold"),command=display_function)
display_button.place(x=180,y=150)

#Append button
append_button = Button(window, text="Append Data", bg="green", width=12, activeforeground="grey", font=("arial", 15, "bold"),command=appending)
append_button.place(x=300,y=150)

#clear button
clear_button = Button(window, text="Clear", bg="pink", width=7, activeforeground="grey", font=("arial", 15, "bold"),command=clear)
clear_button.place(x=470,y=150)

#Exit button
exit_button = Button(window, text="Exit", bg="red", width=7, activeforeground="grey", font=("arial", 15, "bold"),command=window.quit)
exit_button.place(x=580,y=150)



window.mainloop()