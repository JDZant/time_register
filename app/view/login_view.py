import tkinter as tk
from tkinter import messagebox


class LoginView(tk.Frame):
    def __init__(self, auth_controller, master=None):
        super().__init__(master)
        self.master = master
        self.auth_controller = auth_controller
        self.is_register = False  # State to track whether we are in login or register mode
        self.create_widgets()

    def create_widgets(self):
        # Email Label and Entry
        self.email_label = tk.Label(self, text="Email:")
        self.email_label.grid(row=0, column=0, sticky="e", padx=5, pady=10)
        self.email_input = tk.Entry(self)
        self.email_input.grid(row=0, column=1, padx=5, pady=5)

        # Password Label and Entry
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.password_input = tk.Entry(self, show="*")
        self.password_input.grid(row=1, column=1, padx=5, pady=5)

        # Login/Register Button
        self.action_button = tk.Button(self, text="Login", command=self.login_or_register)
        self.action_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Register Account Label
        self.register_label = tk.Label(self, text="Register Account", fg="blue", cursor="hand2")
        self.register_label.grid(row=3, column=0, columnspan=2, pady=5)
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
            # Call the register function of the auth controller
            success, message = self.auth_controller.register_user(email, password)
            if success:
                messagebox.showinfo("Success", message)
                # Optionally switch back to login mode
                self.toggle_login_register()
            else:
                messagebox.showerror("Registration Failed", message)
        else:
            # Here you would call the auth controller's login method
            print(email, password)
            success, message = self.auth_controller.login_user(email, password)
            if success:
                messagebox.showinfo("Success", "You are now logged in.")
            else:
                messagebox.showerror("Login Failed", message)
