import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import subprocess
import importlib.util
import model

class MyGUI():
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme('blue')

        app = ctk.CTk()
        app.geometry("720x500")
        app.title("Iris Model")

        app.columnconfigure((0,4), weight=1)
        app.columnconfigure((1,3), weight=3)
        app.columnconfigure(2, weight=6)
        app.rowconfigure(3, weight=1)
        app.rowconfigure((0,2), weight=2)
        
        #Title Page
        home_frame=ctk.CTkFrame(app,corner_radius=30)
        label_page=ctk.CTkLabel(home_frame, text="Iris Model", font=("Arial", 26))
        label_page.grid_configure(column=2, row=0, padx=20)
        home_image=Image.open("home.png")
        home=ctk.CTkLabel(home_frame, image=ctk.CTkImage(home_image, size=(100,100)),)
        home.grid_configure(column=1, row=0)
        
        home_frame.grid_configure(row=0, column=2, sticky="we")

        #textbox=tk.Text(app, height=3 ,font=("Arial", 16)) #Text Field
        #textbox.pack()

        #myentry= ctk.CTkEntry(app, width=350, height=40)
        #myentry.pack(pady=20)#TextField with 1 line

        #---Import Frame---
        file_frame=ctk.CTkFrame(app, height=50, corner_radius=10)

        label_insert=ctk.CTkLabel(file_frame, text="Insert a CSV file", font=("Arial", 18)) #Text 
        label_insert.grid_configure(row=1, column=1, sticky='ew',  padx=20, pady=20)
        #Import Button
        file_image=Image.open("icon.png")
        self.file_path = tk.StringVar()
        btn_insert=ctk.CTkButton(file_frame, text="Import", font=("Arial", 18), image=ctk.CTkImage(dark_image=file_image, size=(20,20)), compound="top", command=self.browse_file)
        btn_insert.grid_configure(row=2, column=1, sticky='we', padx=20, ipady=2)
        
        #Output File Label
        self.label = ctk.CTkLabel(file_frame, textvariable=self.file_path)
        self.label.grid_configure(row=3, column=1, sticky="we", padx=10, pady=10)
        
        file_frame.grid_configure(row=2, column=0, )#sticky="ns")


        #Result Button
        btn_result=ctk.CTkButton(app, text="Result", font=("Arial", 18), command=self.show_result)
        #btn_result.place(relx=200,rely=200, anchor="center")
        btn_result.grid_configure(column=3, row=2)

        #Frame Model
        model_frame= ctk.CTkFrame(app, height=50, corner_radius=10)

        #DropDown Model    
        self.list= ctk.CTkComboBox(model_frame, values=["SVM","TensorFlow","KNN"],command=self.change_option)
        self.list.grid_configure(row=2, column=2)
        
        text=ctk.CTkLabel(model_frame, text="Choose an algorithm and options", font=("Arial", 16))
        text.grid_configure(row=1,column=2, padx=10, pady=10)
        #DropDown Kernel Option
        self.svm_values=["Linear","Rbf","Sigmoid"]
        self.option_list= ctk.CTkComboBox(model_frame, values=self.svm_values, command=self.change_option)
        self.option_list.grid_configure(row=3, column=2, pady=20)

        model_frame.grid_configure(row=2, column=2, )
        
        #Result Label
        self.result = tk.StringVar()
        self.result_label = ctk.CTkLabel(app, textvariable=self.result)
        self.result_label.grid_configure(row=3, column=2)
        
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
    
    def change_option(self, value):
        algorithm=self.list.get()
        print(f"Selected Model: {value}")
        if algorithm == "SVM":
            
            self.option_list.configure(values=self.svm_values)
            #self.option_list.set("")
        elif algorithm == "KNN":
            knn_values=["1","3","5","7","9"]
            self.option_list.configure(values=knn_values)
            #self.option_list.set("")
        else:
            print("Error")

    def browse_file(self):
        # Open a file dialog to get the file path
        file_path = tk.filedialog.askopenfilename()

        if not file_path:
            error="Error: No file selected."
            self.file_path.set(error)
            print(error)
            return

        # Check if the file has a .csv extension
        if not file_path.lower().endswith('.csv'):
            error="Error: It isn't a CSV file"
            self.file_path.set(error)
            print(error)
        else:
            self.file_path.set(file_path)
            print("CSV file")

        
    def show_result(self):
        # Get the model choosed
        algorithm=self.list.get()
        option=self.option_list.get()
        if algorithm == "SVM":
            accuracy_result=model.svm(option.lower())
        elif algorithm == "KNN":
            accuracy_result=model.knn(int(option))
        else:
            print("Error")
        # Display the accuracy
        self.result.set(f"Accuracy = {accuracy_result*100:.2f}%")
        
        #print("Selected File Path:", self.file_path.get())

MyGUI()

