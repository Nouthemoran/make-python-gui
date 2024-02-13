import customtkinter as ct
import tkinter
app = ct.CTk()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

app.title("ini aplikasi gui tkinter")
app.geometry("500x500")

button = ct.CTkButton(master=app, text="Button")
button.place(relx=, rely=0.3, anchor = tkinter.CENTER)

app.mainloop()