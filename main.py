import tkinter as tk
import PIL.ImageTk
from PIL import Image, ImageTk
from tkinter import filedialog

#Initialize the main window
window = tk.Tk()

#Initalize Tikinter variables
fromFileTypeStr = tk.StringVar()
toFileTypeStr = tk.StringVar()

#Intialize filetype options
fileTypes = [
    ".png",
    ".jpg"
]

#Set window state
window.geometry("750x750")
window.title("File Converter")
icon = tk.PhotoImage(file = "logo_transparent.png")
window.iconphoto(True, icon)

#Initialze widgets and pack into window
optionsFrame = tk.LabelFrame(window, text="Frame", padx=50, pady=50)
optionsFrame.pack()
fromFileType = tk.OptionMenu(optionsFrame, fromFileTypeStr, *fileTypes)
fromFileType.grid(row=0, column=0)
toFileType = tk.OptionMenu(optionsFrame, toFileTypeStr, *fileTypes)
toFileType.grid(row=-0, column=1)

fileUploadButton = tk.Button(window, text="Choose file to upload", padx=20, pady=20)
fileUploadButton.pack()

#Enter the mainloop()
window.mainloop()