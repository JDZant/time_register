import tkinter as tk
from tkinter import messagebox, PhotoImage
from app.controller.authentication_controller import AuthenticationController


class LoginView(tk.Frame):
    def __init__(self, master=None, on_login_success=None):
        super().__init__(master)
        self.auth_controller = AuthenticationController()
        self.on_login_success = on_login_success

        original_image = PhotoImage(file='resources/images/image_auto_nitro.png')
        self.login_image = original_image.subsample(3, 3)

        self.register_label = None
        self.email_label = None
        self.email_input = None
        self.password_label = None
        self.password_input = None
        self.action_button = None
        self.master = master
        self.is_register = False  # State to track whether we are in login or register mode
        self.create_widgets()

    def create_widgets(self):
        self.pack(anchor='center', expand=True)

        # Frame for containing all login widgets, centered in the window
        login_frame = tk.Frame(self)
        login_frame.grid(row=0, column=0, padx=50, pady=50)

        # Image at the top
        self.image_label = tk.Label(login_frame, image=self.login_image)
        self.image_label.image = self.login_image  # Keep a reference
        self.image_label.grid(row=0, column=0, columnspan=2, pady=2)

        # Email Label and Entry
        self.email_label = tk.Label(login_frame, text="Email")
        self.email_label.grid(row=1, sticky="e", padx=5)
        self.email_input = tk.Entry(login_frame)
        self.email_input.grid(row=1, column=1, pady=5)

        # Password Label and Entry
        self.password_label = tk.Label(login_frame, text="Password")
        self.password_label.grid(row=2, sticky="e", padx=5)
        self.password_input = tk.Entry(login_frame, show="*")
        self.password_input.grid(row=2, column=1, pady=5)

        # Login/Register Button
        self.action_button = tk.Button(login_frame, text="Login", command=self.login_or_register,
                                       width=15)
        self.action_button.grid(row=3, column=1, pady=5)

        # Register Account Label
        self.register_label = tk.Label(login_frame, text="Register Account", fg="blue", cursor="hand2")
        self.register_label.grid(row=4, column=0, columnspan=2, pady=5)
        self.register_label.bind("<Button-1>", self.toggle_login_register)

    def toggle_login_register(self, event=None):
        self.is_register = not self.is_register  # Toggle the state
        if self.is_register:
            self.action_button.config(text="Register")
            self.register_label.config(text="Login instead")
        else:
            self.action_button.config(text="Login")
            self.register_label.config(text="Register account")

    def login_or_register(self):
        email = self.email_input.get()
        password = self.password_input.get()

        if self.is_register:
            success, message = self.auth_controller.register_user(email, password)
            if success:
                messagebox.showinfo("Success", message)
                self.toggle_login_register()
            else:
                messagebox.showerror("Registration Failed", message)
        else:
            if self.auth_controller.login_user(email, password):
                if self.on_login_success:
                    self.on_login_success()
