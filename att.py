import tkinter as tk
import pyautogui as pp
import pytesseract
from PIL import Image
win=tk.Tk()
win.title("Take Screenshot")
win.geometry("800x800")
pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def takeScreenshot():
    ss = pp.screenshot()
    for i in range(10):
        ss.save("image\sss.png")

def convert():
    var=(pytesseract.image_to_string(Image.open("image\sss.png")))
    file = open("data1.txt", "a+")


    # print((var))
    arr=['Sudhakaran','Sanjeev Kanth','Selva Ganesh','Sri Krishna','Sofia','Shalini','Steev']
    for i in range(len(arr)):
        if(arr[i] in var):
            print(arr[i] +" is present")
            file.write(arr[i]+" is present\n")
    file.close()

button1=tk.Button(win,text="Take attendence",command=takeScreenshot)
button2=tk.Button(win,text="Convert",command=convert)

button1.pack()
button2.pack()
win.mainloop()
     