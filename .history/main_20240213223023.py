import customtkinter as ct
import tkinter
app = ct.CTk()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

app.title("ini aplikasi gui tkinter")
app.geometry("500x500")

def 

button = ct.CTkButton(master=app, text="Button", command=button_function)
button.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

app.mainloop()