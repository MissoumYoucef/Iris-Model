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
        
        label=ctk.CTkLabel(app, text="Insert a CSV file", font=("Arial", 18)) #Text 
        label.pack(padx=20, pady=20, side="left")

        #textbox=tk.Text(app, height=3 ,font=("Arial", 16)) #Text Field
        #textbox.pack()

        #myentry= ctk.CTkEntry(app, width=350, height=40)
        #myentry.pack(pady=20)#TextField with 1 line
        image=Image.open("icon.png")
        btn_insert=ctk.CTkButton(app, text="Import", font=("Arial", 18), image=ctk.CTkImage(dark_image=image, size=(20,20)), compound="top")#command=self.show_message)
        btn_insert.place(relx=200,rely=200, anchor="nw")
        btn_insert.pack(padx=10, pady=20)

        btn_result=ctk.CTkButton(app, text="Result", font=("Arial", 18), command=self.show_message)
        btn_result.place(relx=200,rely=200, anchor="center")
        btn_result.pack(side="bottom", pady=100)

        self.algorithm=ctk.StringVar()
        list= ctk.CTkComboBox(app, values=["SVM","TensorFlow","KNN"], variable=self.algorithm, command=self.change_value)
        list.pack(padx=20, pady=20)
        
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

MyGUI()

