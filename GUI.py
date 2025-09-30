import customtkinter as tk

class LoginPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)   # attaching this frame to the root window

        # Title
        text_label = tk.CTkLabel(self, text="Welcome to Thompson Medical", font=("Arial", 20))
        text_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Username input
        self.username_entry = tk.CTkEntry(self, placeholder_text="Enter Username: ")
        self.username_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Password input
        password_entry = tk.CTkEntry(self, placeholder_text="Enter Password: ", show="*")
        password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Login button
        login_button = tk.CTkButton(
            self, 
            text="Login",
            command=lambda: controller.login(self.username_entry.get())  # Pass username to controller
        )
        login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)


class MessagingPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Sidebar (contacts/users list)
        sidebar = tk.CTkFrame(self, width=200, corner_radius=0)
        sidebar.pack(side="left", fill="y")

        # Show logged-in user
        user_label = tk.CTkLabel(
            sidebar, 
            text="User: " + (controller.username if hasattr(controller, "username") else "Unknown"),
            font=("Arial", 16)
        )
        user_label.pack(pady=10)

        contacts_label = tk.CTkLabel(sidebar, text="Contacts", font=("Arial", 14))
        contacts_label.pack(pady=(20, 10))

        # Placeholder contacts (for now)
        tk.CTkButton(sidebar, text="Dr. Smith").pack(pady=5, padx=10, fill="x")
        tk.CTkButton(sidebar, text="Nurse Amy").pack(pady=5, padx=10, fill="x")
        tk.CTkButton(sidebar, text="Patient John").pack(pady=5, padx=10, fill="x")

        chat_area = tk.CTkFrame(self)
        chat_area.pack(side="right", fill="both", expand=True)

        # Chat history
        self.chat_history = tk.CTkTextbox(chat_area, state="disabled", wrap="word")
        self.chat_history.pack(fill="both", expand=True, padx=10, pady=10)

        # Input area
        input_frame = tk.CTkFrame(chat_area)
        input_frame.pack(fill="x", padx=10, pady=10)

        self.message_entry = tk.CTkEntry(input_frame, placeholder_text="Type a message...")
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        send_button = tk.CTkButton(input_frame, text="Send", command=self.send_message)
        send_button.pack(side="right")

    def send_message(self):
        """Append a new message to the chat box."""
        message = self.message_entry.get()
        if message.strip():
            self.chat_history.configure(state="normal")
            self.chat_history.insert("end", f"You: {message}\n")
            self.chat_history.configure(state="disabled")
            self.chat_history.see("end")
            self.message_entry.delete(0, "end")


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
        for PageClass in (LoginPage, MessagingPage):
            frame = PageClass(container, self)
            self.frames[PageClass] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_page(LoginPage)

    def show_page(self, PageClass):
        frame = self.frames[PageClass]
        frame.tkraise()

    def login(self, username):
        """Handle login and move to MessagingPage"""
        self.username = username
        # Recreate MessagingPage so it gets updated username
        self.frames[MessagingPage] = MessagingPage(self.frames[MessagingPage].master, self)
        self.frames[MessagingPage].grid(row=0, column=0, sticky="nsew")
        self.show_page(MessagingPage)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = MainClass("Medical Messaging App", "900x600")
    app.run()
