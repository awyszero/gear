from tkinter import Tk,Label,Menu,Entry,Button,END
import databasehandling



root = Tk()    # make object from tk
menu_bar=Menu(root)  # make menu inside the tk object
file_menu = Menu(menu_bar)    # make anthor menu inside the menu_bar
file_menu.add_command(label="Exit",command=root.destroy)   # this is command of filemenu to give name to the filemenu and give it command to exit when it preassed
menu_bar.add_cascade(label="File",menu=file_menu)  # now we put the filemwnu in casecade named File
root.config(menu=menu_bar)    # here we config tk object to the menu_bar as it is main menu

root.title("drug information ")   # the name of the tk frame
root.geometry("500x500+0+0")  # here we set the width and height and set the location
ext =Label(root,text="دليل الادويه")
ext.config(font=('times',28,'italic bold underline '))  # here we config the label set the font
l0 =Label(root,text=":اسم الدواء")
l0.place(x=410,y=210)   # the loaction of the label
l0.config(font=('times',14,'italic bold '))
en0= Entry()  # here we create text box to use
en0.place(x=280,y=215)
l1= Label(root,text=":العائلة")
l1.place(x=410,y=250)
l1.config(font=('times',14,'italic bold '))
en1= Entry()
en1.place(x=280,y=250)


''' simple method that get text from the textarea that we have crated and clear the textarea after that '''
def gettxt():
     t = en0.get()     # get text that have been written by the user from textarea number 1
     r = en1.get()     # same ass above but get data from the textarea number 2
     databasehandling.enterdata(t,r)   # here we call the enterdata method
     print("data entered succssfully")   # here we print something
     en0.delete(0,END)   # here we delate the text that written by the user
     en0.insert(0,"")    # here we make the textare empity
     en1.delete(0,END)    # same as above but we change the textarea
     en1.insert(0,"")     # same as above

b0 =Button(root,text="ادخال",command=gettxt)   # make new button
b0.place(x=350,y=300)


ext.pack()
root.resizable(0,0)    # here we make the frame not resizeable
root.mainloop()     # start the farme