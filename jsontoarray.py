from tkinter import *
import json
from tkinter.filedialog import asksaveasfile

root = Tk()

frame = Frame(root)
frame.pack(side=LEFT)

myLabel = Label(frame, text="Enter json data", font=("Arial Bold",18))
myLabel.pack()

entry = Text(frame, height=20, width=40, bd=5)
entry.focus()
entry.pack()

e = Entry(frame,text="Enter data key", width=50, bd=5)
e.pack()

def myClick():
    hello = entry.get("1.0",END)
    results = json.loads(hello)

    if not e.get():
            myLabel1 = Label(frame, text="No data was entered", font=("Arial Bold",8))
            myLabel1.pack()
    else:
        for result in results:
            myLabel = Label(frame, text=result[e.get()], font=("Arial Bold",8))
            myLabel.pack()


myButton = Button(frame, text="Convert", command = myClick, bd=5)
myButton.pack()

frame2 = Frame(root)
frame2.pack(side=RIGHT)

myLabel2 = Label(frame2, text="Enter array", font=("Arial Bold",18))
myLabel2.pack()

"""entry2 = Text(frame2, height=20, width=40, bd=5)
entry2.pack()"""

e1 = Entry(frame2,text="id", width=50, bd=5)
e1.insert(0, 'id')
e1.pack()

e2 = Entry(frame2,text="name", width=50, bd=5)
e2.insert(0, 'name')
e2.pack()

e3 = Entry(frame2,text="country", width=50, bd=5)
e3.insert(0, 'country')
e3.pack()

def writeToJSONFile(path, fileName, data):
        json.dump(data, path)
 
path = './'

def check():
    a = e1.get()
    b = e2.get()
    c = e3.get()
    print(a)
    print(b)
    print(c)
    data = {}
    data['id'] = a
    data['name'] = b
    data['country'] = c
    files = [('JSON File', '*.json')]
    fileName='IOTEDU'
    filepos = asksaveasfile(filetypes = files,defaultextension = json,initialfile='IOTEDU')
    writeToJSONFile(filepos, fileName, data)
    myLabel3 = Label(frame2, text="Success!", font=("Arial Bold",8))
    myLabel3.pack()
 
myButton1 = Button(frame2, text="Convert", command = check, bd=5)
myButton1.pack()


root.title('JSON-Array Converter')
root.mainloop()