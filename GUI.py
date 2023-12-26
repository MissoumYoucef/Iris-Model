import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

class MyGUI():
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme('blue')

        app = ctk.CTk()
        app.geometry("720x500")
        app.title("Iris Model")

        app.columnconfigure(0, weight=1)
        app.columnconfigure(3, weight=1)
        app.columnconfigure(4, weight=1)
        app.columnconfigure(1, weight=1)
        app.columnconfigure(2, weight=6)
        app.rowconfigure(0, weight=1)
        app.rowconfigure(1, weight=1)
        app.rowconfigure(2, weight=1)
        
        label=ctk.CTkLabel(app, text="Insert a CSV file", font=("Arial", 18)) #Text 
        label.grid(row=0, column=1, sticky='nw',  padx=20, pady=20)

        #textbox=tk.Text(app, height=3 ,font=("Arial", 16)) #Text Field
        #textbox.pack()

        #myentry= ctk.CTkEntry(app, width=350, height=40)
        #myentry.pack(pady=20)#TextField with 1 line

        #Import Button
        file_image=Image.open("icon.png")
        self.file_path = tk.StringVar()

        btn_insert=ctk.CTkButton(app, text="Import", font=("Arial", 18), image=ctk.CTkImage(dark_image=file_image, size=(20,20)), compound="top", command=self.browse_file)
        #btn_insert.place(relx=200,rely=200, anchor="nw")
        btn_insert.grid(row=1, column=1, sticky='w',  padx=20, )
        
        #Output File Label
        self.label = ctk.CTkLabel(app, textvariable=self.file_path)
        self.label.grid(row=2, column=1)
        

        #Result Button
        btn_result=ctk.CTkButton(app, text="Result", font=("Arial", 18), command=self.show_path)
        #btn_result.place(relx=200,rely=200, anchor="center")
        btn_result.grid(column=3, row=1)

        #DropDown List
        self.algorithm=ctk.StringVar()
        list= ctk.CTkComboBox(app, values=["SVM","TensorFlow","KNN"], variable=self.algorithm, command=self.change_value)
        list.grid(row=1, column=2)
        
        #buttonframe= tk.Frame(app)
        #buttonframe.columnconfigure(0, weight=1)
        #buttonframe.columnconfigure(1, weight=1)
        #buttonframe.columnconfigure(2, weight=1)

        #buttonframe.pack(fill="x") #prend toute la largeur X 

        #valuecheck = tk.IntVar() # valeur de checkBox
        #check = tk.Checkbutton(app, text="Show", font=("Arial", 16), variable=self.valuecheck)
        #check.pack(padx=10, pady=10)

        app.mainloop()
    
    def show_message(self):
        #if valuecheck.get() == 0:
        #    print(self.textbox.get("1.0", tk.END))
        #else:
            messagebox.showinfo(title="Message", message=self.algorithm.get())
    
    def change_value(self, value):
        print(f"Selected value {value}")

    def browse_file(self):
        # Open a file dialog to get the file path
        file_path = tk.filedialog.askopenfilename()

        if not file_path:
            print("No file selected.")
            return

        # Check if the file has a .pdf extension
        if not file_path.lower().endswith('.csv'):
            print("Error not CSV")
        else:
            self.file_path.set(file_path)
            print("CSV file")

        # Update the StringVar with the selected file path
        

    def show_path(self):
        # Display the selected file path
        print("Selected File Path:", self.file_path.get())

MyGUI()

