import tkinter as tk
from tkinter import filedialog
import docx
import webbrowser

def txt_to_docx(txt_file, docx_file):
    with open(txt_file, 'r') as f:
        text = f.read()
    
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(docx_file)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    txt_file.set(file_path)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word documents", "*.docx")])
    docx_file.set(file_path)

def convert():
    txt_file_path = txt_file.get()
    docx_file_path = docx_file.get()
    txt_to_docx(txt_file_path, docx_file_path)
    status.set("Conversion complete")
    
def github():
    webbrowser.open_new("https://github.com/KailUser/txt-to-doc")

root = tk.Tk()
root.title("TXT to DOCX")
root.geometry("270x120")

txt_file = tk.StringVar()
docx_file = tk.StringVar()
status = tk.StringVar()

frame = tk.Frame(root)
frame.pack()

open_button = tk.Button(frame, text="Open", command=open_file)
open_button.grid(row=0, column=0, padx=10)

save_button = tk.Button(frame, text="Save", command=save_file)
save_button.grid(row=0, column=1, padx=10)

convert_button = tk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=0, column=2, padx=10)

github_button = tk.Button(frame, text="GitHub", command=github)
github_button.grid(row=0, column=3, padx=10)

txt_entry = tk.Entry(frame, textvariable=txt_file)
txt_entry.grid(row=1, column=0, columnspan=4, pady=10)

docx_entry = tk.Entry(frame, textvariable=docx_file)
docx_entry.grid(row=2, column=0, columnspan=4, pady=10)

status_label = tk.Label(frame, textvariable=status)
status_label.grid(row=3, column=0, columnspan=4, pady=10)

root.mainloop()
