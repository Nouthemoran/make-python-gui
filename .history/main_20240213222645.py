import customtkinter as ct
import t
app = ct.CTk()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

app.title("ini aplikasi gui tkinter")
app.geometry("500x500")

button = ct.CTkButton(master=app, text="Button")
button.place(relx=0.5, rely=0.3, anchor = tKinter.CENTER)

app.mainloop()