import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
from bs4 import BeautifulSoup
import html2text

# Initialize the main window
window = tk.Tk()

# Initialize Tikinter variables
fromFileTypeStr = tk.StringVar()
toFileTypeStr = tk.StringVar()
fromFileNameStr = tk.StringVar()

# Intialize filetype options
compatibleFileTypes = {
    ".png": [".jpg", ".bmp", ".tiff", ".pdf"],
    ".jpg": [".png", ".bmp", ".tiff", ".pdf"],
    ".bmp": [".png", ".jpg", ".tiff", ".pdf"],
    ".tiff": [".png", ".jpg", ".bmp", ".pdf"],
    ".pdf": [".png", ".jpg", ".bmp", ".tiff"],
    ".html": [".txt", ".json", ".xml", ".csv"],
    ".txt": [".html", ".json", ".xml", ".csv"],
    ".csv": [".txt", ".xml", ".json", ".html"],
    ".xml": [".txt", ".csv", ".json", ".html"],
    ".json": [".txt", ".csv", ".xml", ".html"]
    }

photoFileTypes = [
   ".png",
   ".jpg",
   ".gif",
   ".pdf",
   ".bmp",
   ".tiff"
   ]

textFileTypes = [
    ".txt",
    ".html",
    ".csv",
    ".xml",
    ".json"
    ]
def updateOptions():
    global toFileType
    toFileType.destroy()
    toFileType = tk.OptionMenu(optionsFrame, toFileTypeStr, *compatibleFileTypes[fromFileTypeStr.get()])
    toFileType.grid(row=1, column=2, sticky="ew")

def getFile():
    #Getting the file name and storing it as an attribute to the window object
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select file to convert")
    if window.filename:  
        fromFileNameStr.set(window.filename)
        for i in range(len(window.filename) - 1, -1, -1):
            if(window.filename[i] == '.'):
                fromFileTypeStr.set(window.filename[i:len(window.filename)])
                break
        if fromFileTypeStr.get() in compatibleFileTypes:
            updateOptions()


def errorCheck():
    if(fromFileNameStr.get() == "" or fromFileTypeStr.get() == ""):
        messagebox.showwarning(title="Warning", message="Please select a file to convert!")
        return True
    elif(toFileTypeStr.get() == ""):
        messagebox.showwarning(title="Warning", message="Please select a conversion type!")
        return True
    elif(fromFileTypeStr.get() not in compatibleFileTypes):
        messagebox.showwarning(title="Warning", message="Please select a compatable file type!")
        return True
    
def convert():
    #Checks for errors
    if(errorCheck()):
        return

    converted_file_path = filedialog.asksaveasfilename(defaultextension=toFileTypeStr.get(), filetypes=[("Conversion Type", toFileTypeStr.get())])

    if fromFileTypeStr.get() in photoFileTypes:
        #Gets the image
        image = Image.open(fromFileNameStr.get())

        if(converted_file_path):
            image.save(converted_file_path)
            messagebox.showinfo(title="Success!", message="Your file has been converted")
            fromFileNameStr.set("")
            fromFileTypeStr.set("")
            toFileTypeStr.set("")
        else:
            messagebox.showwarning(title="Warning", message="Please select file path!")
    elif fromFileTypeStr.get() in textFileTypes:
        with open(fromFileNameStr.get(), 'r') as txtFile:
            newFile = open(converted_file_path, 'w')
            newFile.write(txtFile.read())
            newFile.close()                                                
# Set window state
window.geometry("400x300")
window.title("File Converter")
icon = tk.PhotoImage(file="logo_transparent.png")
window.iconphoto(True, icon)

# Initialze widgets and pack into window
tk.Label(window, text="Convert your files!", bg='gray23', fg='white', font=("Arial", 20)).grid(row=0, column=0, sticky="ew")
optionsFrame = tk.Frame(window, bg='gray23', padx=50, pady=10)
optionsFrame.grid(row=1, column=0, sticky="ew")
window.grid_columnconfigure(0, weight=1)

# Center the optionsFrame widgets
fromFileType = tk.OptionMenu(optionsFrame, fromFileTypeStr, *compatibleFileTypes)
fromFileType.configure(state="disabled")
fromFileType.grid(row=1, column=0, sticky="ew")

tk.Label(optionsFrame, text=" to ", font=("Arial", 15), bg="gray23", fg='white').grid(row=1, column=1)

toFileType = tk.OptionMenu(optionsFrame, toFileTypeStr, *compatibleFileTypes)
toFileType.grid(row=1, column=2, sticky="ew")

# Configure column weights to make the buttons expand
optionsFrame.grid_columnconfigure(0, weight=1)
optionsFrame.grid_columnconfigure(2, weight=1)

tk.Label(optionsFrame, bg='gray23').grid(row=2, column=1)

fileUploadButton = tk.Button(optionsFrame, text="Choose file to upload", command=getFile)
fileUploadButton.grid(row=3, column=1)

convertButton = tk.Button(window, text="Convert!", font=("Arial", 15), command=convert)
convertButton.grid(row=2, column=0)

tk.Label(window, textvariable=fromFileNameStr).grid(row=3, column=0)

# Enter the mainloop()
window.mainloop()