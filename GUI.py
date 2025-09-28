# Handles the Tkinter windows and layouts
import customtkinter as tk

def start_app():
    window = tk.CTk()
    window.title("Health Database App")
    window.geometry("800x600")
    label = tk.CTkLabel(window, text="Welcome to the Health Database App", font=("Arial", 16))
    label.pack(pady=20, padx=20)
    window.mainloop()



