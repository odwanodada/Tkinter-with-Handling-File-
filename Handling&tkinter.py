from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry("700x400")
window.title("Temperature Conversion")
window.configure(bg="red")

#creating text file button
def create_text():
    file = open('/home/user/Desktop/Myactivities.txt', 'w+') #w+ to create a text file
    file.write("I am crazy\n")
    file.writelines("Beer Friday\n")
    file.write("Vodka Friday\n")
    file.write("Gin and Tonic\n")
    file.close()

#display function
def display_function():
    file = open('/home/user/Desktop/Myactivities.txt', 'r')# r read text file
    text_display = file.read() #you can give it any name
    output.insert(END,text_display)
    file.close()

#Clear function
def clear():
     output.delete("1.0", END)

#Appending function
def appending():
    file=open('/home/user/Desktop/Myactivities.txt', "a")# a to read a text file
    file.write(output.get("1.0","end-1c")+"\n")



#Exit Function
def exit():
    message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        window.destroy()
    else:
        pass

#The Label will display the words on Top
label1 = Label(window, text="My weekend Activies", bg="pink", font=("arial", 20, "bold"))
label1.place(x=30,y=1)


#Label is for output the results will be display there
output = Text(window, width=20, height=3, bg="white",font=("arial", 20, "bold"))
output.place(x=30,y=50)

#Clickable button will create a  Textfile
create_button = Button(window, text="CreateTextFile", bg="yellow", width=12, activeforeground="grey", font=("arial", 15, "bold"),command=create_text)
create_button.place(x=10,y=150)

#Display button if you click it will show everything you have done
display_button = Button(window, text="Display", bg="blue", width=7, activeforeground="grey", font=("arial", 15, "bold"),command=display_function)
display_button.place(x=180,y=150)

#Append button to the text file that is created
append_button = Button(window, text="Append Data", bg="green", width=12, activeforeground="grey", font=("arial", 15, "bold"),command=appending)
append_button.place(x=300,y=150)

#clear button remove everything on output text
clear_button = Button(window, text="Clear", bg="pink", width=7, activeforeground="grey", font=("arial", 15, "bold"),command=clear)
clear_button.place(x=470,y=150)

#Exit button to exit the window that I created
exit_button = Button(window, text="Exit", bg="red", width=7, activeforeground="grey", font=("arial", 15, "bold"),command=exit)
exit_button.place(x=580,y=150)



window.mainloop()