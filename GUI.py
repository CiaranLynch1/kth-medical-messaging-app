import customtkinter as tk

class LoginPage(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)   # attaching this frame to the root window
        # Widgets
        text_label = tk.CTkLabel(self, text="Welcome to Thompson Medical", font=("Arial", 20))
        text_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        login_button = tk.CTkButton(self, text="Login")
        login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        password_entry = tk.CTkEntry(self, placeholder_text="Enter Password: ", show="*")
        password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        username_entry = tk.CTkEntry(self, placeholder_text="Enter Username: ")
        username_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        
class MainClass(tk.CTk):
    def __init__(self, title, dimensions):
        super().__init__()
        self.title(title)
        self.geometry(dimensions)

        # Add login page inside root
        self.login_page = LoginPage(self)
        self.login_page.pack(fill="both", expand=True)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = MainClass("Medical Messaging App", "800x600")
    app.run()
