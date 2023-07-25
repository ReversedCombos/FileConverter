import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

# Initialize the main window
window = tk.Tk()

# Initialize Tikinter variables
fromFileTypeStr = tk.StringVar()
toFileTypeStr = tk.StringVar()

# Intialize filetype options
fileTypes = [
    ".png",
    ".jpg"
]

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
fromFileType = tk.OptionMenu(optionsFrame, fromFileTypeStr, *fileTypes)
fromFileType.grid(row=1, column=0, sticky="ew")

tk.Label(optionsFrame, text=" to ", font=("Arial", 15), bg="gray23", fg='white').grid(row=1, column=1)

toFileType = tk.OptionMenu(optionsFrame, toFileTypeStr, *fileTypes)
toFileType.grid(row=1, column=2, sticky="ew")

# Configure column weights to make the buttons expand
optionsFrame.grid_columnconfigure(0, weight=1)
optionsFrame.grid_columnconfigure(2, weight=1)

tk.Label(optionsFrame, bg='gray23').grid(row=2, column=1)

fileUploadButton = tk.Button(optionsFrame, text="Choose file to upload")
fileUploadButton.grid(row=3, column=1)

convertButton = tk.Button(window, text="Convert!", font=("Arial", 15))
convertButton.grid(row=2, column=0)

# Enter the mainloop()
window.mainloop()
