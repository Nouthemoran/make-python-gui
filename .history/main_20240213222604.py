import customtkinter as ct

app = ct.CTk()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

app.title("ini aplikasi gui tkinter")
app.geometry("500x500")

button = ct.CTkButton(master=app, text="Button")
button.place(relx)

app.mainloop()