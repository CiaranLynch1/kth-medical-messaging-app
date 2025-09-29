import customtkinter as tk

class LoginPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)   # attaching this frame to the root window

        # Widgets
        text_label = tk.CTkLabel(self, text="Welcome to Thompson Medical", font=("Arial", 20))
        text_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.username_entry = tk.CTkEntry(self, placeholder_text="Enter Username: ")
        self.username_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        password_entry = tk.CTkEntry(self, placeholder_text="Enter Password: ", show="*")
        password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        login_button = tk.CTkButton(
            self, 
            text="Login",
            command=lambda: controller.login(self.username_entry.get())  # Pass username
        )
        login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)


class HomePage(tk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        welcome_label = tk.CTkLabel(self, text="Messaging App", font=("Arial", 20))
        welcome_label.pack(pady=20)

        sidebar = tk.CTkFrame(self, width=200, corner_radius=0)
        sidebar.pack(side="left", fill="y")

        # Display username from controller
        self.user_label = tk.CTkLabel(
            sidebar, 
            text="User: " + (controller.username if hasattr(controller, "username") else "Unknown"),
            font=("Arial", 16)
        )
        self.user_label.pack(pady=10)


class MainClass(tk.CTk):
    def __init__(self, title, dimensions):
        super().__init__()
        self.title(title)
        self.geometry(dimensions)

        # Container to hold all pages
        container = tk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for PageClass in (LoginPage, HomePage):
            frame = PageClass(container, self)
            self.frames[PageClass] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_page(LoginPage)

    def show_page(self, PageClass):
        frame = self.frames[PageClass]
        frame.tkraise()

    def login(self, username):
        """Handle login and pass username to HomePage"""
        self.username = username
        # Refresh HomePage so it shows the username
        self.frames[HomePage] = HomePage(self.frames[HomePage].master, self)
        self.frames[HomePage].grid(row=0, column=0, sticky="nsew")
        self.show_page(HomePage)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = MainClass("Medical Messaging App", "800x600")
    app.run()
